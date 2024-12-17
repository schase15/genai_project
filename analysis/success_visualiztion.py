import matplotlib.pyplot as plt
import numpy as np

def create_comparison_plot():
    # Data from goat_optimization.txt
    models = ['Meta-Llama-3-1-8B', 'GPT-4o-mini', 'GPT-4o']
    
    # Success rates with GOAT specific questions
    goat_rates = [48.5, 54.5, 66.7]  # GOAT success rates
    non_goat_rates = [45.5, 57.6, 57.6]  # Non-GOAT success rates

    # Overall success rates
    # non_goat_rates = [59.50, 66.00, 64.50]  # Average success rates without GOAT
    # goat_rates = [48.00, 53.50, 55.00]  

    # Set up the bar chart
    x = np.arange(len(models))
    width = 0.25  # Thin bars
    
    # Changed figure size to be taller and narrower
    fig, ax = plt.subplots(figsize=(9, 8))
    
    # Reduced spacing between groups by adjusting the x positions
    rects1 = ax.bar(x - width/2, goat_rates, width, label='With GOAT', color='#ff7f0e')
    rects2 = ax.bar(x + width/2, non_goat_rates, width, label='Without GOAT', color='#1f77b4')
    
    # Increase all font sizes
    plt.rcParams.update({'font.size': 16})  # Increased base font size
    
    ax.set_ylabel('Success Rate (%)', fontsize=18)
    ax.set_title('Success Rate Comparison Across Subset of Questions', fontsize=20)
    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=45, fontsize=16, ha='right')
    ax.legend(fontsize=16)
    
    # Reduce the plot range to decrease spacing between groups
    ax.set_xlim(x[0] - 0.35, x[-1] + 0.35)  # Even tighter x-axis limits
    
    # Add more space at the top
    ax.set_ylim(0, max(max(goat_rates), max(non_goat_rates)) * 1.2)  # 20% more space at the top
    
    # Add value labels on top of each bar with larger font
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.1f}%',
                       xy=(rect.get_x() + rect.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom',
                       fontsize=14)  # Increased font size for bar labels
    
    autolabel(rects1)
    autolabel(rects2)
    
    # Adjust layout and display
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('./subset-graph1.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_comparison_plot()