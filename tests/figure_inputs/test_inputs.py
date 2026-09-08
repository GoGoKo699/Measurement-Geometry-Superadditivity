from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D
import csv,json,sys,tempfile,shutil,unittest
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'numerics/figure_inputs'))
import build_inputs as build
import verify_inputs as verify

def rows(name):
    with (ROOT/'data/figures'/name).open()as f:return list(csv.DictReader(f))

class FigureInputs(unittest.TestCase):
    def test_source_identity(self):
        _,r=build.validate_source(build.DEFAULT_SOURCE)
        self.assertEqual(r['verified_manifest_entries'],len(json.loads((ROOT/'provenance/CANONICAL_INPUTS.json').read_text())['files']))
    def test_witness_bounds_are_source(self):
        raw,_=build.validate_source(build.DEFAULT_SOURCE)
        self.assertEqual(raw[build.WITNESS],(ROOT/'data/figures/figure1_original_witness140.json').read_bytes())
    def test_global_zero_marker(self):
        r=rows('figure1_comparison.csv')[0]
        self.assertEqual(F(r['lower']),0);self.assertEqual(F(r['upper']),0)
        self.assertIn('global',r['status'])
    def test_all_nine_mask_terms(self):
        r=rows('figure1_all_masks_not_for_display.csv')
        self.assertEqual([int(x['measured'])for x in r],list(range(9)))
        self.assertEqual(sum((F(x['mask_probability_exact'])for x in r),F(0)),1)
        self.assertLess(F(r[-1]['upper']),0)
    def test_noise_grid(self):
        r=rows('figure2_pauli_guaranteed_region.csv')
        self.assertEqual(len(r),1001)
        self.assertEqual([F(x['epsilon_exact'])for x in r],[F(j,2000)for j in range(1001)])
    def test_no_interior_theorem_at_noise_endpoints(self):
        r=rows('figure2_pauli_guaranteed_region.csv')
        for x in [r[0],r[-1]]:
            self.assertEqual(x['theorem_applies'],'False');self.assertEqual(F(x['certified_width']),0)
        self.assertTrue(all(x['theorem_applies']=='True' for x in r[1:-1]))
    def test_strict_frontier_and_capacity_caveat(self):
        self.assertTrue(all(x['upper_p_endpoint_included']=='False' and x['exact_capacity_boundary']=='False'for x in rows('figure2_pauli_guaranteed_region.csv')))
    def test_witness_not_in_conservative_band(self):
        c=json.loads((ROOT/'data/figures/cross_figure_witness_bound_check.json').read_text())
        self.assertLess(F(c['p_witness']),F(c['p_cert_from_uniform_3_over_35_bound']['lower']))
        self.assertLess(F(c['p_single_use_exact']),F(c['p_witness']))
    def test_safe_cone_domain(self):
        r=rows('figure3_cone_gap.csv');self.assertEqual(len(r),501)
        self.assertEqual(F(r[0]['lambda_exact']),0);self.assertEqual(F(r[-1]['lambda_exact']),F(1,4))
        with self.assertRaises(ValueError):build.cone_slice(F(1,3))
    def test_exact_cone_endpoint_and_slope(self):
        r=rows('figure3_cone_gap.csv')
        self.assertEqual(F(r[-1]['p_one_use_exact_rational']),F(7,10))
        self.assertTrue(all(F(x['asymptote_slope_exact'])==F(18,289)for x in r))
    def test_geometry_snapshots(self):
        r=rows('figure3_cone_geometry.csv')
        self.assertEqual(len(r),9)
        self.assertEqual({F(x['lambda_exact'])for x in r},{F(0),F(1,16),F(1,4)})
    def test_contract_keeps_distinctions(self):
        c=json.loads((ROOT/'figures/FIGURE_CONTRACT.json').read_text())
        self.assertFalse(c['figure_2']['overlay_figure1_witness'])
        self.assertFalse(c['figure_3']['plot']['capacity_threshold_claim'])
        self.assertFalse(c['figure_3']['plot']['fit_slope_from_data'])
        self.assertFalse(c['rendered'])
    def test_all_scalar_rows_independently_checked(self):
        self.assertTrue(verify.verify(ROOT/'data/figures')['passed'])
    def test_tampered_witness_rejected(self):
        with tempfile.TemporaryDirectory()as td:
            target=Path(td)/'data';shutil.copytree(ROOT/'data/figures',target)
            p=target/'figure1_original_witness140.json';p.write_bytes(p.read_bytes()+b'\n')
            with self.assertRaises(AssertionError):verify.verify(target)
    def test_wrong_cone_interval_rejected(self):
        with tempfile.TemporaryDirectory()as td:
            target=Path(td)/'data';shutil.copytree(ROOT/'data/figures',target)
            p=target/'figure3_cone_gap.csv';rs=verify.read_csv(p);rs[-1]['gap_lower']='0.1'
            build.save_csv(p,rs)
            with self.assertRaises(AssertionError):verify.verify(target)
    def test_generation_not_a_full_proof_audit(self):
        b=json.loads((ROOT/'data/figures/BUILD_RECORD.json').read_text())
        self.assertFalse(b['new_theorem_or_global_certificate_audit'])
        self.assertFalse(b['figures_rendered']);self.assertFalse(b['repository_changes'])

if __name__=='__main__':unittest.main()
