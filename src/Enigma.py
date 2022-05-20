# Historical Rotors and Reflectors
util = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

one = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}
one_util = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
one_rev = {}
one_step = util.index("R")

two = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}
two_util = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
two_rev = {}
two_step = util.index("F")

three = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}
three_util = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
three_rev = {}
three_step = util.index("W")

four = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}
four_util = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
four_rev = {}
four_step = util.index("K")

five = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}
five_util = "VZBRGITYUPSDNHLXAWMJQOFECK"
five_rev = {}
five_step = util.index("A")

ref_a = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}
ref_a_util = "EJMZALYXVBWFCRQUONTSPIKHGD"

ref_b = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}
ref_b_util = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

ref_c = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "", "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "", "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": ""}
ref_c_util = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

plugboard = {}

rotor_ref = {"i": one, "ii": two, "iii": three, "iv": four, "v": five}
rotor_rev_ref = {"i": one_rev, "ii": two_rev, "iii": three_rev, "iv": four_rev, "v": five_rev}
ref_ref = {"a": ref_a, "b": ref_b, "c": ref_c}

step_ref = {"i": one_step, "ii": two_step, "iii": three_step, "iv": four_step, "v": five_step}

def init():
    global one, two, three, four, five, one_rev, two_rev, three_rev, four_rev, five_rev, rotor_ref, ref_ref, rotor_rev_ref
    tmp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, len(tmp)):
        one[tmp[i]] = one_util[i]
        two[tmp[i]] = two_util[i]
        three[tmp[i]] = three_util[i]
        four[tmp[i]] = four_util[i]
        five[tmp[i]] = five_util[i]
        ref_a[tmp[i]] = ref_a_util[i]
        ref_b[tmp[i]] = ref_b_util[i]
        ref_c[tmp[i]] = ref_c_util[i]
    one_rev = {value: key for key, value in one.items()}
    two_rev = {value: key for key, value in two.items()}
    three_rev = {value: key for key, value in three.items()}
    four_rev = {value: key for key, value in four.items()}
    five_rev = {value: key for key, value in five.items()}
    rotor_ref = {"i": one, "ii": two, "iii": three, "iv": four, "v": five}
    rotor_rev_ref = {"i": one_rev, "ii": two_rev, "iii": three_rev, "iv": four_rev, "v": five_rev}
    ref_ref = {"a": ref_a, "b": ref_b, "c": ref_c}

def rot(rotor):
    global one, two, three, four, five, one_rev, two_rev, three_rev, four_rev, five_rev, rotor_ref, ref_ref, rotor_rev_ref
    if rotor == "i":
        tmp = one["A"]
        for i in util:
            if i == "Z":
                one["Z"] = tmp
            else:
                one[i] = one[util[util.index(i)+1]]
    elif rotor == "ii":
        tmp = two["A"]
        for i in util:
            if i == "Z":
                two["Z"] = tmp
            else:
                two[i] = two[util[util.index(i)+1]]
    elif rotor == "iii":
        tmp = three["A"]
        for i in util:
            if i == "Z":
                three["Z"] = tmp
            else:
                three[i] = three[util[util.index(i)+1]]
    elif rotor == "iv":
        tmp = four["A"]
        for i in util:
            if i == "Z":
                four["Z"] = tmp
            else:
                four[i] = four[util[util.index(i)+1]]
    elif rotor == "v":
        tmp = five["A"]
        for i in util:
            if i == "Z":
                five["Z"] = tmp
            else:
                five[i] = five[util[util.index(i)+1]]
    one_rev = {value: key for key, value in one.items()}
    two_rev = {value: key for key, value in two.items()}
    three_rev = {value: key for key, value in three.items()}
    four_rev = {value: key for key, value in four.items()}
    five_rev = {value: key for key, value in five.items()}
    rotor_ref = {"i": one, "ii": two, "iii": three, "iv": four, "v": five}
    rotor_rev_ref = {"i": one_rev, "ii": two_rev, "iii": three_rev, "iv": four_rev, "v": five_rev}
    ref_ref = {"a": ref_a, "b": ref_b, "c": ref_c}

