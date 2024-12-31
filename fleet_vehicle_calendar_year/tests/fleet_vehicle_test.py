from odoo.tests.common import TransactionCase


class TestFleetVehicle(TransactionCase):
    def setUp(self):
        super().setUp()
        self.FleetVehicle = self.env["fleet.vehicle"]
        self.vehicle = self.FleetVehicle.create(
            {
                "name": "Test Vehicle",
                "license_plate": "TEST123",
                "model_id": self.env["fleet.vehicle.model"]
                .create({"name": "Test Model"})
                .id,
                "calendar_year": "2024",
            }
        )

    def test_calendar_year_field(self):
        """Test the calendar_year field functionality."""
        # Check initial value
        self.assertEqual(
            self.vehicle.calendar_year, "2024", "Calendar year should be '2024'"
        )

        # Update calendar_year
        self.vehicle.calendar_year = "2025"
        self.assertEqual(
            self.vehicle.calendar_year,
            "2025",
            "Calendar year should be updated to '2025'",
        )

    def test_tracking(self):
        """Test if changes in the calendar_year field are tracked in the chatter."""
        message_count_before = len(self.vehicle.message_ids)

        # Modify the calendar_year
        self.vehicle.calendar_year = "2026"

        message_count_after = len(self.vehicle.message_ids)
        self.assertGreater(
            message_count_after,
            message_count_before,
            "The calendar_year change should create a new message in the chatter",
        )
