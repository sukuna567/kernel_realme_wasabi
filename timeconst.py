import sys, math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fmul(b, n, d):
    return ((1 << b) * n + d - 1) // d

def fadj(b, n, d):
    d = d // gcd(n, d)
    return ((1 << b) * (d - 1)) // d

def fmuls(b, n, d):
    for s in range(64):
        m = fmul(s, n, d)
        if m >= (1 << (b - 1)):
            return s
    return 0

hz = int(sys.stdin.read().strip())
print(f"/* Automatically generated */\n#ifndef KERNEL_TIMECONST_H\n#define KERNEL_TIMECONST_H\n\n#include <linux/param.h>\n#include <linux/types.h>\n\n#if HZ != {hz}\n#error \"include/generated/timeconst.h has the wrong HZ value!\"\n#endif\n")

s = fmuls(32, 1000, hz)
print(f"#define HZ_TO_MSEC_MUL32\tU64_C(0x{fmul(s, 1000, hz):X})")
print(f"#define HZ_TO_MSEC_ADJ32\tU64_C(0x{fadj(s, 1000, hz):X})")
print(f"#define HZ_TO_MSEC_SHR32\t{s}")

s = fmuls(32, hz, 1000)
print(f"#define MSEC_TO_HZ_MUL32\tU64_C(0x{fmul(s, hz, 1000):X})")
print(f"#define MSEC_TO_HZ_ADJ32\tU64_C(0x{fadj(s, hz, 1000):X})")
print(f"#define MSEC_TO_HZ_SHR32\t{s}")

cd = gcd(hz, 1000)
print(f"#define HZ_TO_MSEC_NUM\t\t{1000//cd}")
print(f"#define HZ_TO_MSEC_DEN\t\t{hz//cd}")
print(f"#define MSEC_TO_HZ_NUM\t\t{hz//cd}")
print(f"#define MSEC_TO_HZ_DEN\t\t{1000//cd}\n")

s = fmuls(32, 1000000, hz)
print(f"#define HZ_TO_USEC_MUL32\tU64_C(0x{fmul(s, 1000000, hz):X})")
print(f"#define HZ_TO_USEC_ADJ32\tU64_C(0x{fadj(s, 1000000, hz):X})")
print(f"#define HZ_TO_USEC_SHR32\t{s}")

s = fmuls(32, hz, 1000000)
print(f"#define USEC_TO_HZ_MUL32\tU64_C(0x{fmul(s, hz, 1000000):X})")
print(f"#define USEC_TO_HZ_ADJ32\tU64_C(0x{fadj(s, hz, 1000000):X})")
print(f"#define USEC_TO_HZ_SHR32\t{s}")

cd = gcd(hz, 1000000)
print(f"#define HZ_TO_USEC_NUM\t\t{1000000//cd}")
print(f"#define HZ_TO_USEC_DEN\t\t{hz//cd}")
print(f"#define USEC_TO_HZ_NUM\t\t{hz//cd}")
print(f"#define USEC_TO_HZ_DEN\t\t{1000000//cd}")

cd = gcd(hz, 1000000000)
print(f"#define HZ_TO_NSEC_NUM\t\t{1000000000//cd}")
print(f"#define HZ_TO_NSEC_DEN\t\t{hz//cd}")
print(f"#define NSEC_TO_HZ_NUM\t\t{hz//cd}")
print(f"#define NSEC_TO_HZ_DEN\t\t{1000000000//cd}\n")
print("#endif /* KERNEL_TIMECONST_H */")
