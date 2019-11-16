import enum

VoucherStatus = enum.Enum(
    value = 'VoucherStatus',
    names = ('issued consumed archived cancelled expired'),
)

for s in VoucherStatus:
    print('{} with {}'.format(
        s.name,
        s.value,
    ))