import unittest
from yummy_app import YummyApp
import gps_service

# ======================================================================
# CAP DO 1: Bo test co ban cho san (Moi chi dat 35% Coverage)
# ======================================================================
class TestEasyLevel(unittest.TestCase):
    """Kiem thu chuc nang co ban tinh tien don hang"""
    
    def setUp(self):
        self.app = YummyApp()

    def test_calculate_total_for_single_item(self):
        cart = {"pho": 2}
        self.assertEqual(self.app.calculate_order_total(cart), 100000)

    def test_calculate_total_for_multiple_items(self):
        cart = {"pho": 1, "bun": 1}
        self.assertEqual(self.app.calculate_order_total(cart), 95000)

    def test_calculate_total_for_empty_cart(self):
        self.assertEqual(self.app.calculate_order_total({}), 0.0)

    def test_calculate_total_with_zero_quantity(self):
        cart = {"pho": 0}
        self.assertEqual(self.app.calculate_order_total(cart), 0.0)

# ======================================================================
# CAP DO 2 (TIET 3): SINH VIEN TU TAY LAP TRINH TEST CASE DUOI DAY
# (Sau khi da hoan thanh Ban thiet ke test case viet tay tren giay)
# ======================================================================
# Sinh vien tu viet class TestMediumLevel o day (4 test case cho apply_promo_code)
class TestMediumLevel(unittest.TestCase):

    def test_apply_promo_valid_promo(self):
        app = YummyApp(network_status="online", os_version=15)
        total = 200000
        discounted_total = app.apply_promo_code(total, "GIAM10")
        self.assertEqual(discounted_total, 180000)

    def test_apply_promo_offline_raises_error(self):
        app = YummyApp(network_status="offline", os_version=15)
        total = 200000.0
        with self.assertRaises(ConnectionError):
            app.apply_promo_code(total, "GIAM10")

    def test_apply_promo_special_code_os_15(self):
        app = YummyApp(network_status="online", os_version=15)
        result = app.apply_promo_code(100000.0, "NEW_OS_ONLY")
        self.assertEqual(result, 80000.0)

    def test_apply_promo_special_code_os_14(self):
        app = YummyApp(network_status="online", os_version=14)
        with self.assertRaises(ValueError):
            app.apply_promo_code(100000.0, "NEW_OS_ONLY")


# Sinh vien tu viet class TestHardLevel o day (@patch cho get_nearby_restaurants)

if __name__ == '__main__':
    unittest.main()