from mrjob.job import MRJob

# Create a class called Bacon_count


class Bacon_count(MRJob):

    # create a mapper() function.

    def mapper(self, _, line):

# use the Python convention of an underscore to indicate that won’t use this param.
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1

# call reducer function
    def reducer(self, key, values):
        yield key, sum(values)


# call function 

if __name__ == "__main__":
   Bacon_count.run()