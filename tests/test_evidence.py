"""Evidence checks and rejection of invalid moment witnesses."""
import sys
from pathlib import Path
import unittest
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from exact_verify import verify, validate_witness


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.a, self.u, self.v = F(12,25), F(1641,3200), F(103,200)
        self.f = lambda x: x*(1+F(1,2)*(x*x-F(1,4))*(1-x*x))
        self.mu = [(F(0),F(369,625)),(-F(3,4),F(128,625)),(F(3,4),F(128,625))]
        self.mu0 = [(-self.a,F(1,2)),(self.a,F(1,2))]
        self.nu = [(-self.u,F(1,2)),(self.u,F(1,2))]

    def test_continuum_evidence_and_exact_margins(self):
        self.assertEqual(verify()["status"], "EXACT_EVIDENCE_VERIFIED")

    def test_degree_four_witness_must_fail(self):
        with self.assertRaisesRegex(ValueError,"Initial moments"):
            validate_witness(self.mu,self.mu0,self.nu,self.f,4,self.a,self.u,self.v)

    def test_corrupted_successor_moment_must_fail(self):
        bad = [(-self.v,F(1,2)),(self.v,F(1,2))]
        with self.assertRaisesRegex(ValueError,"Successor moments"):
            validate_witness(self.mu,self.mu0,bad,self.f,3,self.a,self.u,self.v)

    def test_negative_weight_must_fail(self):
        bad = [(F(0),F(-1)),(F(1),F(2))]
        with self.assertRaisesRegex(ValueError,"nonnegative"):
            validate_witness(bad,self.mu0,self.nu,self.f,3,self.a,self.u,self.v)

    def test_wrong_support_must_fail(self):
        bad = [(F(0),F(1))]
        with self.assertRaisesRegex(ValueError,"Unsafe support"):
            validate_witness(self.mu,self.mu0,bad,self.f,3,self.a,self.u,self.v)


if __name__ == "__main__":
    unittest.main()
