"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 75
        self.register = [0] * 8
        self.pc = 0
        self.sp_index = 7
        self.equal_flag = 0

    def load(self):
        """Load a program into memory."""

        address = 0

        # # For now, we've just hardcoded a program:
        # Program for ADD and MUL
        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b10000010,  # LDI R1,9
        #     0b00000001,
        #     0b00001001,
        #     0b10100010,  # MUL R0,R1
        #     0b00000000,
        #     0b00000001,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00000001  # HLT
        # ]

        # Push and Pop Program
        # program = [
        #     # From stack.ls8
        #     0b10000010,  # LDI R0,1
        #     0b00000000,
        #     0b00000001,
        #     0b10000010,  # LDI R1,2
        #     0b00000001,
        #     0b00000010,
        #     0b01000101,  # PUSH R0
        #     0b00000000,
        #     0b01000101,  # PUSH R1
        #     0b00000001,
        #     0b10000010,  # LDI R0,3
        #     0b00000000,
        #     0b00000011,
        #     0b01000110,  # POP R0
        #     0b00000000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b10000010,  # LDI R0,4
        #     0b00000000,
        #     0b00000100,
        #     0b01000101,  # PUSH R0
        #     0b00000000,
        #     0b01000110,  # POP R2
        #     0b00000010,
        #     0b01000110,  # POP R1
        #     0b00000001,
        #     0b01000111,  # PRN R2
        #     0b00000010,
        #     0b01000111,  # PRN R1
        #     0b00000001,
        #     0b00000001,  # HLT
        # ]

        # program = [
        #     0b10000010,  # LDI R1,MULT2PRINT
        #     0b00000001,
        #     0b00011000,
        #     0b10000010, # LDI R0,10
        #     0b00000000,
        #     0b00001010,
        #     0b01010000,  # CALL R1
        #     0b00000001,
        #     0b10000010,  # LDI R0,15
        #     0b00000000,
        #     0b00001111,
        #     0b01010000,  # CALL R1
        #     0b00000001,
        #     0b10000010,  # LDI R0,18
        #     0b00000000,
        #     0b00010010,
        #     0b01010000,  # CALL R1
        #     0b00000001,
        #     0b10000010,  # LDI R0,30
        #     0b00000000,
        #     0b00011110,
        #     0b01010000,  # CALL R1
        #     0b00000001,
        #     0b00000001, # HLT
        #     # MUL2PRINT (address 24):
        #     0b10100000,  # ADD R0,R0
        #     0b00000000,
        #     0b00000000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b00010001,  # RET
        # ]

        program = [
            0b10000010,  # LDI R0,10
            0b00000000,
            0b00001010,
            0b10000010,  # LDI R1,20
            0b00000001,
            0b00010100,
            0b10000010,  # LDI R2,TEST1
            0b00000010,
            0b00010011,
            0b10100111,  # CMP R0,R1
            0b00000000,
            0b00000001,
            0b01010101,  # JEQ R2
            0b00000010,
            0b10000010,  # LDI R3,1
            0b00000011,
            0b00000001,
            0b01000111,  # PRN R3
            0b00000011,
            # TEST1 (address 19):
            0b10000010,  # LDI R2,TEST2
            0b00000010,
            0b00100000,
            0b10100111, # CMP R0,R1
            0b00000000,
            0b00000001,
            0b01010110,  # JNE R2
            0b00000010,
            0b10000010,  # LDI R3,2
            0b00000011,
            0b00000010,
            0b01000111,  # PRN R3
            0b00000011,
            # TEST2 (address 32):
            0b10000010,  # LDI R1,10
            0b00000001,
            0b00001010,
            0b10000010,  # LDI R2,TEST3
            0b00000010,
            0b00110000,
            0b10100111,  # CMP R0,R1
            0b00000000,
            0b00000001,
            0b01010101,  # JEQ R2
            0b00000010,
            0b10000010,  # LDI R3,3
            0b00000011,
            0b00000011,
            0b01000111,  # PRN R3
            0b00000011,
            # TEST3 (address 48):
            0b10000010,  # LDI R2,TEST4
            0b00000010,
            0b00111101,
            0b10100111,  # CMP R0,R1
            0b00000000,
            0b00000001,
            0b01010110,  # JNE R2
            0b00000010,
            0b10000010,  # LDI R3,4
            0b00000011,
            0b00000100,
            0b01000111, # PRN R3
            0b00000011,
            # TEST4 (address 61):
            0b10000010,  # LDI R3,5
            0b00000011,
            0b00000101,
            0b01000111,  # PRN R3
            0b00000011,
            0b10000010, # LDI R2,TEST5
            0b00000010,
            0b01001001,
            0b01010100,  # JMP R2
            0b00000010,
            0b01000111,  # PRN R3
            0b00000011,
            # TEST5 (address 73):
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

        # try:
        #     address = 0

        #     with open(sys.argv[1]) as f:
        #         for line in f:
        #         # Process comments:
        #         # Ignore anything after a # symbol
        #             comment_split = line.split("#")

        #         # Convert any numbers from binary strings to integers
        #             num = comment_split[0].strip()
        #             try:
        #                 val = int(num, 2)
        #             except ValueError:
        #                 continue

        #             self.ram[address] = val
        #             address += 1
        #         # print(f"{val:08b}: {val:d}")

        # except FileNotFoundError:
        #     print(f"{sys.argv[0]}: {sys.argv[1]} not found")
        #     sys.exit(2)

        # for x in range(len(self.ram)):
        #     print(self.ram[x])

        # for y in range(len(self.register)):
        #     print("register", self.register[y])
        print("LOAD RAM:", self.ram)
        print("LOAD REG:", self.register)

    def ram_read(self, memory_address):
        return self.ram[memory_address]

    def ram_write(self, memory_address, memory_data):
        self.ram[memory_address] = memory_data
        return self.ram[memory_address]

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "LDI":
            print("LDI: opA", reg_a, "opB", reg_b)
            # self.register[reg_a] += self.register[reg_b]
            self.register[reg_a] = reg_b
            # print("Register", self.register[reg_a])
            return self.register[reg_a]

        elif op == "MUL":
            print("MUL: opA", reg_a, "opB", reg_b)
            # self.register[reg_a] = self.register[reg_b]*self.register[reg_a]
            self.register[reg_a] *= self.register[reg_b]
            # print("Register at", self.register[reg_a])
            return self.register[reg_a]
        
        elif op == "CMP":
            print("CMP: opA", reg_a, "opB", reg_b)
            if self.register[reg_a] == self.register[reg_b]:
                self.equal_flag = 1
                return self.equal_flag
            else:
                self.equal_flag = 0
                return self.equal_flag
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
            print(" %02X" % self.register[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # Head tags for instructions
        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001
        MUL = 0b10100010
        PUSH = 0b01000101
        POP = 0b01000110
        CALL = 0b01010000
        RET = 0b00010001
        ADD = 0b10100000
        # Sprint Instructions
        CMP = 0b10100111

        running = True

        while running:
            IR = self.ram[self.pc]
            operand_a = self.ram[self.pc+1]
            operand_b = self.ram[self.pc+2]
            # print("MEMORY", IR)

            if IR == LDI:
                registered = self.alu("LDI", operand_a, operand_b)
                self.pc += 3
                print("LDI", registered)
                print(self.register)
                continue

            elif IR == MUL:
                multiplied = self.alu("MUL", operand_a, operand_b)
                self.pc += 3
                # print("multiply at index zero", self.register[0])
                print("MUL", multiplied)
                # print(self.register)
                continue

            elif IR == PRN:
                # print("IR == PRN")
                print("PRN", self.register[operand_a])
                self.pc += 2

            elif IR == ADD:
                added = self.register[operand_a] + self.register[operand_b]
                print("ADD:", self.register[operand_a],"+", self.register[operand_b], "=", added)
                self.pc += 3

            elif IR == PUSH:
                print("PUSH")
                # Change the position within the stack downward by lowering stack pointer
                self.register[self.sp_index] -= 1
                # value is stored in the register at index of specified pc+1
                value = self.register[operand_a]
                # Set the value to the stack in ram specified by R7 or stack pointer
                self.ram[self.register[self.sp_index]] = value
                # print("IN PUSH, RAM", self.ram)
                # print("IN PUSH, REG", self.register)
                # print("PUSHED", value)
                self.pc += 2
                pass

            elif IR == POP:
                print("POP")
                # Copy the value at SP in ram into specified register
                # then increment
                value = self.ram[self.register[self.sp_index]]
                self.register[operand_a] = value
                self.register[self.sp_index] += 1
                # print("IN POP, RAM", self.ram)
                # print("IN POP, REG", self.register)
                # print("POPPED", value)
                self.pc += 2
                pass

            elif IR == CALL:
                print("CALL")
                self.register[self.sp_index] -= 1
                self.ram[self.register[self.sp_index]] = self.pc + 2
                reg = self.ram[self.pc + 1]
                self.pc = self.register[reg]

            elif IR == RET:
                print("RETURN")
                self.pc = self.ram[self.register[self.sp_index]]
                self.register[self.sp_index] += 1
                pass

            elif IR == HLT:
                print("IR == HLT")
                print("PC at HLT", self.pc)
                running = False

            # Sprint Instructions
            elif IR == CMP:
                print("CMP")
                equal_status = self.alu("CMP", operand_a, operand_b)
                print("Equal_Status Value:", equal_status)
                self.pc += 3

            else:
                print("IR == ELSE")
                sys.exit(1)


cpu = CPU()
cpu.load()
cpu.run()
