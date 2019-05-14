import pytest
import hashlib

from plenum.common.constants import TARGET_NYM
from plenum.common.util import get_utc_epoch
from plenum.common.messages.fields import TimestampField
from plenum.common.types import f

from plenum.test.txn_author_agreement.conftest import random_taa
from plenum.test.txn_author_agreement.acceptance.conftest import (
    taa_acceptance, taa_digest, taa_acceptance_mechanism, taa_acceptance_time
)
from .helper import gen_nym_operation


@pytest.fixture
def operation():
    return gen_nym_operation()


@pytest.fixture
def operation_invalid(operation):
    operation[TARGET_NYM] = "1"
    return operation


@pytest.fixture
def taa_acceptance_invalid(taa_acceptance):
    taa_acceptance[f.TAA_ACCEPTANCE_TIME.nm] = TimestampField._oldest_time - 1
    return taa_acceptance
