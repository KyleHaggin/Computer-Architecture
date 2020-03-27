"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [None] * 256

        self.register = [0]*8
        pass

    def load(self, filepath):
        """Load a program into memory."""

        address = 0

        # Try/Except file loader
        try:
            with open(filepath, 'r') as f:

                # Create program
                program = f.read().splitlines()
                program = [
                    '0b'+line[:8]
                    for line in program
                    if line and line[0] in ['0', '1']
                    ]

                # Load program to ram
                for instruction in program:
                    self.ram[address] = eval(instruction)
                    address += 1

        except FileNotFoundError:
            print('File not found')
            sys.exit(2)

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001,  # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pc = 0
        running = True
        while running is True:

            # Breakout condition
            if self.ram[pc] is 0b00000001:
                # Increment pc by 1
                pc += 1

                # Breakout condition
                running = False

            # Resister Print
            elif self.ram[pc] is 0b01000111:
                # Increment pc by 1
                pc += 1

                # Set register index
                reg = self.ram[pc]
                # Print the register
                print(self.register[reg])
                # Increment pc by 1
                pc += 1

            elif self.ram[pc] is 0b10000010:
                # Increment pc by 1
                pc += 1

                # Set register index
                reg = self.ram[pc]
                # increment pc by 1
                pc += 1

                # Save value to register
                self.register[reg] = self.ram[pc]
                # Increment pc by 1
                pc += 1

            else:
                print(f'Unknown instruction: {self.ram[pc]}')
                sys.exit(1)
        pass
