import enum


class VoucherStatus(enum.Enum):
    issued = (
        1, [
            'consumed',
            'cancelled',
            'expired',
        ]
    )

    consumed = (
        2, [
            'archived',
        ]
    )

    expired = (
        3, [
            'archived',
        ]
    )

    def __init__(self, num, transitions):
        self.num = num
        self.possible_values = transitions

    def can_transition(self, new_state):
        return new_state in self.possible_values

print(VoucherStatus.issued.value)
print(VoucherStatus.issued.possible_values)
print(VoucherStatus.consumed.can_transition(VoucherStatus.issued))
