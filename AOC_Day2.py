import sys

def is_safe_report(report):
    """
    Check if a report is safe according to the Red-Nosed reactor safety rules:
    1. Levels must be either all increasing or all decreasing
    2. Adjacent levels can only differ by 1-3
    
    Args:
        report (list): A list of integers representing levels in a report
    
    Returns:
        bool: True if the report is safe, False otherwise
    """
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
    """
    Analyze a list of reports and count how many are safe
    
    Args:
        reports (list): A list of reports, where each report is a list of integers
    
    Returns:
        dict: Dictionary containing analysis results
    """
    safe_reports = [report for report in reports if is_safe_report(report)]
    return {
        'total_reports': len(reports),
        'safe_reports': len(safe_reports),
        'safe_report_details': safe_reports
    }

def parse_input_file(filename):
    """
    Parse input file into reports
    
    Args:
        filename (str): Path to the input file
    
    Returns:
        list: List of reports
    """
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

def main():
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