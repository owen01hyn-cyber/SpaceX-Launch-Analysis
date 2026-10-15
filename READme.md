# SpaceX Launch Analysis

## Project Description

This project uses Python to analyze SpaceX launch data and investigate how launch success rates and launch frequency have changed over time. It calculates yearly statistics and creates two line graphs.

## Research Questions

**Main question:** How has SpaceX's launch success rate changed over time?

**Sub-question:** How has the number of SpaceX launches per year changed?

## Dataset

The analysis uses `spacex_launches_20251222.csv`.

Required columns:
- `date_utc`: Date of the launch.
- `success`: Launch result, recorded as `True` or `False`.

Launches without a known success result are excluded. To reproduce the results, place the CSV file in the same folder as the Python script. Include the dataset source/link in your project when available.

## Requirements

- Python 3
- pandas
- matplotlib

Install the libraries with:

```bash
pip install pandas matplotlib
```

## How to Run

1. Download or copy this repository.
2. Make sure `spacex_launches_20251222.csv` and your Python script are in the same folder.
3. Open the folder in Visual Studio Code or a terminal.
4. Run the script (replace `spacex_analysis.py` if your script has a different filename):

   ```bash
   python spacex_analysis.py
   ```

5. Read the results printed in the terminal and view the two graphs.

## Methodology

The Python script:

1. Loads the CSV using pandas.
2. Converts `date_utc` to a datetime value and extracts the launch year.
3. Keeps only rows where `success` is the string `True` or `False`.
4. Converts `True` to 1 and `False` to 0.
5. Groups launches by year and counts total and successful launches.
6. Calculates the yearly success rate:

   **Success rate (%) = (Successful launches / Total launches) × 100**

7. Calculates the mean, median, and standard deviation of the annual success rates.
8. Plots the yearly success rate and number of launches per year.

**Data-format note:** The current script expects the `success` column to contain the strings `True` and `False`. If the CSV stores these values differently, the filtering step may need adjustment.

## Output

The script prints:
- Number of launches per year
- Annual launch success rate (rounded to one decimal place)
- Mean annual success rate
- Median annual success rate
- Standard deviation of annual success rates

It displays two line graphs:

1. **SpaceX Launch Success Rate Over Time** — Year vs. success rate (%).
2. **Number of SpaceX Launches Per Year** — Year vs. number of launches.

## Conclusion

The analysis provides yearly launch counts and success rates to help evaluate how SpaceX launch reliability and launch activity have changed over time. The specific trends and conclusions should be based on the results produced from the dataset.
