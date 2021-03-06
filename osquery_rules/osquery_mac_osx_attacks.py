def rule(event):
    if 'osx-attacks' not in event['name']:
        return False

    # There is another rule specifically for this query
    if 'Keyboard_Event_Taps' in event['name']:
        return False

    if event['action'] != 'added':
        return False

    return True


def dedup(event):
    return event.get('hostIdentifier')


def title(event):
    return 'MacOS malware detected on [{}]'.format(event.get('hostIdentifier'))
