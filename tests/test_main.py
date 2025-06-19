import os
import runpy
import pytest # Using pytest for test structure and fixtures if needed later

# Define the path to the script and the expected output file
SCRIPT_PATH = "src/main.py"
OUTPUT_CSV_PATH = "data/DATA_FORMATEADA.csv"
OUTPUT_EXCEL_PATH = "car_evaluation_data.xlsx" # main.py also creates this

def test_main_script_execution_and_output():
    """
    Tests if src/main.py runs to completion without errors and
    creates the expected data/DATA_FORMATEADA.csv file.
    """
    # Ensure output files don't exist before running the script
    if os.path.exists(OUTPUT_CSV_PATH):
        os.remove(OUTPUT_CSV_PATH)
    if os.path.exists(OUTPUT_EXCEL_PATH):
        os.remove(OUTPUT_EXCEL_PATH)

    # Assert that files are indeed removed (or didn't exist)
    assert not os.path.exists(OUTPUT_CSV_PATH), f"Pre-test cleanup failed: {OUTPUT_CSV_PATH} still exists."
    assert not os.path.exists(OUTPUT_EXCEL_PATH), f"Pre-test cleanup failed: {OUTPUT_EXCEL_PATH} still exists."

    try:
        # Execute the script
        # The script is expected to run in the context of the repository root
        runpy.run_path(SCRIPT_PATH, run_name="__main__") # run_name='__main__' ensures if __name__ == '__main__': blocks run
    except Exception as e:
        pytest.fail(f"src/main.py raised an exception during execution: {e}")

    # Verify that the CSV output file was created
    assert os.path.exists(OUTPUT_CSV_PATH), f"Script {SCRIPT_PATH} did not create the output file {OUTPUT_CSV_PATH}."

    # Verify that the Excel output file was also created (as main.py does this)
    assert os.path.exists(OUTPUT_EXCEL_PATH), f"Script {SCRIPT_PATH} did not create the output file {OUTPUT_EXCEL_PATH}."

    # Optional: Clean up created files after test
    # This is good practice, especially if file content was also checked.
    # For this test, which primarily checks existence, it's less critical if setUp always cleans.
    # However, let's keep it for completeness.
    if os.path.exists(OUTPUT_CSV_PATH):
        os.remove(OUTPUT_CSV_PATH)
    if os.path.exists(OUTPUT_EXCEL_PATH):
        os.remove(OUTPUT_EXCEL_PATH)

if __name__ == "__main__":
    # This allows running the test file directly for debugging,
    # though 'pytest' is the recommended way to run tests.
    pytest.main([__file__])
