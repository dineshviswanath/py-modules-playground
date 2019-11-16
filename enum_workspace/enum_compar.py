import enum

class VoucherStatus(enum.Enum):

    issued = 1
    cancelled = 4
    archived = 3
    consumed = 2
    expired = 5

expected = VoucherStatus.issued
actual = VoucherStatus.cancelled

print('{} by {}'.format(expected == actual, 'Equality'))
print('{} by {}'.format(expected is actual, 'Identity'))

print('Sort')

# TypeError: '<' not supported between instances of 'VoucherStatus' and 'VoucherStatus'
sorted(VoucherStatus)