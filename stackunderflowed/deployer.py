import base64

from algosdk.future import transaction

from mechanics import StatefulApplication, StatelessApplication

from stackunderflowed.clients import fetch_algod_client
from stackunderflowed.sender import wait_for_confirmation
from stackunderflowed.wallets import account_private_key

def compile_smart_signature(client, source_code):
    compile_response = client.compile(source_code)
    return compile_response['result'], compile_response['hash']


def compile_program(client, source_code):
    compile_response = client.compile(source_code)
    return base64.b64decode(compile_response['result'])

def create_app(approval_program, clear_program, global_schema, local_schema):
    client = fetch_algod_client()
    
    # define sender as creator
    sender = account_private_key

    # declare on_complete as NoOp
    on_complete = transaction.OnComplete.NoOpOC.real

    # get node suggested parameters
    params = client.suggested_params()

    # create unsigned transaction
    txn = transaction.ApplicationCreateTxn(sender, params, on_complete, \
                                            approval_program, clear_program, \
                                            global_schema, local_schema)

    # sign transaction
    signed_txn = txn.sign(private_key)
    tx_id = signed_txn.transaction.get_txid()

    # send transaction
    client.send_transactions([signed_txn])

    # await confirmation
    wait_for_confirmation(client, tx_id, 5)

    # display results
    transaction_response = client.pending_transaction_info(tx_id)
    app_id = transaction_response['application-index']
    print("Created new app-id:", app_id)

    return app_id



def deploy_stateful_contract(contract: StatefulApplication) -> bool:
    pass

def deploy_smart_signiture(contract: StatelessApplication) -> bool:
    pass