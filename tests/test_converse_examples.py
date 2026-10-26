"""Checks for scalar baselines and continuum nonlinear separation evidence."""
from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from exact_verify_converse import verify_scalar_baseline, verify_nonlinear_recovery


class ConverseExampleTests(unittest.TestCase):
    def test_scalar_baseline_has_the_stronger_exact_margin(self):
        result=verify_scalar_baseline()
        self.assertEqual(result["global_propagation_margin"],"1/20")
        self.assertGreater(Q(result["global_propagation_margin"]),Q(73,2500))

    def test_scalar_baseline_rejects_margin_violating_endpoint(self):
        with self.assertRaisesRegex(ValueError,"endpoint"):
            verify_scalar_baseline(eta=Q(1,10))

    def test_cubic_family_has_global_polynomial_and_mixed_pair_proofs(self):
        result=verify_nonlinear_recovery()
        self.assertEqual(result["robust_successor_infinity_norm_bound"],"247/500")
        self.assertEqual(result["minimum_degree_scope"]["scalar_constant_comparison"],2)
        self.assertEqual(result["minimum_degree_scope"]["finite_fixed_anchor_vector"],1)

    def test_smaller_positive_nonlinear_parameter_is_verified(self):
        result=verify_nonlinear_recovery(theta=Q(1,80))
        self.assertEqual(result["theta"],"1/80")

    def test_wrong_rotation_coupling_is_rejected(self):
        result=verify_nonlinear_recovery()
        matrix=[[Q(v) for v in row] for row in result["A"]]
        matrix[0]=[Q(0),Q(9,10),Q(0),Q(0)]
        with self.assertRaisesRegex(ValueError,"cubic comparison identity"):
            verify_nonlinear_recovery(matrix=matrix)

    def test_invalid_propagation_margin_is_rejected(self):
        with self.assertRaisesRegex(ValueError,"perturbation margin"):
            verify_nonlinear_recovery(eta=Q(1,10))

    def test_uncertified_independent_error_radius_is_rejected(self):
        with self.assertRaisesRegex(ValueError,"feature-error radius"):
            verify_nonlinear_recovery(eps=Q(1,50))


if __name__=="__main__":
    unittest.main()
