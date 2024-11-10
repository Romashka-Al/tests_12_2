import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r1 = Runner('Усэйн', speed=10)
        self.r2 = Runner('Андрей', speed=9)
        self.r3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results:
            print({place: str(runner) for place, runner in res.items()})

    def test1(self):
        tournament = Tournament(90, *[self.r1, self.r3])
        self.all_results.append(tournament.start())
        self.assertEqual(self.all_results[0][2], 'Ник')

    def test2(self):
        tournament = Tournament(90, *[self.r2, self.r3])
        self.all_results.append(tournament.start())
        self.assertEqual(self.all_results[1][2], 'Ник')

    def test3(self):
        tournament = Tournament(90, *[self.r1, self.r2, self.r3])
        self.all_results.append(tournament.start())
        self.assertEqual(self.all_results[2][3], 'Ник')


if __name__ == '__main__':
    unittest.main()
