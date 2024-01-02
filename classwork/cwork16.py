
values = [12, 20, 32, 43, 49]

def compute_avg(values):
  return sum(values) / len(values)

print(compute_avg(values))
def compute_greatest(values):
    values.sort()
    return values[-1]

print(compute_greatest([10, 20, 5, 4, 9, 30, 8, 7, 17]))
print(compute_greatest([9, 6, 15, 41, 90, 31, 82, 47, 0]))