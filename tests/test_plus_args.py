import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

import pytest
from cocotb_test.run import run
import os


@cocotb.test(skip=False)
def run_test(dut):

    yield Timer(1)

    user_mode = int(dut.user_mode)

    if user_mode != 1:
        raise TestFailure(
            "user_mode mismatch detected : got %d, exp %d!" % (dut.user_mode, 1)
        )


@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="Verilog not suported")
def test_plus_args():
    run(
        verilog_sources=["plus_args.v"],
        toplevel="plus_args",
        plus_args=["+USER_MODE", "+TEST=ARB_TEST"],
    )


@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="Verilog not suported")
@pytest.mark.xfail
def test_plus_args_fail():
    run(verilog_sources=["plus_args.v"], toplevel="plus_args")


@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="Verilog not suported")
@pytest.mark.xfail
def test_plus_args_test_wrong():
    run(
        verilog_sources=["plus_args.v"], toplevel="plus_args", plus_args=["+XUSER_MODE"]
    )


if __name__ == "__main__":
    test_plus_args()
