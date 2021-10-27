# samplecontract.py
from pyteal import *
from pyteal import (
    Return,
    compileTeal,
    Int,
    Seq,
    And,
    Bytes,
    Txn,
    TxnType,
    If,
    App,
    Gtxn,
    Assert,
    Global,
    Cond,
    Mul,
    Btoi,
    OnComplete,
    Mode,
)

"""Basic Counter Application"""


def approval_program():
    on_creation = Seq([App.globalPut(Bytes("Creator"), Txn.sender()), Return(Int(1))])
    handle_optin = Return(Int(1))
    handle_closeout = Return(Int(1))
    handle_updateapp = Return(Int(0))
    handle_deleteapp = If(
        # Condition
        App.globalGet(Bytes("Creator")) == Txn.sender(),
        # Then
        Return(Int(1)),
        # Else
        Return(Int(0)),
    )

    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp],
        # [Txn.on_completion() == OnComplete.NoOp, handle_noop],
    )

    return program


def clear_state_program():
    program = Return(Int(1))
    # Mode.Application specifies that this is a smart contract
    return program


if __name__ == "__main__":
    with open("approval.teal", "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled)

    with open("clear_state.teal", "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=5)
        f.write(compiled)
