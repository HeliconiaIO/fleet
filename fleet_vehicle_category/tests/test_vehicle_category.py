# Copyright 2020 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://odoo.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import TransactionCase


class TestFleetVehicleCategory(TransactionCase):
    def setUp(self):
        """Set up initial data for the test cases."""
        super().setUp()

        self.category = self.env["fleet.vehicle.category"].create(
            {
                "name": "Ambulance",
                "description": "<p>Emergency medical vehicle</p>",
            }
        )

        vehicle_model = self.env["fleet.vehicle.model"].create(
            {
                "name": "Model Name",
                "brand_id": 1,
            }
        )

        self.vehicle = self.env["fleet.vehicle"].create(
            {
                "model_id": vehicle_model.id,
                "vehicle_category_id": self.category.id,
            }
        )

    def test_vehicle_category_creation(self):
        """Test that a vehicle category can be created successfully."""
        category = self.env["fleet.vehicle.category"].search(
            [("name", "=", "Ambulance")]
        )
        self.assertTrue(
            category, "Vehicle category 'Ambulance' was not created correctly."
        )
        self.assertEqual(
            category.name, "Ambulance", "Vehicle category name is incorrect."
        )
        self.assertEqual(
            category.description,
            "<p>Emergency medical vehicle</p>",
            "Vehicle category description is incorrect.",
        )

    def test_fleet_vehicle_category_link(self):
        """Test that a fleet vehicle is correctly linked to a vehicle category."""
        vehicle = self.vehicle
        self.assertEqual(
            vehicle.vehicle_category_id.id,
            self.category.id,
            "Fleet vehicle category is not set correctly.",
        )
        self.assertEqual(
            vehicle.vehicle_category_id.name,
            "Ambulance",
            "Vehicle category name on fleet vehicle is incorrect.",
        )

    def test_vehicle_category_field_help(self):
        """Test the help text of the vehicle_category_id
        field in fleet.vehicle model."""
        field = self.env["fleet.vehicle"].fields_get(allfields=["vehicle_category_id"])[
            "vehicle_category_id"
        ]
        self.assertEqual(
            field["help"],
            "Eg. Tow truck, Ambulance, Trailer, Boat",
            "Help text for vehicle category field is incorrect.",
        )

    def test_vehicle_category_description_html(self):
        """Test that the description field is stored as HTML."""
        category = self.env["fleet.vehicle.category"].create(
            {
                "name": "Tow truck",
                "description": "<p>This is a tow truck</p>",
            }
        )
        self.assertIn(
            "<p>This is a tow truck</p>",
            category.description,
            "Vehicle category description is not stored correctly as HTML.",
        )
