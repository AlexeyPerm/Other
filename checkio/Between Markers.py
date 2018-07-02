def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    if text.find(begin) == -1:
        start = 0
    else:
        start = text.find(begin) + len(begin)

    if text.find(end) == -1:
        stop = None
    else:
        stop = text.find(end)

    return text[start:stop]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers("<head><title>My new site</title></head>",
                        "<title>", "</title>"))
    print( between_markers('No[/b] hi', '[b]', '[/b]'))
    print( between_markers('No [b]hi', '[b]', '[/b]'))
    print( between_markers('No hi', '[b]', '[/b]'))
    print( between_markers('No <hi>', '>', '<'))
    print('Wow, you are doing pretty good. Time to check it!')