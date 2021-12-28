import operator

from numpy import unicode_
from numpy.lib.arraysetops import unique

class ScannerReport():
    def __init__(self, scanner, beacons):
        self.Scanner = scanner
        self.Beacons = beacons
    def __str__(self):
        items = list(self.Beacons)
        items.append([0,0])
        items_min = list(map(min, zip(*items)))
        items_max = list(map(max, zip(*items)))
        x_min = items_min[0]
        x_max = items_max[0]
        y_min = items_min[1]
        y_max = items_max[1]
        x_center = abs(x_min)
        y_center = abs(y_min)
        report = [['.' for x in range(x_min, x_max+1)] for y in range(y_min, y_max+1)] 
        report[y_center][x_center] = 'S'
        for beacon in self.Beacons:
            report[y_center+beacon[1]][x_center+beacon[0]] = 'B'
        str = '--- scanner {} ---\n'.format(self.Scanner)
        for y in range(y_max, y_min-1, -1):
            for x in range(x_min, x_max+1):
                str += report[y_center+y][x_center+x]
            str += '\n'
        return str

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

def readScannerReports(file_name, print_report = False):
    scanner_reports = list()
    with open(file_name) as f:
        while(True):
            scanner_report = readScannerReport(f)
            if scanner_report == None:
                break 
            if print_report:
                print(scanner_report)
            scanner_reports.append(scanner_report)
    return scanner_reports

def getBeaconPairs(scanner_report, print_beacons = False):
    beacon_pairs = []
    if print_beacons:
        print('--- beacon pairs scanner {} ---'.format(scanner_report.Scanner))
    for beacon in scanner_report.Beacons:
        for beacon_other in scanner_report.Beacons:
            if beacon[0] == beacon_other[0] and beacon[1] == beacon_other[1]:
                continue
            beacon_delta = list(map(operator.sub, beacon_other, beacon))
            if print_beacons:
                print('{} {} --> {}'.format(beacon, beacon_other, beacon_delta))
            beacon_pairs.append([beacon, beacon_other, beacon_delta])
    return beacon_pairs
                    
def findOverlappingBeacons(scanner_reports):
    matches = 0
    for scanner_report in scanner_reports:
        for scanner_report_other in scanner_reports:
            if scanner_report.Scanner >= scanner_report_other.Scanner:
                continue
            beacon_pairs = getBeaconPairs(scanner_report)
            beacon_pairs_other = getBeaconPairs(scanner_report_other)
            print('compare scanner {} with {}'.format(scanner_report_other.Scanner, scanner_report.Scanner))
            for beacon_pair in beacon_pairs:
                for beacon_pair_other in beacon_pairs_other:
                    error = list(map(operator.sub, beacon_pair[2], beacon_pair_other[2]))
                    abs_error = map(operator.abs, error)
                    if sum(abs_error) == 0:
                        scanner_other = list(map(operator.sub, beacon_pair[0], beacon_pair_other[0]))                        
                        print('{} {} --> {} equals {} {} --> {} ==> {}'.format(beacon_pair[0], beacon_pair[1], beacon_pair[2],
                                                                        beacon_pair_other[0], beacon_pair_other[1], beacon_pair_other[2],
                                                                        scanner_other))   
                        matches += 1
    return matches            

def day19(file_name):
    scanner_reports = readScannerReports(file_name)
    matches = findOverlappingBeacons(scanner_reports)                         
    return matches

if __name__ == '__main__':
    assert(len(readScannerReports('day19_test2d.txt', True)) == 2)
    assert(day19('day19_test2d.txt') == 6)
    assert(len(readScannerReports('day19_test3d.txt')) == 5)
    assert(day19('day19_test3d.txt') == 132)


