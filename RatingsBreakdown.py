from mrjob.job import MRJob
from mrjob.step impport MRStep

class RatingsBreakdown(MRJob):
    def steps(Self):
            return[
                MRStep(mapper=self.mapper_get_ratings,
                        reducer=self.reducer_count_ratings)

            ]

    def mapper_get_ratings(self, _ , line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yeild rating, 1

    def reducer_count_ratings(self, key, values):
        yeild key, sum(values)


if __name__ == '__main__':
    RatingsBreakdown.ren()
