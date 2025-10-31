def cache_mapping():
    cache_size_kb = int(input("Enter size of Cache memory (in KB): "))
    main_mem_mb = int(input("Enter size of Main memory (in MB): "))
    address_bits = int(input("Enter number of bits for Main memory address: "))
    line_size_bytes = int(input("Enter size of each cache line (in Bytes): "))
    mapping_policy = input("Select cache mapping policy (Direct/Associative/Set-Associative): ").strip().lower()
    cache_banks = int(input("Enter number of cache banks: "))
    block_number = int(input("Input any Main memory block number for cache mapping: "))

    cache_size_bytes = cache_size_kb * 1024
    main_mem_bytes = main_mem_mb * 1024 * 1024
    cache_bank_size = cache_size_bytes // cache_banks
    cache_lines = cache_bank_size // line_size_bytes
    main_mem_blocks = main_mem_bytes // line_size_bytes
    byte_offset_bits = line_size_bytes.bit_length() - 1
    line_index_bits = cache_lines.bit_length() - 1
    tag_bits = address_bits - (byte_offset_bits + line_index_bits)

    if mapping_policy == "direct":
        line_number = block_number % cache_lines
        mapping_name = "Direct mapping"
    elif mapping_policy == "associative":
        line_number = "Any line"
        mapping_name = "Associative mapping"
    elif mapping_policy == "set-associative":
        sets = int(input("Enter number of sets: "))
        set_number = block_number % sets
        line_number = f"Set {set_number}"
        mapping_name = "Set-Associative mapping"
    else:
        print("Invalid mapping policy selected!")
        return

    print(f"\nSize of Cache memory = {cache_size_kb} KB ")
    print(f"Size of Main memory = {main_mem_mb} MB ")
    print(f"Main memory address = {address_bits} bits  ")
    print(f"Size of each cache line = {line_size_bytes} Bytes ")
    print(f"Select cache mapping policy: {mapping_name}  ")
    print(f"Number of cache banks = {cache_banks} ")
    print(f"Hence, size of cache bank = {cache_bank_size // 1024} KB ")
    print(f"Cache lines per cache bank = {cache_size_kb} KB/ {line_size_bytes} Bytes = {cache_lines//1024} K = {cache_lines} (Line No-0 to Line No-{cache_lines-1}) ")
    print(f"Main memory address of {address_bits} bits is interpreted in 3 fields as calculated below:  ")
    print(f"LSB {byte_offset_bits} bits for Byte selection ")

    print(f"Number of main memory blocks = {main_mem_mb} MB/{line_size_bytes} Bytes= {main_mem_blocks/(10**6):.1f} M = {main_mem_blocks:.0f} (Block -0 to Block No-{main_mem_blocks-1}) ")

    if mapping_policy == "direct":
        print(f"Middle {line_index_bits} bits for Cache line selection ")
        print(f"MSB {tag_bits} bits (remaining) for the Tags ")
        print(f"Input any Main memory block number for cache mapping = {block_number} ")
        print(f"Block {block_number} is mapped into cache line number = {line_number} ")
    elif mapping_policy == "associative":
        print(f"MSB {tag_bits} bits (remaining) for the Tags ")
        print(f"Input any Main memory block number for cache mapping = {block_number} ")
        print(f"Block {block_number} can be mapped into {line_number} ")
    elif mapping_policy == "set-associative":
        print(f"MSB {tag_bits} bits (remaining) for the Tags ")
        print(f"Input any Main memory block number for cache mapping = {block_number} ")
        print(f"Block {block_number} is mapped into {line_number} ")

cache_mapping()

