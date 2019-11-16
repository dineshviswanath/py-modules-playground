import enum

class VoucherStatus(enum.Enum):

    issued = 1
    consumed = 2
    archived = 3
    cancelled = 4
    expired = 5

print(VoucherStatus.cancelled.name)
print(VoucherStatus.cancelled.value)
