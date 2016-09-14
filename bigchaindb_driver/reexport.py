"""Module re-exports for users of the driver"""
from bigchaindb_common.transaction import Transaction

create_transfer_transaction = Transaction.transfer
