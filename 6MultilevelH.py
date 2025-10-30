def multilevel_memory_analysis():
    n = int(input("Enter number of memory levels (2 or 3): "))
    if n not in [2, 3]:
        print("❌ Error: Only 2 or 3 levels are supported.")
        return
    cost, size, hit_rate, access_time = [], [], [], []
    print("\n--- Enter cost per bit (INR) for each level ---")
    for i in range(n):
        c = float(input(f"Enter C{i+1}: "))
        cost.append(c)
    print("\n--- Enter size (in bits) for each level ---")
    for i in range(n):
        s = float(input(f"Enter S{i+1}: "))
        size.append(s)
    print("\n--- Enter hit rate for each level ---")
    for i in range(n):
        if i == n - 1:
            print(f"Hit rate H{i+1} is automatically set to 1.0 (last level)")
            hit_rate.append(1.0)
        else:
            h = float(input(f"Enter H{i+1}: "))
            hit_rate.append(h)
    print("\n--- Enter access time (in microseconds) for each level ---")
    for i in range(n):
        ta = float(input(f"Enter ta{i+1}: "))
        access_time.append(ta)
    total_size = sum(size)
    cost_components = [f"({cost[i]} × {int(size[i])})" for i in range(n)]
    cost_values = [cost[i] * size[i] for i in range(n)]
    cav_numerator_val = sum(cost_values)
    cav = cav_numerator_val / total_size
    if n == 2:
        h1, ta1, ta2 = hit_rate[0], access_time[0], access_time[1]
        tav = h1 * ta1 + (1 - h1) * ta2
    else:
        h1, h2 = hit_rate[0], hit_rate[1]
        ta1, ta2, ta3 = access_time
        tav = h1 * ta1 + (1 - h1) * h2 * ta2 + (1 - h1) * (1 - h2) * ta3
    print("\n--- 📤 Output ---")
    print(f"Case-{n - 1}: Consider {n}-level memory hierarchy (n = {n})")
    if n == 2:
        print(f"Cost/bit (in INR): C1 = {cost[0]}, C2 = {cost[1]}")
        print(f"Size (bits): S1 = {int(size[0])}, S2 = {int(size[1])}")
        print(f"Hit rate/ratio: H1 = {hit_rate[0]}, H2 = 1.0")
        print(f"Access time (µs): ta1 = {access_time[0]}, ta2 = {access_time[1]}")
    else:
        print(f"Cost/bit (in INR): C1 = {cost[0]}, C2 = {cost[1]}, C3 = {cost[2]}")
        print(f"Size (bits): S1 = {int(size[0])}, S2 = {int(size[1])}, S3 = {int(size[2])}")
        print(f"Hit rate/ratio: H1 = {hit_rate[0]}, H2 = {hit_rate[1]}, H3 = 1.0")
        print(f"Access time (µs): ta1 = {access_time[0]}, ta2 = {access_time[1]}, ta3 = {access_time[2]}")
    print("\n✅ Average cost/bit (INR):")
    print(f"= ({' + '.join(cost_components)}) / {int(total_size)}")
    print(f"= ({' + '.join(str(int(v)) for v in cost_values)}) / {int(total_size)}")
    print(f"= {int(cav_numerator_val)} / {int(total_size)}")
    print(f"= {round(cav, 7)}")
    print("\n⏱ Average access time (µs):")
    if n == 2:
        print(f"= H1 × ta1 + (1 - H1) × ta2")
        print(f"= ({h1} × {ta1}) + ((1 - {h1}) × {ta2})")
    else:
        print(f"= H1 × ta1 + (1 - H1) × H2 × ta2 + (1 - H1) × (1 - H2) × ta3")
        print(f"= ({h1} × {ta1}) + ((1 - {h1}) × {h2} × {ta2}) + ((1 - {h1}) × (1 - {h2}) × {ta3})")
    print(f"= {round(tav, 2)} µs")
multilevel_memory_analysis()
