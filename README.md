# happiness_data
From a given .csv file the python code plots scatter graph to analyse correlation between country and happiness
This Python code leverages the `streamlit`, `pandas`, and `plotly.express` libraries to build a web application that visualizes relationships between different factors affecting happiness in a dataset.

1. **`streamlit`**: This is an open-source Python library that allows you to easily create and share beautiful, custom web apps for machine learning and data science. In this code, it's used to design the web application's interface, including creating the title, dropdown boxes, and the section to display scatter plot and text.

2. **`pandas`**: A Python library for data manipulation and analysis. Here it's used to read a CSV file containing the happiness data into a DataFrame, which is a table-like data structure that's mutable and can be manipulated in-memory.

3. **`plotly.express`**: A library that provides a simple syntax for complex charts. In the code, it's used to create scatter plots based on the user's selection of x and y variables from the dropdown boxes.

The script starts by importing the necessary libraries and then setting the title of the web application. It defines a tuple, `options`, which contains the available attributes from the dataset: "country", "happiness", "gdp", "social_support", "life_expectancy", "freedom_to_make_life_choices", "generosity", and "corruption". It reads a CSV file, "happy.csv", into a pandas DataFrame, `df`.

The user is prompted to select an attribute from the options tuple for the x-axis and y-axis of the scatter plot. If the combination of the x and y variables chosen by the user is valid (i.e., they are not the same), a scatter plot is created with `plotly.express` and displayed using `st.plotly_chart()`. The script also outputs the user's current selection of x and y variables. If the combination is invalid, a message stating "Invalid combination" is shown. 

Overall, the code is creating a web-based, interactive data visualization tool that allows users to explore relationships between different variables related to happiness.

```
git clone https://github.com/stillwrinkled/happiness_data.git

```
