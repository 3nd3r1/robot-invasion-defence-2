import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvataa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 35.00 euroa")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi_ja_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi_ja_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")
