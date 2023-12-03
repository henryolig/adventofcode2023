# Part 1:

fp = open('input.txt')
lines = fp.readlines()
calibration_list = []
for line in lines:
    nums = []
    line = line.strip()
    for char in line:
        if char.isdigit():
            nums.append(char)
    calibration_list.append(int(nums[0] + nums[-1]))
fp.close()

print(sum(calibration_list))


# Part 2:

fp = open('input.txt')
lines = fp.readlines()
calibration_list = []
conversion = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for line in lines:
    nums = []
    line = line.strip()
    while line != '':
        if line[0].isdigit():
            nums.append(line[0])
            line = line[1:]
        else:
            for k, v in conversion.items():
                if line.find(k) == 0:
                    nums.append(v)
                    break
            line = line[1:]
    calibration_list.append(int(nums[0] + nums[-1]))
fp.close()


print(sum(calibration_list))


