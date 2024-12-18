import sys

def is_safe_report(report):
    # Check if levels are increasing
    def is_increasing(lst):
        return all(lst[i+1] - lst[i] >= 1 and lst[i+1] - lst[i] <= 3 for i in range(len(lst) - 1))
    
    # Check if levels are decreasing
    def is_decreasing(lst):
        return all(lst[i] - lst[i+1] >= 1 and lst[i] - lst[i+1] <= 3 for i in range(len(lst) - 1))
    
    # Ensure report has at least 2 levels and all levels are unique
    if len(report) < 2 or len(set(report)) != len(report):
        return False
    
    # Check if the report is either completely increasing or completely decreasing
    return is_increasing(report) or is_decreasing(report)

def analyze_reactor_reports(reports):
    safe_reports = []
    for report in reports:
        # Check if report is safe directly or with Problem Dampener
        if is_safe_report(report) or apply_problem_dampener(report):
            safe_reports.append(report)
    
    return {
        'total_reports': len(reports),
        'safe_reports': len(safe_reports),
        'safe_report_details': safe_reports
    }

def parse_input_file(filename):
    try:
        with open(filename, 'r') as file:
            reports = []
            for line in file:
                # Convert line to list of integers
                report = [int(x) for x in line.strip().split()]
                reports.append(report)
        return reports
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid input in file '{filename}'. Ensure all entries are integers.")
        sys.exit(1)

def apply_problem_dampener(report):
    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        # Create a new report without the i-th level
        dampened_report = report[:i] + report[i+1:]
        
        # Check if the dampened report is safe
        if is_safe_report(dampened_report):
            return True
    
    return False

def parse_input_file(filename):
    try:
        with open(filename, 'r') as file:
            reports = []
            for line in file:
                # Convert line to list of integers
                report = [int(x) for x in line.strip().split()]
                reports.append(report)
        return reports
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    except ValueError:
        print("Error: Invalid input in file. Ensure all entries are integers.")
        exit(1)

def main():
    import sys
    
    # Check if filename is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    # Get filename from command-line argument
    input_filename = sys.argv[1]
    
    # Parse input file and analyze reports
    reports = parse_input_file(input_filename)
    result = analyze_reactor_reports(reports)
    
    # Print results
    print(f"\nTotal Reports: {result['total_reports']}")
    print(f"Safe Reports: {result['safe_reports']}")
    
    # Optionally print details of safe reports
    if result['safe_reports'] > 0:
        print("\nSafe Reports Details:")
        for report in result['safe_report_details']:
            print(report)

if __name__ == "__main__":
    main()