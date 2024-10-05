import algosdk
from algosdk import transaction

algod = algosdk.v2client.algod.AlgodClient(
    "", "https://testnet-api.4160.nodely.dev"
)
PK = "tp2dMG+DUyD3X7NTM23HtWS3Jb8jS2233jkJME7pGs6gbr+ECyY8mOWP1K3rAnOtakUDSGrA3Q4Xa9byhREtHg=="
ADDRESS = "UBXL7BALEY6JRZMP2SW6WATTVVVEKA2INLAN2DQXNPLPFBIRFUPHWDHRWE"

def main() -> None:
    sp = algod.suggested_params() #obtener parametro

    # creaar la transacción
    txn = transaction.AssetCreateTxn(
        sender=ADDRESS,
        sp=sp,
        total=1000,
        decimals=2,
        unit_name="A2",
        asset_name="Testing Asset 2",
        default_frozen=False,
    )

    #firmar la transacción
    signed_txn = txn.sign(PK)
    #enviar la transacción
    txid = algod.send_transaction(signed_txn)
    #hash de la transacción
    print(f"Sent asset create transaction with txid: {txid}")
    results = transaction.wait_for_confirmation(algod, txid, 2)
    print(f"Result confirmed in round: {results['confirmed-round']}")


main()
