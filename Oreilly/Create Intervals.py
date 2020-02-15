"""
From a set of ints you have to create a list of closed intervals as tuples, so the intervals are covering all the values found in the set.

A closed interval includes its endpoints! The interval 1..5, for example, includes each value x that satifies the condition 1 <= x <= 5.

Values can only be in the same interval if the difference between a value and the next smaller value in the set equals one, otherwise 
a new interval begins. Of course, the start value of an interval is excluded from this rule.
A single value, that does not fit into an existing interval becomes the start- and endpoint of a new interval.
"""

def create_intervals(data):
    sort = sorted(data)
    response, b, e = [], 0, 0
    if(len(sort)>0):
        for i in range(1, len(sort)):
            if (sort[i] - sort[e]) > 1:
                response.append(tuple([sort[b], sort[e]]))
                b = i
            e = i
        if((sort[b], sort[e]) not in response):
            response.append(tuple([sort[b], sort[e]]))
    return response

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')