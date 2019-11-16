import enum

VoucherStatus = enum.Enum(
    value = 'VoucherStatus',
    names = [
        ('issued', 10),
        ('consumed', 20),
        ('archived', 30),
        ('cancelled', 40),
        ('expired', 50)
    ],
)

for s in VoucherStatus:
    print('{} with {}'.format(
        s.name,
        s.value,
    ))