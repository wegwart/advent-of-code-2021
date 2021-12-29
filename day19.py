import operator
import matplotlib.pyplot as plt

class ScannerReport():
    def __init__(self, scanner, beacons):
        self.Scanner = scanner
        self.Beacons = beacons

    def plot(self):
        if len(self.Beacons[0]) == 3:
            self.plot3D()
        else:
            self.plot2D()    
            
    def plot2D(self):
        plt.clf()
        x = list(zip(*self.Beacons))[0]
        y = list(zip(*self.Beacons))[1]   
        plt.plot(0, 0, 'o')
        plt.plot(x, y, 'x')
        plt.grid()
        plt.title('--- scanner {} ---\n'.format(self.Scanner))
        #plt.show()
        plt.savefig('day19_2D_scanner{}.png'.format(self.Scanner))   
        
    def plot3D(self):
        plt.clf()
        x = list(zip(*self.Beacons))[0]
        y = list(zip(*self.Beacons))[1]
        z = list(zip(*self.Beacons))[2]
        ax = plt.axes(projection='3d')        
        ax.scatter3D(0, 0, 0, 'o')
        ax.scatter3D(x, y, z, '.')
        ax.grid()
        plt.title('--- scanner {} ---\n'.format(self.Scanner))
        plt.savefig('day19_3D_scanner{}.png'.format(self.Scanner))   
        
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
                    
def findOverlappingBeacons(scanner_reports, print_overlaps = False, print_overlap_results = True):
    overlap_results = []
    for scanner_report in scanner_reports:
        for scanner_report_other in scanner_reports:
            if scanner_report.Scanner >= scanner_report_other.Scanner:
                continue
            beacon_pairs = getBeaconPairs(scanner_report)
            beacon_pairs_other = getBeaconPairs(scanner_report_other)
            if print_overlaps:                        
                print('compare scanner {} with {}'.format(scanner_report_other.Scanner, scanner_report.Scanner))
            for beacon_pair in beacon_pairs:
                for beacon_pair_other in beacon_pairs_other:
                    error = list(map(operator.sub, beacon_pair[2], beacon_pair_other[2]))
                    abs_error = map(operator.abs, error)
                    if sum(abs_error) == 0:
                        scanner_other = list(map(operator.sub, beacon_pair[0], beacon_pair_other[0]))
                        if print_overlaps:                        
                            print('{} {} --> {} equals {} {} --> {} ==> {}'.format(beacon_pair[0], beacon_pair[1], beacon_pair[2],
                                                                            beacon_pair_other[0], beacon_pair_other[1], beacon_pair_other[2],
                                                                            scanner_other))
                        found = False
                        for overlap_result in overlap_results:
                            if scanner_report_other.Scanner == overlap_result[0] and scanner_report.Scanner == overlap_result[1] and scanner_other == overlap_result[2]:
                                found = True
                        if not found:    
                            if print_overlap_results:
                                print('scanner {} to scanner {} --> {}'.format(scanner_report_other.Scanner, scanner_report.Scanner, scanner_other))
                            overlap_results.append([scanner_report_other.Scanner, scanner_report.Scanner, scanner_other])
    return overlap_results            

def day19(file_name):
    scanner_reports = readScannerReports(file_name)
    matches = findOverlappingBeacons(scanner_reports)
    return len(matches)

if __name__ == '__main__':
    assert(len(readScannerReports('day19_test2d.txt')) == 2)
    assert(day19('day19_test2d.txt') == 1)
    assert(len(readScannerReports('day19_test3d.txt')) == 5)
    assert(day19('day19_test3d.txt') == 1)


