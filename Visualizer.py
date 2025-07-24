'''

PR.9 Visualizer

PROJECT:- Pandas Analyzer and Data Visualization

OBJECTIVE:- Develop a comprehensive Sales Data Analysis and Visualization tool in 
            Python. This project will utilize Pandas for data manipulation and 
            analysis, Matplotlib and Seaborn for data visualization. Students will 
            gain hands-on experience in handling real-world sales datasets, 
            performing various data operations, and creating insightful 
            visualization to support business decisions.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        """Constructor to initialize the data as None"""
        self.data = None
        print("SalesDataAnalyzer object created.\n")
        self.last_fig = None  

    def __del__(self):
        """Destructor message"""
        print("SalesDataAnalyzer object deleted.\n")

    def load_data(self, file_path):
        """Load data from a CSV file"""
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!\n")
        except FileNotFoundError:
            print("File not found. Please check the file path.\n")

    def explore_data(self):
        """Display first few rows and info of the dataset"""
        if self.data is not None:
            print("First 5 rows of the dataset:\n")
            print(self.data.head())
            print("\nDataset Info:\n")
            print(self.data.info())
            print("\nSummary Statistics:\n")
            print(self.data.describe())
        else:
            print("No data loaded yet.\n")

    def clean_data(self):
        """Handle missing values"""
        if self.data is not None:
            print("Missing values before cleaning:\n")
            print(self.data.isnull().sum())
            self.data = self.data.dropna()  
            print("\nMissing values handled successfully.\n")
        else:
            print("No data loaded to clean.\n")

    def mathematical_operations(self):
        """Perform sample mathematical operations"""
        if self.data is not None:
            print("Total Sales:", self.data["Sales"].sum())
            print("Average Profit:", self.data["Profit"].mean())
        else:
            print("No data available.\n")

    def search_sort_filter(self):
        """Provide Search, Sort, and Filter functionality"""
        if self.data is not None:
            while True:
                print("\n🔍 Search, Sort & Filter Menu")
                print("1. Search by Customer Name")
                print("2. Sort by Any Column")
                print("3. Filter → Group By + Aggregation")
                print("4. 🔙 Return to Main Menu")

                sub_choice = input("Enter your choice (1–4): ")

                if sub_choice == "1":
                    # SEARCH
                    name = input("Enter customer name to search: ").strip()
                    result = self.data[self.data["Customer Name"].str.contains(name, case=False, na=False)]
                    print(f"\n🔎 Found {len(result)} records:\n")
                    if len(result) > 10:
                        print(f"\n📊 Top 10 records of {name} :\n")
                    else:
                        print(f"\n📊 {len(result)} records of {name} :\n")
                    print(result.head(10))

                elif sub_choice == "2":
                    # SORT
                    print("\n🧾 Available Columns:")
                    print(list(self.data.columns))
                    column = input("Enter column to sort by: ").strip()

                    if column in self.data.columns:
                        order = input("Sort order? (asc/desc): ").lower()
                        ascending = True if order == "asc" else False
                        sorted_data = self.data.sort_values(by=column, ascending=ascending)
                        print(f"\n📊 Top 10 records sorted by '{column}' ({order.upper()}):\n")
                        print(sorted_data.head(10))
                    else:
                        print("❌ Invalid column name.")

                elif sub_choice == "3":
                    # FILTER → GROUP BY + AGG
                    print("\n📌 Available Columns:")
                    print(list(self.data.columns))
                    group_col = input("Enter column to group by: ").strip()
                    agg_col = input("Enter column to apply function on: ").strip()
                    func = input("Enter function (sum/mean/count/min/max): ").strip().lower()

                    if group_col in self.data.columns and agg_col in self.data.columns:
                        if func in ["sum", "mean", "count", "min", "max"]:
                            grouped = self.data.groupby(group_col)[agg_col]
                            agg_result = getattr(grouped, func)()
                            print(f"\n📊 Grouped Data ({func.upper()} of '{agg_col}' by '{group_col}'):\n")
                            print(agg_result.head(10))
                        else:
                            print("❌ Unsupported function. Try sum/mean/count/min/max.")
                    else:
                        print("❌ One or both columns are invalid.")

                elif sub_choice == "4":
                    print("Returning to main menu...\n")
                    break
                else:
                    print("❌ Invalid choice. Please enter 1–4.")
        else:
            print("❌ No data to search/sort/filter.\n")


    def statistical_analysis(self):
        """Show statistical info"""
        if self.data is not None:
            numeric_data = self.data.select_dtypes(include='number')  
            print("Standard Deviation:\n",numeric_data.std())
            print("\nVariance:\n",numeric_data.var())
            print("\nQuantiles:\n",numeric_data.quantile([0.25, 0.5, 0.75]))
        else:
            print("No data available.\n")


    def create_pivot_table(self):
        """Create pivot table to summarize sales by Region and Category"""
        if self.data is not None:
            pivot = pd.pivot_table(self.data, index="Region", columns="Category", values="Sales", aggfunc="sum")
            print("\nPivot Table:\n", pivot)
        else:
            print("No data loaded.\n")

    def visualize_data(self):
        """Create beautiful, error-free, and professional plots with looped interaction."""
        if self.data is not None:
            sns.set_theme(style="whitegrid")  # Clean visual theme

            while True:
                print("\n📊 Chart Options:")
                print("1. Bar Plot (Sales by Region)")
                print("2. Line Plot (Sales Over Time)")
                print("3. Scatter Plot (Custom X vs Y)")
                print("4. Pie Chart (Sales by Category)")
                print("5. Histogram (Sales Distribution)")
                print("6. Stack Plot (Sales vs Profit by Region)")
                print("7. 🔙 Return to Main Menu")

                try:
                    choice = int(input("Enter your choice (1–7): "))
                    if choice == 7:
                        print("Returning to main menu...\n")
                        break  # Exit the visualize loop to main menu
                    
                    fig = plt.figure(figsize=(12, 6))
                    self.last_fig = fig

                    if choice == 1:
                        grouped = self.data.groupby("Region")["Sales"].sum().sort_values()
                        sns.barplot(x=grouped.index, y=grouped.values, palette="Set2")
                        plt.title("💼 Total Sales by Region", fontsize=16, weight='bold')
                        plt.xlabel("Region", fontsize=12)
                        plt.ylabel("Sales", fontsize=12)
                        plt.xticks(rotation=45, ha='right')

                    elif choice == 2:
                        df = self.data.copy()
                        df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')
                        df = df.dropna(subset=["Order Date"])
                        df = df.sort_values("Order Date")
                        daily_sales = df.groupby("Order Date")["Sales"].sum()
                        plt.plot(daily_sales.index, daily_sales.values, color="royalblue", linewidth=2.2)
                        plt.title("📈 Sales Trend Over Time", fontsize=16, weight='bold')
                        plt.xlabel("Order Date", fontsize=12)
                        plt.ylabel("Sales", fontsize=12)
                        plt.xticks(rotation=30)

                    elif choice == 3:
                        print("Available columns:", list(self.data.columns))
                        x = input("Enter x-axis column: ").strip()
                        y = input("Enter y-axis column: ").strip()
                        if x in self.data.columns and y in self.data.columns:
                            sns.scatterplot(data=self.data, x=x, y=y, hue="Region", palette="tab10")
                            plt.title(f"🎯 {y} vs {x}", fontsize=16, weight='bold')
                            plt.xlabel(x, fontsize=12)
                            plt.ylabel(y, fontsize=12)
                        else:
                            print("❌ Invalid column names.")
                            continue

                    elif choice == 4:
                        cat_sales = self.data.groupby("Category")["Sales"].sum()
                        colors = sns.color_palette("pastel")
                        plt.pie(cat_sales, labels=cat_sales.index, autopct='%1.1f%%',
                                startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
                        plt.title("🧩 Sales Distribution by Category", fontsize=16, weight='bold')
                        plt.axis('equal')

                    elif choice == 5:
                        sales = self.data["Sales"].dropna()
                        # Optional: remove extreme outliers for better plotting
                        q_low = sales.quantile(0.01)
                        q_high = sales.quantile(0.99)
                        sales = sales[(sales >= q_low) & (sales <= q_high)]

                        # Plot WITHOUT KDE to avoid warnings
                        sns.histplot(sales, bins=20, color="teal", edgecolor="black")
                        plt.title("Sales Distribution", fontsize=16, weight='bold')  # removed emoji
                        plt.xlabel("Sales", fontsize=12)
                        plt.ylabel("Frequency", fontsize=12)


                    elif choice == 6:
                        stacked = self.data.groupby("Region")[["Sales", "Profit"]].sum()
                        stacked.plot(kind="bar", stacked=True, colormap="Set3", figsize=(12, 6), edgecolor="black")
                        plt.title("📦 Sales & Profit by Region", fontsize=16, weight='bold')
                        plt.xlabel("Region", fontsize=12)
                        plt.ylabel("Amount", fontsize=12)
                        plt.xticks(rotation=0)
                        plt.legend(title="Metric", loc="upper right")
                        plt.tight_layout()
                        self.last_fig = plt.gcf()  # Save current figure
                        plt.grid(axis='y', linestyle='--', alpha=0.5)
                        plt.show()
                        save_choice = input("💾 Do you want to save this chart? (y/n): ").lower()
                        if save_choice == 'y':
                            self.save_visualization()

                        continue  # Stay in the loop

                    else:
                        print("❌ Invalid choice.")
                        continue

                    # Final layout formatting for non-Stack plots
                    plt.tight_layout()
                    plt.grid(True, linestyle='--', alpha=0.5)
                    plt.tick_params(axis='both', labelsize=10)
                    plt.show()
                    save_choice = input("💾 Do you want to save this chart? (y/n): ").lower()
                    if save_choice == 'y':
                        self.save_visualization()


                except Exception as e:
                    print("⚠️ Error occurred:", e)

        else:
            print("❌ Please load data first.\n")

    def save_visualization(self):
        """Save the last viewed chart as a high-quality image file."""
        if self.last_fig:
            filename = input("Enter filename to save (e.g. 'chart.png'): ").strip()
            if not filename.endswith(".png"):
                filename += ".png"  # Ensure PNG extension
            try:
                self.last_fig.savefig(filename, dpi=300, bbox_inches='tight')
                print(f"✅ Chart saved successfully as: {filename}\n")
            except Exception as e:
                print(f"❌ Error saving chart: {e}")
        else:
            print("⚠️ No chart available to save yet. Please view a chart first.\n")



# === Main Program ===

def menu():
    obj = SalesDataAnalyzer()

    while True:
        print("""
========== Data Analysis & Visualization Program ==========
Please select an option:
1. Load Dataset
2. Explore Data
3. Clean Data
4. Mathematical Operations
5. Search, Sort & Filter
6. Statistical Analysis
7. Create Pivot Table
8. Visualize Data
9. Save Visualization
10. Exit
===========================================================
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter CSV file path (e.g. data/Superstore.csv): ")
            obj.load_data(path)
        elif choice == "2":
            obj.explore_data()
        elif choice == "3":
            obj.clean_data()
        elif choice == "4":
            obj.mathematical_operations()
        elif choice == "5":
            obj.search_sort_filter()
        elif choice == "6":
            obj.statistical_analysis()
        elif choice == "7":
            obj.create_pivot_table()
        elif choice == "8":
            obj.visualize_data()
        elif choice == "9":
            obj.save_visualization()
        elif choice == "10":
            print("Exiting the program. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
