import operator
import matplotlib.pyplot as plt

class ScannerReport():
    def __init__(self, scanner, beacons):
        self.Scanner = scanner
        self.Beacons = beacons
            
    def plot(self):
        plt.clf()
        x = list(zip(*self.Beacons))[0]
        y = list(zip(*self.Beacons))[1]   
        plt.plot(0, 0, 'o')
        plt.plot(x, y, '.')
        plt.grid()
        plt.title('--- scanner {} ---\n'.format(self.Scanner))
        plt.savefig('day19_2D_scanner{}.png'.format(self.Scanner))   
                
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

def readScannerReports(file_name, plot_report = True):
    scanner_reports = list()
    with open(file_name) as f:
        while(True):
            scanner_report = readScannerReport(f)
            if scanner_report == None:
                break 
            if plot_report:
                scanner_report.plot()                   
            scanner_reports.append(scanner_report)
    return scanner_reports

def getBeaconPairs(scanner_report, print_beacons = True):
    beacon_pairs = []
    if print_beacons:
        print('--- beacon pairs scanner {} ---'.format(scanner_report.Scanner))
    for beacon in scanner_report.Beacons:
        for beacon_other in scanner_report.Beacons:
            if beacon[0] == beacon_other[0] and beacon[1] == beacon_other[1]:
                continue
            beacon_delta = list(map(operator.sub, beacon_other, beacon))
            if print_beacons:
                print('{} {} --> delta {}'.format(beacon, beacon_other, beacon_delta))                             
            beacon_pairs.append([beacon, beacon_other, beacon_delta])
    return beacon_pairs
                    
def findOverlappingBeacons(scanner_reports, print_overlap_results = True, print_overlaps = True):
    overlap_results = []
    for scanner_report in scanner_reports:
        for scanner_report_other in scanner_reports:
            if scanner_report.Scanner >= scanner_report_other.Scanner:
                continue
            beacon_pairs = getBeaconPairs(scanner_report)
            beacon_pairs_other = getBeaconPairs(scanner_report_other)
            if print_overlaps:                        
                print('compare scanner {} with {}'.format(scanner_report.Scanner, scanner_report_other.Scanner))
            for beacon_pair in beacon_pairs:
                for beacon_pair_other in beacon_pairs_other:
                    error = list(map(operator.sub, beacon_pair[2], beacon_pair_other[2]))
                    abs_error = map(operator.abs, error)
                    if sum(abs_error) == 0:
                        transform_other = list(map(operator.sub, beacon_pair[0], beacon_pair_other[0]))
                        if print_overlaps:                        
                            print('{} {} --> {} equals {} {} --> {} ==> transform {}'.format(beacon_pair[0], beacon_pair[1], beacon_pair[2],
                                                                            beacon_pair_other[0], beacon_pair_other[1], beacon_pair_other[2],
                                                                            transform_other))
                        found = False
                        for overlap_result in overlap_results:
                            if scanner_report.Scanner == overlap_result[0] and scanner_report_other.Scanner == overlap_result[1] and transform_other == overlap_result[2]:
                                found = True
                        if not found:    
                            if print_overlap_results:
                                print('compare scanner {} with scanner {} --> {}'.format(scanner_report.Scanner, scanner_report_other.Scanner, transform_other))
                            overlap_results.append([scanner_report.Scanner, scanner_report_other.Scanner, transform_other])
    return overlap_results            

class MatchesReport():
    def __init__(self, scanner_reports, matches):
        self.ScannerReports = scanner_reports
        self.Matches = matches

    def plot(self):
        for match in self.Matches:
            plt.clf()            
            scannerA = match[0]
            scannerB = match[1]
            transform = match[2]
            for scannerReport in self.ScannerReports:
                if scannerA == scannerReport.Scanner:                    
                    x = list(zip(*scannerReport.Beacons))[0]
                    y = list(zip(*scannerReport.Beacons))[1]
                    plt.plot(0, 0, 'o')
                    plt.plot(x, y, '.')
            for scannerReport in self.ScannerReports:
                if scannerB == scannerReport.Scanner:                    
                    x = list(zip(*scannerReport.Beacons))[0]
                    y = list(zip(*scannerReport.Beacons))[1]
                    x_new = list(map(lambda xi: xi + transform[0], x))
                    y_new = list(map(lambda yi: yi + transform[1], y))
                    plt.plot(transform[0], transform[1], 'x')
                    plt.plot(x_new, y_new, '.')          
            plt.grid()
            plt.title('--- scanner {} (o) scanner {} (x) ---\n'.format(scannerA, scannerB))
            plt.savefig('day19_2D_scanner{}_scanner{}.png'.format(scannerA, scannerB))           

def day19(file_name):
    scanner_reports = readScannerReports(file_name)
    matches = findOverlappingBeacons(scanner_reports)
    matches_report = MatchesReport(scanner_reports, matches)
    matches_report.plot()
    return len(matches)

if __name__ == '__main__':
    assert(len(readScannerReports('day19_test2d.txt', True)) == 2)
    assert(day19('day19_test2d.txt') == 1)


