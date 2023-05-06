from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair

client = Client("https://api.mainnet-beta.solana.com")

sender = Keypair.from_private_key("PRIVATE_KEY")
receiver = PublicKey("PUBLIC_KEY_TO_SEND_TO")
sol_amount = 0.01

instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver, 
        lamports=int(sol_amount*(10**9))
    )

transaction = Transaction(instructions=[instruction], signers=[sender])
result = client.send_transaction(transaction)
print("Transaction response: ", result)
