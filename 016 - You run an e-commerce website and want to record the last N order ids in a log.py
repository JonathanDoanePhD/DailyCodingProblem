# Good morning! Here's your coding interview problem for today.

# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

order_log = list(range(1000))

def record(in_id, in_order_log=order_log):
    return in_order_log + [in_id]

def get_last(in_i=1, in_order_log=order_log):
    return in_order_log[-in_i]

def ANS(in_ids, in_order_log=order_log):
    return in_order_log + in_ids

print(get_last(4, ANS([1, 22, 333, 4444, 55555])))