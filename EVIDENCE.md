# Booking Lab Evidence Record

**Name:** Siriphanaphon
**Student ID:** 6680085
**Repository:** https://github.com/blimmy/iccs471-booking-lab-Siriphanaphon-Sir.git

## Goal
I needed to reject a new booking if its time overlaps another booking in the same room. The program should raise ValueError and should not save the new booking.

## Constraints / Out of Scope
- change only booking_app/booking.py and tests/test_booking.py. 
- The old input checks, create/list functions, and four original tests had to stay. Bookings could still be next to each other, and different rooms could have bookings at the same time. Room names had to match exactly. demo.py could not be changed.

## Key Decision and Agent Claim
I asked Copilot to keep demo.py unchanged but use it to check the result. I accepted its choice to check for an overlap before saving a booking. 

Copilot said only the two files changed. The recorded git diff and git status checks supported this claim.

## Verification: Claim → Evidence
- **Claim:** Same-room overlaps are rejected. Bookings next to each other and bookings in different rooms are allowed.
- **Command or test I ran:** uv run python -m unittest discover -s tests -v
- **Actual result:** All 9 tests passed, including the four original tests.
- **What this supports:** The tested booking rules work, and the original tests still pass.

## Manual Validation
The recorded run of uv run python demo.py shows that it reject a same-room overlap and showed Stored bookings: 3. 

## Remaining Uncertainty
I did not test many people trying to book the same room at the same time
I did not test how the program works with very large time numbers.