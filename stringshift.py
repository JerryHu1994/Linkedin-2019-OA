def stringshift(str, left, right):
    shift = right - left
    l, r = False, False
    if shift > 0:   shiftright = True
    shift = abs(shift)%len(str)
    if shiftright:
        return str[-shift:] + str[:len(str)-shift]
    else:
        return str[shift+1:] + str[:shift]