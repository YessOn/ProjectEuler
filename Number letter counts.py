units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hunderds = ['hundred', 'thousand', 'and']
result = 0

for i in range(1, 1001):
    unit = i%10
    ten = (i//10)%10
    hundered = (i//100)%10
    thousand = (i//1000)%10
    if thousand != 0:
        result += len(units[0]) + len(hunderds[1])
    if i%1000 != 0:
        if hundered != 0:
            result += len(units[hundered-1]) + len(hunderds[0])
            if i%100 != 0:
                result += len(hunderds[2])
        if i%100 != 0:
            if ten < 2:
                result += len(units[i%100-1])
            else:
                result += len(tens[ten-2])
                if unit != 0:
                    result += len(units[unit-1])
print(result)

# The answer: 21124
