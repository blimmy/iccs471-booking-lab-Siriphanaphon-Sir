import unittest

from booking_app.booking import BookingService


class BookingServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = BookingService()

    def test_create_and_list_booking(self) -> None:
        created = self.service.create_booking("A", 540, 600, "Narin")
        self.assertEqual(created.room, "A")
        self.assertEqual(created.guest, "Narin")
        self.assertEqual(self.service.list_bookings(), (created,))

    def test_bookings_remain_in_creation_order(self) -> None:
        first = self.service.create_booking("A", 540, 600, "Narin")
        second = self.service.create_booking("B", 600, 660, "Mali")
        self.assertEqual(self.service.list_bookings(), (first, second))

    def test_rejects_blank_room_or_guest(self) -> None:
        with self.assertRaises(ValueError):
            self.service.create_booking("  ", 540, 600, "Narin")
        with self.assertRaises(ValueError):
            self.service.create_booking("A", 540, 600, "  ")
        self.assertEqual(self.service.list_bookings(), ())

    def test_rejects_invalid_time_range(self) -> None:
        for start, end in ((600, 600), (660, 600), (-1, 60), (1380, 1441)):
            with self.subTest(start=start, end=end):
                with self.assertRaises(ValueError):
                    self.service.create_booking("A", start, end, "Narin")
        self.assertEqual(self.service.list_bookings(), ())

    def test_rejects_same_room_overlap_without_storing_it(self) -> None:
        original = self.service.create_booking("A", 540, 600, "Narin")

        with self.assertRaises(ValueError):
            self.service.create_booking("A", 570, 630, "Mali")

        self.assertEqual(self.service.list_bookings(), (original,))

    def test_rejects_contained_enclosing_and_identical_overlaps(self) -> None:
        cases = ((550, 590), (500, 650), (540, 600))

        for start, end in cases:
            with self.subTest(start=start, end=end):
                service = BookingService()
                original = service.create_booking("A", 540, 600, "Narin")

                with self.assertRaises(ValueError):
                    service.create_booking("A", start, end, "Mali")

                self.assertEqual(service.list_bookings(), (original,))

    def test_allows_adjacent_bookings(self) -> None:
        first = self.service.create_booking("A", 540, 600, "Narin")
        second = self.service.create_booking("A", 600, 660, "Mali")

        self.assertEqual(self.service.list_bookings(), (first, second))

        service = BookingService()
        later = service.create_booking("A", 600, 660, "Mali")
        earlier = service.create_booking("A", 540, 600, "Narin")

        self.assertEqual(service.list_bookings(), (later, earlier))

    def test_allows_overlapping_times_in_different_rooms(self) -> None:
        first = self.service.create_booking("A", 540, 600, "Narin")
        second = self.service.create_booking("B", 570, 630, "Mali")

        self.assertEqual(self.service.list_bookings(), (first, second))

    def test_matches_room_names_exactly(self) -> None:
        first = self.service.create_booking("A", 540, 600, "Narin")
        second = self.service.create_booking("a", 570, 630, "Mali")

        self.assertEqual(self.service.list_bookings(), (first, second))


if __name__ == "__main__":
    unittest.main()
