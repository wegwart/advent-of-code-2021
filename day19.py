class ScannerReport():
    def __init__(self, scanner, beacons):
        self.Scanner = scanner
        self.Beacons = beacons
    def __str__(self):
        return 'ScannerReport: Scanner {}, Beacons {}'.format(self.Scanner, len(self.Beacons))

def readScannerReport(f):
    beacons = list()
    while(True):
        line = next(f, '\n')
        if 'scanner' in line:
            scanner = int(line.split(' ')[2])
            continue
        if len(line.strip()) == 0:
            if len(beacons) == 0:
                return None
            return ScannerReport(scanner, beacons)
        beacon = list(map(lambda x: int(x), line.strip().split(',')))
        beacons.append(beacon)

def readScannerReports(file_name):
    scanner_reports = list()
    with open(file_name) as f:
        while(True):
            scanner_report = readScannerReport(f)
            if scanner_report == None:
                break 
            print(scanner_report)
            scanner_reports.append(scanner_report)
    return scanner_reports

def day19(file_name):
    scanner_reports = readScannerReports(file_name)
    return 0

if __name__ == '__main__':
    assert(len(readScannerReports('day19_test.txt')) == 2)
    assert(len(readScannerReports('day19_puzzle.txt')) == 26)
    #assert(day19('day19_test.txt') == 0)
    #day19('day19_puzzle.txt')
