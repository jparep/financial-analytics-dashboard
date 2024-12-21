# Interactive Banking Dashboard

This repository hosts an **interactive dashboard** built with Python and Dash to analyze and visualize synthetic banking data. The project demonstrates real-world data visualization techniques, making it suitable for professional portfolios and learning purposes.

---

## Features

- **Interactive Filters**: Filter data by region, account type, and more.
- **Dynamic Visualizations**:
  - Balance distribution histogram.
  - Loan status pie chart.
- **Real-World Use Case**: Designed for banking data insights.
- **Responsive Design**: Compatible with desktop and mobile devices.

---

## Technologies Used

- **Python**: Core programming language.
- **Dash**: Framework for building interactive web applications.
- **Plotly**: Library for creating rich visualizations.
- **Pandas**: Data manipulation and analysis.
- **Faker**: Synthetic data generation.

---

## Dataset

The dataset contains 95,000 synthetic records of banking information, including:

- `Customer_ID`: Unique identifier for each customer.
- `Name`: Customer names.
- `Age`: Customer age.
- `Gender`: Male/Female/Other.
- `Region`: Geographic location.
- `Account_Type`: Savings/Checking/Business.
- `Balance`: Account balance.
- `Loan_Status`: Loan approval status.
- `Loan_Amount`: Loan value.
- `Transaction_Type`: Credit/Debit.
- `Transaction_Amount`: Amount of each transaction.
- `Date`: Transaction date.

The dataset is generated using the [Faker library](https://faker.readthedocs.io/).

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/interactive-banking-dashboard.git
   cd interactive-banking-dashboard
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. Open the dashboard in your browser at [http://127.0.0.1:8050/](http://127.0.0.1:8050/).

---

## Project Structure

```plaintext
interactive-banking-dashboard/
├── app.py                 # Main application code
├── synthetic_banking_data.csv  # Synthetic dataset
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignored files for Git
```

---

## Visualizations

### Balance Distribution Histogram
- Shows the distribution of account balances for selected filters.

### Loan Status Pie Chart
- Displays the proportion of approved and rejected loans.

---

## Future Enhancements

- Add geographic heatmaps for region-wise analysis.
- Include time-series analysis for transaction trends.
- Enhance deployment with Docker and CI/CD pipelines.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**[Your Name]**  
Feel free to connect with me on [LinkedIn](https://www.linkedin.com) or check out my [portfolio](https://your-portfolio-link.com).

---

## Acknowledgments

- [Dash Documentation](https://dash.plotly.com/)
- [Faker Library](https://faker.readthedocs.io/) for generating synthetic data.
