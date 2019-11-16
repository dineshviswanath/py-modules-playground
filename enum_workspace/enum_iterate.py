import enum

class VoucherStatus(enum.Enum):

    issued = 1
    consumed = 2
    archived = 3
    cancelled = 4
    expired = 5

for status in VoucherStatus:
    print('{:15}->{}'.format(status.name, status.value))
