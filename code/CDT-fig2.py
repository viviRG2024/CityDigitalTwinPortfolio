"""
Script to generate subplots for Figure 2 in the manuscript.

This script produces three panels:
- fig2c1: bar chart with cumulative percentage line
- fig2c2: bubble plot (without legend row)
- fig2c2_label: bubble plot with a legend row indicating bubble sizes

All outputs are saved as PNG files. Adjust DATA_PATH and OUTPUT_DIR as needed.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# =============================================================================
# Global settings
# =============================================================================
plt.style.use('default')
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["axes.unicode_minus"] = False

# =============================================================================
# User configuration - change these paths if needed
# =============================================================================
DATA_PATH = "D:\\CDT\\data\\count.csv"
OUTPUT_DIR = "D:\\CDT\\figures\\"


# =============================================================================
# Figure 2c2 (bubble plot without legend row)
# =============================================================================
def plot_fig2c2(df, output_path=OUTPUT_DIR + "fig2c2.png"):
    fig, ax = plt.subplots(figsize=(13 / 2.54, 9 / 2.54), dpi=150)

    colors = {
        'Cluster1': '#ee7e77',
        'Cluster2': '#ee8d87',
        'Cluster3': '#ee9d98',
        'Cluster4': '#eeaca8',
        'Cluster5': '#eebbb8',
        'Cluster0': '#cecece',
        'High': '#7fb1b6',
        'Moderate': '#A9CACE',
        'Low': '#D4E4E6'
    }

    series_list = ['Cluster1', 'Cluster2', 'Cluster3', 'Cluster4', 'Cluster5',
                   'Cluster0', 'High', 'Moderate', 'Low']

    # Build y positions with a gap between Cluster0 and High
    y_positions = []
    position_map = {}
    current_y = len(series_list) - 1
    for series in series_list:
        if series == 'High':
            current_y -= 0.5
        position_map[series] = current_y
        y_positions.append(current_y)
        current_y -= 1

    # Vertical grid lines (every 5 years)
    for year in range(2000, 2026, 5):
        if year == 2015:
            ax.axvline(x=year, color='#fedfb2', linestyle='-', alpha=1.0,
                       linewidth=1, zorder=1)
        else:
            ax.axvline(x=year, color='gray', linestyle='-', alpha=0.3,
                       linewidth=0.3, zorder=1)

    # Horizontal grid lines
    for pos in sorted(y_positions, reverse=True):
        ax.axhline(y=pos, color='gray', linestyle='-', alpha=0.3,
                   linewidth=0.3, zorder=1)

    # Bubble scatter
    for series in series_list:
        mask = df[series] > 0
        years = df['year'][mask]
        values = df[series][mask]
        ax.scatter(years,
                   [position_map[series]] * len(years),
                   s=values * 5,
                   c=colors[series],
                   alpha=0.7,
                   zorder=2)

    ax.set_xlim(1999, 2026)
    min_y = min(y_positions) - 0.5
    max_y = max(y_positions) + 0.7
    ax.set_ylim(min_y, max_y)

    # Order y-tick labels from top to bottom
    sorted_indices = np.argsort(y_positions)[::-1]
    sorted_y_positions = np.array(y_positions)[sorted_indices]
    sorted_labels = np.array(series_list)[sorted_indices]

    ax.set_yticks(sorted_y_positions)
    ax.set_yticklabels(sorted_labels)

    # Remove all spines, ticks and labels
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()


# =============================================================================
# Figure 2c2 with legend row (bubble plot + legend bubbles)
# =============================================================================
def plot_fig2c2_label(df, output_path=OUTPUT_DIR + "fig2c2_label.png"):
    fig, ax = plt.subplots(figsize=(12 / 2.54, 10 / 2.54), dpi=150)

    colors = {
        'Cluster1': '#ee7e77',
        'Cluster2': '#ee8d87',
        'Cluster3': '#ee9d98',
        'Cluster4': '#eeaca8',
        'Cluster5': '#eebbb8',
        'Cluster0': '#cecece',
        'High': '#7fb1b6',
        'Moderate': '#A9CACE',
        'Low': '#D4E4E6'
    }

    series_list = ['Cluster1', 'Cluster2', 'Cluster3', 'Cluster4', 'Cluster5',
                   'Cluster0', 'High', 'Moderate', 'Low']

    # Vertical grid lines
    for year in range(2000, 2026, 5):
        if year == 2015:
            ax.axvline(x=year, color='#fedfb2', linestyle='-', alpha=1.0,
                       linewidth=1, zorder=1)
        else:
            ax.axvline(x=year, color='gray', linestyle='-', alpha=0,
                       linewidth=0.3, zorder=1)

    # Horizontal lines for each data row
    for i in range(len(series_list)):
        ax.axhline(y=i, color='gray', linestyle='-', alpha=0.3,
                   linewidth=0.3, zorder=1)

    # Bubbles
    for i, series in enumerate(series_list):
        mask = df[series] > 0
        years = df['year'][mask]
        values = df[series][mask]
        ax.scatter(years,
                   [len(series_list) - 1 - i] * len(years),
                   s=values * 5,
                   c=colors[series],
                   alpha=0.7,
                   zorder=2)

    # Legend row on top (bubbles indicating size)
    legend_y_position = len(series_list)
    legend_years = [2002, 2007, 2012]
    legend_values = [1, 50, 100]
    ax.scatter(legend_years,
               [legend_y_position] * len(legend_years),
               s=np.array(legend_values) * 5,
               c='#cecece',
               alpha=0.7,
               zorder=2)

    ax.set_xlim(1999, 2026)
    ax.set_ylim(-0.8, len(series_list) + 0.5)

    # Set y-ticks (inverted order) but hide them
    ax.set_yticks(range(len(series_list)))
    ax.set_yticklabels(series_list[::-1])

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()


# =============================================================================
# Figure 2c1 (bar + cumulative line)
# =============================================================================
def plot_fig2c1(df, output_path=OUTPUT_DIR + "fig2c1.png"):
    # Ensure data is sorted and filtered
    df = df.sort_values(by='year')
    df = df[(df['year'] >= 2000) & (df['year'] <= 2025)].copy()

    fig, ax1 = plt.subplots(figsize=(12/2.54, 4/2.54), dpi=150, facecolor='white')
    ax1.set_facecolor('white')

    bar_color = '#7fb1b6'
    line_color = '#ee7e77'

    # Cumulative percentage
    df['cumulative_all'] = df['all'].cumsum()
    total_all = df['all'].sum()
    df['cumulative_percentage'] = (df['cumulative_all'] / total_all) * 100

    # Bar chart
    bars = ax1.bar(df['year'], df['all'], color=bar_color, alpha=0.7, width=0.8)

    ax1.set_xlim(1999, 2026)
    ax1.set_ylim(0, 250)
    ax1.set_ylabel('')
    ax1.set_xlabel('')
    ax1.set_yticks(np.arange(0, 251, 50))
    ax1.set_yticklabels([])
    ax1.tick_params(axis='y', width=0.3, color='darkgray')

    # Secondary y-axis for cumulative percentage
    ax2 = ax1.twinx()
    ax2.set_ylabel('')
    ax2.set_ylim(0, 100)
    ax2.set_yticks(np.arange(0, 101, 20))
    ax2.set_yticklabels([])
    ax2.tick_params(axis='y', width=0.3, color='gray')

    # Line plot
    line = ax2.plot(df['year'], df['cumulative_percentage'],
                    color=line_color, linewidth=2, marker='o', markersize=3)

    # X-axis ticks
    years = [2000, 2005, 2010, 2015, 2020, 2025]
    ax1.set_xticks(years)
    ax1.set_xticklabels([])
    ax1.tick_params(axis='x', width=0.3, color='gray')

    # Special vertical line at 2015
    ax1.axvline(x=2015, color='#fedfb2', linestyle='-', alpha=1.0,
                linewidth=1.2, zorder=1)

    # Spines style
    for spine in ax1.spines.values():
        spine.set_color('darkgray')
        spine.set_linewidth(0.3)
    for spine in ax2.spines.values():
        spine.set_color('darkgray')
        spine.set_linewidth(0.3)

    # Legend (empty labels to match original appearance)
    legend_elements = [
        Patch(facecolor=bar_color, alpha=0.7),
        Line2D([0], [0], color=line_color, linewidth=2, marker='o', markersize=3)
    ]
    ax1.legend(legend_elements, ['', ''], loc='upper left',
               frameon=False, labelspacing=0)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()


# =============================================================================
# Main execution
# =============================================================================
if __name__ == "__main__":
    # Load data
    df = pd.read_csv(DATA_PATH)

    # Generate all figures
    plot_fig2c2(df)
    plot_fig2c2_label(df)
    plot_fig2c1(df)

    print("All figures generated successfully.")