def encrypt():
    global plugboard
    plain = input("Enter your message (only letters): ")
    plain = plain.upper()

    cipher = ""

    layout = [0, 0, 0] # AAA

    fast = input("Enter roman numeral for fast rotor (i, ii, iii, iv, v): ").strip()
    medium = input("Enter roman numeral for medium rotor (i, ii, iii, iv, v): ").strip()
    slow = input("Enter roman numeral for slow rotor (i, ii, iii, iv, v): ").strip()
    reflector = input("Enter letter for reflector (a, b, c): ").strip()
    
    counter = 0
    letters = list(util)
    while counter < 10:
        c = input("Enter a letter followed by a space and another (eg. \"A B\" to map a to b for the plugboard) or \"exit\" to quit (any unused letters will be defaulted to no connection): ")
        if c == "exit":
            break
        elif c.split(" ")[0] == c.split(" ")[1]:
            exit()
        elif not c.split(" ")[0] in letters or not c.split(" ")[1] in letters:
            exit()
        else:
            plugboard[c.split(" ")[0]] = c.split(" ")[1]
            plugboard[c.split(" ")[1]] = c.split(" ")[0]
            letters.remove(c.split(" ")[0])
            letters.remove(c.split(" ")[1])
        counter+=1
    if fast == medium or medium == slow or slow == fast:
        exit()

    lay = input("Enter starting rotor layout (AAA, AAB, etc.), or leave blank for AAA: ")
    if len(lay) == 0:
        pass
    elif len(lay) == 3:
        for i in range(0, 3):
            layout[i] = util.index(lay[i])
            if i == 0:
                for _ in range(0, util.index(lay[i])):
                    rot(slow)
            elif i == 1:
                for _ in range(0, util.index(lay[i])):
                    rot(medium)
            elif i == 2:
                for _ in range(0, util.index(lay[i])):
                    rot(fast)
    else:
        exit()
    if layout[2] == step_ref[fast]:
        rot(medium)
        layout[1] = (layout[1] + 1) % 26
    if layout[1] == step_ref[medium]:
        rot(slow)
        layout[0] = (layout[0] + 1) % 26

    for letter in plain:
        if letter == " ":
            cipher += " "
            continue
        curr = letter if letter not in plugboard else plugboard[letter]
        tmp = rotor_rev_ref[fast][rotor_rev_ref[medium][rotor_rev_ref[slow][ref_ref[reflector][rotor_ref[slow][rotor_ref[medium][rotor_ref[fast][curr]]]]]]]
        cipher += tmp if tmp not in plugboard else plugboard[tmp]
        rot(fast)
        layout[2] = (layout[2] + 1) % 26
        if layout[2] == step_ref[fast]:
            rot(medium)
            layout[1] = (layout[1] + 1) % 26
        if layout[1] == step_ref[medium]:
            rot(slow)
            layout[0] = (layout[0] + 1) % 26
    print("Ciphertext: " + cipher)

def decrypt():
    global plugboard
    plain = input("Enter ciphertext: ")
    plain = plain.upper()

    cipher = ""

    layout = [0, 0, 0] # AAA

    fast = input("Enter roman numeral for fast rotor (i, ii, iii, iv, v): ").strip()
    medium = input("Enter roman numeral for medium rotor (i, ii, iii, iv, v): ").strip()
    slow = input("Enter roman numeral for slow rotor (i, ii, iii, iv, v): ").strip()
    reflector = input("Enter letter for reflector (a, b, c): ").strip()
    
    counter = 0
    letters = list(util)
    while counter < 10:
        c = input("Enter a letter followed by a space and another (eg. \"A B\" to map a to b for the plugboard) or \"exit\" to quit (any unused letters will be defaulted to no connection): ")
        if c == "exit":
            break
        elif c.split(" ")[0] == c.split(" ")[1]:
            exit()
        elif not c.split(" ")[0] in letters or not c.split(" ")[1] in letters:
            exit()
        else:
            plugboard[c.split(" ")[0]] = c.split(" ")[1]
            plugboard[c.split(" ")[1]] = c.split(" ")[0]
            letters.remove(c.split(" ")[0])
            letters.remove(c.split(" ")[1])
        counter+=1
    if fast == medium or medium == slow or slow == fast:
        exit()

    lay = input("Enter starting rotor layout (AAA, AAB, etc.), or leave blank for AAA: ")
    if len(lay) == 0:
        pass
    elif len(lay) == 3:
        for i in range(0, 3):
            layout[i] = util.index(lay[i])
            if i == 0:
                for _ in range(0, util.index(lay[i])):
                    rot(slow)
            elif i == 1:
                for _ in range(0, util.index(lay[i])):
                    rot(medium)
            elif i == 2:
                for _ in range(0, util.index(lay[i])):
                    rot(fast)
    else:
        exit()
    if layout[2] == step_ref[fast]:
        rot(medium)
        layout[1] = (layout[1] + 1) % 26
    if layout[1] == step_ref[medium]:
        rot(slow)
        layout[0] = (layout[0] + 1) % 26

    for letter in plain:
        if letter == " ":
            cipher += " "
            continue
        curr = letter if letter not in plugboard else plugboard[letter]
        tmp = rotor_rev_ref[fast][rotor_rev_ref[medium][rotor_rev_ref[slow][ref_ref[reflector][rotor_ref[slow][rotor_ref[medium][rotor_ref[fast][curr]]]]]]]
        cipher += tmp if tmp not in plugboard else plugboard[tmp]
        rot(fast)
        layout[2] = (layout[2] + 1) % 26
        if layout[2] == step_ref[fast]:
            rot(medium)
            layout[1] = (layout[1] + 1) % 26
        if layout[1] == step_ref[medium]:
            rot(slow)
            layout[0] = (layout[0] + 1) % 26
    print("Plaintext: " + cipher)

def main():
    init()
    choice = input("Encrypt (a) or decrypt (b): ")
    if choice == "a":
        encrypt()
    elif choice == "b":
        decrypt()
    else:
        exit()
    



if __name__ == "__main__":
    main()