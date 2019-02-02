def print_colorful_text(string, style, foreground, background):
    format = ';;'.join([str(style), str(foreground), str(background)])
    print('\x1b[%sm %s \x1b[0m' % (format, string), end="")

print_colorful_text("R", 5, 35, 45)
print_colorful_text("A", 6, 36, 46)
print_colorful_text("I", 7, 37, 43)
print_colorful_text("N", 8, 38, 42)
print_colorful_text("B", 1, 30, 43)
print_colorful_text("O", 2, 31, 44)
print_colorful_text("W", 3, 32, 42)
