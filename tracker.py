"""
tracker.py

Defines the ApartmentTracker class: manages a LIST of Apartment objects.

apartment.py knows how to score ONE apartment.
tracker.py knows how to manage MANY apartments — add them, rank them,
filter them. Different responsibility, different file.
"""

from apartment import Apartment


class ApartmentTracker:
    def __init__(self):
        self.apartments = []

    def add_apartment(self, apartment):
        """Add an already-built Apartment object to the list."""
        self.apartments.append(apartment)

    def rank_apartments(self, max_rent=30000, max_commute=60, rent_weight=0.6, commute_weight=0.4):
        """
        Returns the list of apartments sorted by score, best first.
        rent_weight / commute_weight let the caller (the UI) control
        what matters more to THIS user — not a fixed default for everyone.
        Doesn't modify self.apartments — just returns a new sorted list.
        """
        return sorted(
            self.apartments,
            key=lambda apt: apt.score(
                max_rent=max_rent,
                max_commute=max_commute,
                rent_weight=rent_weight,
                commute_weight=commute_weight,
            ),
            reverse=True,  # highest score first
        )

    def filter_by_area(self, keyword):
        """
        Return apartments whose address contains the given keyword.
        Case-insensitive, partial match — e.g. "sector 45" matches
        "Sector 45, Gurgaon, Haryana". Empty keyword returns everything.
        """
        if not keyword:
            return self.apartments
        keyword = keyword.lower()
        return [apt for apt in self.apartments if keyword in apt.address.lower()]

    def filter_by_max_rent(self, max_rent):
        """Return only apartments at or under a given rent."""
        return [apt for apt in self.apartments if apt.rent <= max_rent]

    def filter_by_max_commute(self, max_commute):
        """Return only apartments at or under a given commute time (minutes)."""
        return [
            apt for apt in self.apartments
            if apt.commute_minutes is not None and apt.commute_minutes <= max_commute
        ]

    def filter_by_min_bedrooms(self, min_bedrooms):
        """Return only apartments with at least this many bedrooms."""
        return [apt for apt in self.apartments if apt.bedrooms >= min_bedrooms]

    def __len__(self):
        # Lets you write len(tracker) instead of len(tracker.apartments)
        return len(self.apartments)


# Quick manual test
if __name__ == "__main__":
    tracker = ApartmentTracker()

    tracker.add_apartment(Apartment("Maple Court 2B", "221 Maple St", 12000, 1, commute_minutes=12))
    tracker.add_apartment(Apartment("Birchwood Flats", "40 Birch Ave", 15500, 2, commute_minutes=15))
    tracker.add_apartment(Apartment("Riverside Studios", "9 River Rd", 9800, 1, commute_minutes=29))

    print(f"Tracking {len(tracker)} apartments\n")

    print("Ranked by score:")
    for apt in tracker.rank_apartments():
        print(f"  {apt.name}: score={apt.score()}")

    print("\nUnder ₹12000 rent:")
    for apt in tracker.filter_by_max_rent(12000):
        print(f"  {apt.name}")

    print("\nSearch 'maple':")
    for apt in tracker.filter_by_area("maple"):
        print(f"  {apt.name}")