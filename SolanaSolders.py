# This version of the transfer uses solana and solders libraries


# Import Packages etc
import base58

from solana.rpc.api import Client
from solana.transaction import Transaction

from solders.system_program import TransferParams, transfer
from solders.pubkey import Pubkey
from solders.keypair import Keypair

# Initialise Client
solana_client = Client("https://api.mainnet-beta.solana.com")

# Address Variables
from_address = 'Sending_Address'
from_address = base58.b58decode(from_address)

to_address = 'Receiving_Address'
to_address = base58.b58decode(to_address)

# Configure Private KEY
priv_key = 'Private_KEY'
priv_key = base58.b58decode(priv_key)

# How much Sol do you want to send?
sol_amount = 0.01

# Setup transfer parameters
transfer_parameters = TransferParams(
    from_pubkey=Pubkey(from_address),
    to_pubkey=Pubkey(to_address),
    lamports=int(sol_amount*(10**9))
)

# Create transaction
sol_transfer = transfer(transfer_parameters)
transaction = Transaction().add(sol_transfer)

# Sign Transaction
transaction_result = solana_client.send_transaction(transaction, Keypair.from_bytes(priv_key))

# Print Transaction
print(transaction_result)
