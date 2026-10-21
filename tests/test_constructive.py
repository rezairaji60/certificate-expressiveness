"""Exact acceptance and rejection checks for a finite continuum certificate."""
import json
from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from constructive_converse import MATRIX_FILE, replay, validate_matrix


class ConstructiveCertificateTests(unittest.TestCase):
    def setUp(self):
        payload = json.loads(MATRIX_FILE.read_text(encoding="utf-8"))
        self.matrix = [[Q(v) for v in row] for row in payload["A"]]

    def test_exact_continuum_certificate_with_both_feature_errors(self):
        report = replay(self.matrix)
        self.assertEqual(report["status"], "EXACT_CONSTRUCTIVE_EVIDENCE_VERIFIED")
        self.assertGreater(Q(report["finite_lp"]["minimum_exact_lp_slack"]), 0)
        self.assertLess(Q(report["finite_lp"]["maximum_row_sum"]), 1)

    def test_deleting_anchor_row_fails(self):
        self.matrix[0] = [Q(0)]*12
        with self.assertRaisesRegex(ValueError, "Finite LP inequality"):
            validate_matrix(self.matrix)

    def test_negative_comparison_entry_fails(self):
        self.matrix[0][0] = Q(-1, 1000)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            validate_matrix(self.matrix)

    def test_uncertified_smaller_source_cover_fails(self):
        with self.assertRaisesRegex(ValueError, "certified cover radii"):
            validate_matrix(self.matrix, xi_s=Q(0))

    def test_uncertified_smaller_successor_cover_fails(self):
        with self.assertRaisesRegex(ValueError, "certified cover radii"):
            validate_matrix(self.matrix, xi_t=Q(0))

    def test_excessive_propagation_margin_fails(self):
        with self.assertRaisesRegex(ValueError, "Finite LP inequality"):
            validate_matrix(self.matrix, eta=Q(1, 10))


if __name__ == "__main__":
    unittest.main()
