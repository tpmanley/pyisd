import sys
import re
import zigbee_crypt
import zipfile

def parse_event(event):
    #[721629332 576 16908322 Packet B1] [ember01] [0A 03 08 E3 FF FF FF FF 07 56 A7 01]
    result = re.match(r"\[\d+ \d+ \d+ Packet [A-F0-9]{2}\] \[.*\] \[(.*)\]", event)
    if result:
        return result.group(1)
    return None

def get_event(isd_file):
    with zipfile.ZipFile(isd_file, 'r') as z:
        with z.open('event.log', 'r') as event_file:
            for event in event_file:
                parsed_event = parse_event(event)
                if parsed_event:
                    yield parsed_event

def parse_isd(isd_file):
    for event in get_event(isd_file):
        print(event)


if __name__ == "__main__":
    isd_file = sys.argv[1]
    parse_isd(isd_file)

