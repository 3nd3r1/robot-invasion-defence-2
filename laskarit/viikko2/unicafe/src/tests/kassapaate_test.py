import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):

    def setUp(self) -> None:
        self.kassapaate = Kassapaate()

    def test_luodun_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_osto_kateisella_toimii_jos_maksu_on_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_osto_kateisella_ei_toimi_jos_maksu_ei_ole_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaan_lounaan_osto_kateisella_toimii_jos_maksu_on_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_osto_kateisella_ei_toimi_jos_maksu_ei_ole_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_osto_kortilla_toimii_jos_saldo_on_riittava(self):
        kortti = Maksukortti(500)
        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_osto_kortilla_ei_toimi_jos_saldo_ei_ole_riittava(self):
        kortti = Maksukortti(200)
        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaa_lounaan_osto_kortilla_toimii_jos_saldo_on_riittava(self):
        kortti = Maksukortti(500)
        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_osto_kortilla_ei_toimi_jos_saldo_ei_ole_riittava(self):
        kortti = Maksukortti(200)
        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortille_rahaa_ladattaessa_saldo_muuttuu_ja_kassan_raha_kasvaa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
        self.assertEqual(kortti.saldo, 500)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 0)
