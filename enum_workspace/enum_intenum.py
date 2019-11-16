import enum

class VoucherStatus(enum.IntEnum):

    issued = 1
    cancelled = 4
    archived = 3
    consumed = 2
    expired = 5

print('sorting by IntEnum')
print('\n'.join(s.name for s in sorted(VoucherStatus)))

# sorting by IntEnum
# issued
# consumed
# archived
# cancelled
# expired