"""
Contract for Purchasing Simple Script tokens using Grind Toekns
"""
from pyteal import (
    Seq,
    Return,
    App,
    Bytes,
    Int,
    And,
    Global,
    Txn,
    If,
    ScratchVar,
    TealType,
    Cond,
    OnComplete,
    Mode,
    compileTeal,
)

from mechanics import StatefulApplication, StatelessApplication


class SimpleScriptPurchaseApp(StatefulApplication):
    def __init__(self) -> None:
        pass

    def on_creation(self):
        return Seq([App.globalPut(Bytes("Count"), Int(0)), Return(Int(1))])

    def handle_optin(self):
        return Return(Int(0))

    def handle_closeout(self):
        return Return(Int(0))

    def handle_updateapp(self):
        return Return(Int(0))

    def handle_deleteapp(self):
        return Return(Int(0))

    def handle_noop(self):
        scratchCount = ScratchVar(TealType.uint64)

        add = Seq(
            [
                scratchCount.store(App.globalGet(Bytes("Count"))),
                App.globalPut(Bytes("Count"), scratchCount.load() + Int(1)),
                Return(Int(1)),
            ]
        )

        deduct = Seq(
            [
                scratchCount.store(App.globalGet(Bytes("Count"))),
                If(
                    scratchCount.load() > Int(0),
                    App.globalPut(Bytes("Count"), scratchCount.load() - Int(1)),
                ),
                Return(Int(1)),
            ]
        )

        handle_noop = Cond(
            [
                And(
                    Global.group_size() == Int(1),
                    Txn.application_args[0] == Bytes("Add"),
                ),
                add,
            ],
            [
                And(
                    Global.group_size() == Int(1),
                    Txn.application_args[0] == Bytes("Deduct"),
                ),
                deduct,
            ],
        )

        return handle_noop

    @property
    def approval_program(self):
        program = Cond(
            [Txn.application_id() == Int(0), self.on_creation()],
            [Txn.on_completion() == OnComplete.OptIn, self.handle_optin()],
            [Txn.on_completion() == OnComplete.CloseOut, self.handle_closeout()],
            [
                Txn.on_completion() == OnComplete.UpdateApplication,
                self.handle_updateapp(),
            ],
            [
                Txn.on_completion() == OnComplete.DeleteApplication,
                self._handle_deleteapp(),
            ],
            [Txn.on_completion() == OnComplete.NoOp, self.handle_noop()],
        )
        return compileTeal(program, Mode.Application, version=4)

    @property
    def clear_state_program(self):
        program = Return(Int(1))
        return compileTeal(program, Mode.Application, version=4)
