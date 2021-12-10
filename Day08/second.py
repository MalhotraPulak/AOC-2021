import sys
import pprint


def get_output(inputs, outputs) -> int:
    maps = {}
    for s in inputs:
        maps.setdefault(len(s), []).append(s)
    pprint.pprint(maps)

    # check for the two and three len to determine what maps to a
    cf = maps[2][0]
    acf = maps[3][0]
    a = set(acf) - set(cf)
    print(f"{a} maps to a")
    bdcf = maps[4][0]
    bd = set(bdcf) - set(cf)
    print(f"{bd} maps to bd")
    fives = maps[5]
    adg = set(fives[0]).intersection(set(fives[1])).intersection(fives[2])
    print(f"{adg} maps to adg")
    dg = adg - set(a)
    print(f"{dg} maps to dg")
    d = bd.intersection(dg)
    print(f"{d} maps to d")
    g = dg - d
    print(f"{g} maps to g")
    b = bd - d
    print(f"{b} maps to b")
    sixes = maps[6]
    agbf = set(sixes[0]).intersection(set(sixes[1])).intersection(set(sixes[2]))
    f = agbf - (a.union(g).union(b))
    print(f"{f} maps to f")
    c = set(cf) - f
    print(f"{c} maps to c")
    e = set("abcdefg") - (a.union(b).union(c).union(d).union(f).union(g))
    print(f"{e} maps to e")

    a = a.pop()
    b = b.pop()
    c = c.pop()
    d = d.pop()
    e = e.pop()
    f = f.pop()
    g = g.pop()

    mapping = {
        a: "a",
        b: "b",
        c: "c",
        d: "d",
        e: "e",
        f: "f",
        g: "g",
    }
    value = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }
    ans = 0
    for s in outputs:
        new_s = ""
        for c in s:
            new_s += mapping[c]
        sorted_s = "".join(sorted(new_s))
        ans = ans * 10 + value[sorted_s]
    return ans


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    lines = [line.split("|") for line in lines]

    ans = 0
    for f, s in lines:
        outputs = s.strip().split()
        inputs = f.strip().split()
        ans += get_output(inputs, outputs)

    print(ans)


if __name__ == "__main__":
    main()
