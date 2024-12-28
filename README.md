# QualIA

QualIA is a Streamlit-based application designed to help organizations manage and evaluate their quality governance, productivity, transparency, and data/IT metrics effectively. It allows users to upload scoring structures, track selections, and generate visualizations and reports.

## Features

- **Dynamic Category Management**: Upload a scoring structure (`structure.csv`) to dynamically populate categories and options.
- **Selections Tracking**: Use uploaded selections (`selections.csv`) to pre-fill choices.
- **Customizable Score Calculation**: Automatically calculate scores for each category based on user inputs.
- **Data Visualization**: Generate bar charts to visualize category-wise scores.
- **CSV Export**: Save selections and scores to a CSV file for easy sharing and record-keeping.

## Installation

### Prerequisites

- Python 3.8 or higher
- Required Python libraries:
  - `streamlit`
  - `pandas`
  - `matplotlib`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/QualIA.git
   cd QualIA
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

### Sidebar Features
- **QualIA Branding**: Displays the logo, title, and author's name.
- **File Uploads**:
  - `structure.csv`: Define the scoring structure with columns `Category`, `Option`, and `Value`.
  - `selections.csv`: Load previously saved selections.

- **Dynamic Checkboxes**:
  - Checkboxes are dynamically generated based on uploaded `structure.csv`.
  - Pre-filled selections appear based on `selections.csv`.

### Main Page Features

1. **Overview**: Displays example metrics for governance, productivity, transparency, and data/IT.
2. **Bar Chart**: Visualizes the total scores for each category.
3. **Save and Export**:
   - Save current selections to `selections.csv`.
   - Download selections as a CSV file directly from the app.

## Example File Formats

### `structure.csv`
```csv
Category,Option,Value
Governance,Policy Development,100
Governance,Internal Audit,80
Productivity,Process Optimization,150
Transparency,Public Reports,120
Dados e TI,System Integration,200
```

### `selections.csv`
```csv
Category,Option,Value
Governance,Policy Development,100
Productivity,Process Optimization,150
```

## Visual Output
The application generates a bar chart showing the scores for each category:

- **X-axis**: Categories (e.g., Governance, Productivity).
- **Y-axis**: Scores based on selected options.

## Contributions
Contributions are welcome! Fork the repository and submit pull requests with improvements or new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For inquiries or support, reach out to:

- **Author**: Samuel Brasil
