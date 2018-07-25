def sun_angle(time):
    hour = int(time.split(':')[0])
    min = int(time.split(':')[1])
    if hour in range(6, 19):
        if hour >= 18 and min > 0:
            return "I don't see the sun!"
        else:
            return (hour - 6) * 15 + (min * 0.25)

    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")




