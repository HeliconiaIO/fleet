# Copyright 2021 - TODAY, Marcel Savegnago
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo.tests.common import TransactionCase


class TestFleetVehicleFuelCapacity(TransactionCase):
    def setUp(self):
        """Set up initial data for the test cases."""
        super().setUp()

        # Create a vehicle model (you can use a valid brand ID or mock it)
        self.vehicle_model = self.env["fleet.vehicle.model"].create(
            {
                "name": "Model Name",
                "brand_id": 1,  # Assuming brand_id 1 exists
            }
        )

    def test_valid_fuel_capacity(self):
        """Test if a vehicle can be created with a valid fuel capacity."""
        vehicle = self.env["fleet.vehicle"].create(
            {
                "model_id": self.vehicle_model.id,
                "fuel_capacity": 50.0,  # Valid fuel capacity
            }
        )

        self.assertEqual(
            vehicle.fuel_capacity, 50.0, "The fuel capacity should be 50.0 liters."
        )
