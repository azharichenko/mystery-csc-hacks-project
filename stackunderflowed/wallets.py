from algosdk import mnemonic

from stackunderflowed import fetch_configuration

config = fetch_configuration()

# Initalize throw-away account for this example - check that is has funds before running script
mnemonic_phrase = config.custodian_wallet_mnemonic
account_private_key = mnemonic.to_private_key(mnemonic_phrase)
account_public_key = mnemonic.to_public_key(mnemonic_phrase)
