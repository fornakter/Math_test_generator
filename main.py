import random
from fpdf import FPDF
import os

try:
    a = int(input("Enter the first value: "))
    b = int(input("Second one: "))
    tasks = int(input("How many tasks: "))
except:
    print('Value error')
    quit()

math_action = input('Action: ')

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('helvetica', '', 16)


for i in range(tasks):
    pdf.cell(100, 10, f'{random.randrange(a, b)} {math_action} {random.randrange(a, b)} = __')
    pdf.cell(100, 10, f'{random.randrange(a, b)} {math_action} {random.randrange(a, b)} = __', new_x="LMARGIN", new_y="NEXT")
pdf.output('1.pdf')
print('File ready')
my_file = open('1.pdf', 'r')
os.startfile(my_file, 'print')
os.startfile(my_file, 'print')