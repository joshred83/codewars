"""In this kata, you will write a function that returns the positions
and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3
with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks.
Both of these properties should be arrays. If there is no peak in the given
array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return
{pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be
empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks
(in the context of a mathematical function, we don't know what is after
and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3]
does not. In case of a plateau-peak, please only return the position and value
of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1])
returns {pos: [1], peaks: [2]} (or equivalent in other languages)

Have fun!"""
from typing import List


def pick_peaks(arr):
    positions = []  # type: List[int]
    peaks_list = []
    position = None
    peak = None
    asc_or_desc = 'DESC'

    for i, p in enumerate(arr):
        if i == 0:
            continue
        if arr[i - 1] < arr[i]:
            position = i
            peak = p
            asc_or_desc = 'ASC'
        if arr[i - 1] > arr[i] and asc_or_desc != 'DESC':
            positions.append(position)
            peaks_list.append(peak)
            asc_or_desc = 'DESC'

    return {'pos': positions, 'peaks': peaks_list}


'''     0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9'''
nums = [7, 5, 3, 3, 5, 3, 6, 9, 9, 9, 9, 0, 2, 4, 5, 5, 6, 7, 8, 9]
print(nums)
nums = pick_peaks([7, 5, 3, 3, 5, 3, 6, 9, 9, 9, 9, 0, 2, 4, 5, 5, 6, 7, 8, 9])

print(nums)
