import unittest

class Athlete:
    def __init__(self, athlete_id, name, sport):
        self.athlete_id = athlete_id
        self.name = name
        self.sport = sport

class MediaSchedule:
    def __init__(self, schedule_id, athlete_id, date, media_outlet):
        self.schedule_id = schedule_id
        self.athlete_id = athlete_id
        self.date = date
        self.media_outlet = media_outlet

class Scheduler:
    def __init__(self):
        self.schedules = []
        self.athletes = []

    def create_media_schedule(self, schedule_id, athlete_id, date, media_outlet):
        self.schedules.append(MediaSchedule(schedule_id, athlete_id, date, media_outlet))

    def read_media_schedule(self, schedule_id):
        for schedule in self.schedules:
            if schedule.schedule_id == schedule_id:
                return schedule
        raise ValueError("Schedule ID not found")

    def update_media_schedule(self, schedule_id, updated_data):
        for schedule in self.schedules:
            if schedule.schedule_id == schedule_id:
                schedule.date = updated_data.get('date', schedule.date)
                schedule.media_outlet = updated_data.get('media_outlet', schedule.media_outlet)
                break

    def delete_media_schedule(self, schedule_id):
        self.schedules = [schedule for schedule in self.schedules if schedule.schedule_id != schedule_id]

    def organize_media_appearances(self, athlete_id):
        athlete_schedules = []
        for schedule in self.schedules:
            if schedule.athlete_id == athlete_id:
                athlete_schedules.append(schedule)
        if not athlete_schedules:
            return "No media appearances found for this athlete."
        return athlete_schedules

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()
        self.scheduler.create_media_schedule(1, 1, "2024-05-01", "dd")
        self.scheduler.create_media_schedule(2, 2, "2024-05-02", "star sports")
        self.scheduler.create_media_schedule(3, 3, "2024-05-03", "sports +")
        self.scheduler.athletes.append(Athlete(1, "aaaa", "Football"))
        self.scheduler.athletes.append(Athlete(2, "bbbb", "cricket"))
        self.scheduler.athletes.append(Athlete(3, "cccc", "volliball"))

    def test_create_media_schedule(self):
        self.assertEqual(len(self.scheduler.schedules), 3)
        print("\nMedia Schedules:")
        for schedule in self.scheduler.schedules:
            print(f"Schedule ID: {schedule.schedule_id}, Athlete ID: {schedule.athlete_id}, Date: {schedule.date}, Media Outlet: {schedule.media_outlet}")

    def test_read_media_schedule(self):
        schedule = self.scheduler.read_media_schedule(1)
        self.assertEqual(schedule.date, "2024-05-01")
        print("\nRead Media Schedule:")
        print(f"Schedule ID: {schedule.schedule_id}, Athlete ID: {schedule.athlete_id}, Date: {schedule.date}, Media Outlet: {schedule.media_outlet}")

    def test_update_media_schedule(self):
        self.scheduler.update_media_schedule(2, {'date': "2024-05-05"})
        schedule = self.scheduler.read_media_schedule(2)
        self.assertEqual(schedule.date, "2024-05-05")
        print("\nUpdated Media Schedule:")
        print(f"Schedule ID: {schedule.schedule_id}, Athlete ID: {schedule.athlete_id}, Date: {schedule.date}, Media Outlet: {schedule.media_outlet}")

    def test_delete_media_schedule(self):
        self.scheduler.delete_media_schedule(1)
        self.assertEqual(len(self.scheduler.schedules), 2)
        print("\nRemaining Media Schedules:")
        for schedule in self.scheduler.schedules:
            print(f"Schedule ID: {schedule.schedule_id}, Athlete ID: {schedule.athlete_id}, Date: {schedule.date}, Media Outlet: {schedule.media_outlet}")

    def test_organize_media_appearances(self):
        athlete_id = 2
        athlete_media_appearances = self.scheduler.organize_media_appearances(athlete_id)
        if isinstance(athlete_media_appearances, list):
            print(f"\nMedia Appearances for Athlete ID {athlete_id}:")
            for appearance in athlete_media_appearances:
                print(f"Schedule ID: {appearance.schedule_id}, Date: {appearance.date}, Media Outlet: {appearance.media_outlet}")
        else:
            print(athlete_media_appearances)

if __name__== '__main__':
    unittest.main(verbosity=0,exit=False)
