import sys

if len(sys.argv) == 4:
	block_number = int(sys.argv[1])
	block_size = int(sys.argv[2])
	hardware_counter = sys.argv[3]

	with open("src/main.rs", "w") as rust_file:
		rust_file.write("use perfcnt::linux::{HardwareEventType, PerfCounterBuilderLinux};use perfcnt::{AbstractPerfCounter, PerfCounter};use std::arch::asm;")

		rust_file.write("fn main() {{let mut pc: PerfCounter =PerfCounterBuilderLinux::from_hardware_event(HardwareEventType::{}).finish().expect(\"Could not create the counter\");pc.start().expect(\"Can not start the counter\");".format(hardware_counter))

		block = "\"jmp 2f\"," + ''.join(["\"nop\","]*block_size) + "\"2:\""
		for _ in range(block_number):
			rust_file.write("unsafe {{ asm!({})}};".format(block))

		#unsafe { asm!("jmp 2f", "nop", "nop", "nop", "nop", "2:") };

		rust_file.write("pc.stop().expect(\"Can not stop the counter\");let res = pc.read().expect(\"Can not read the counter\");println!(\"Measured {{}} for counter {}.\", res);}}".format(hardware_counter))
