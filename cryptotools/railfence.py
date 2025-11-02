et = input("encrypted text:").replace(" ", "")
rails = int(input("rail number:"))

if rails <= 1:
    print("theres no railfence encryption on ts")
else:
    pattern = []
    row = 0
    down = True
    for _ in range(len(et)):
        pattern.append(row)
        if row == 0: #deciding what rails to put the text on
            down = True
        elif row == rails - 1:
            down = False
        row += 1 if down else -1

    rail_lengths = [pattern.count(i) for i in range(rails)]
    rails_list = []
    idx = 0
    for length in rail_lengths:
        rails_list.append(list(et[idx:idx + length])) # adding the text to those rails
        idx += length

    answer = []
    rail_positions = [0] * rails
    for rail_index in pattern:
        answer.append(rails_list[rail_index][rail_positions[rail_index]]) #linking it all up
        rail_positions[rail_index] += 1

    print("answer:", ''.join(answer))
