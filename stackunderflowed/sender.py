from algosdk import transaction

from stackunderflowed.clients import fetch_algod_client
from stackunderflowed.wallets import account_private_key, account_public_key


# Function from Algorand Inc.
def wait_for_confirmation(client, txid):
    last_round = client.status().get("last-round")
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get("confirmed-round") and txinfo.get("confirmed-round") > 0):
        print("Waiting for confirmation")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print("Transaction confirmed in round", txinfo.get("confirmed-round"))
    return txinfo


def send_grind_token(recipient_address: str, send_amount: int) -> bool:
    algod_client = fetch_algod_client()
    # get suggested parameters from Algod
    params = algod_client.suggested_params()

    gh = params.gh
    first_valid_round = params.first
    last_valid_round = params.last
    fee = params.min_fee

    existing_account = account_public_key

    # Create and sign transaction
    tx = transaction.AssetTransferTxn(
        existing_account,
        fee,
        first_valid_round,
        last_valid_round,
        gh,
        recipient_address,
        send_amount,
        33020017,
        flat_fee=True,
    )
    signed_tx = tx.sign(account_private_key)

    try:
        tx_confirm = algod_client.send_transaction(signed_tx)
        print("Transaction sent with ID", signed_tx.transaction.get_txid())
        wait_for_confirmation(algod_client, txid=signed_tx.transaction.get_txid())
        return True
    except Exception as e:
        print(e)
    return False
