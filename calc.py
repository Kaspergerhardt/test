"""Basic calculation"""

def subtract(left_hand, right_hand):
    """Substract function"""
    return left_hand - right_hand


def add(left_hand, right_hand):
    """Add function"""
    return left_hand + right_hand

if __name__ == "__main__":
    print(f"1 + 3 = {add(1, 3)}")
    print(f"4 - 1 = { subtract(4, 1)}")
