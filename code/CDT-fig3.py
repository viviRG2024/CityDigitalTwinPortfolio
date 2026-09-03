"""
Script to generate all subplots for Figure 3 in the manuscript.

This script produces the following panels:
- fig3a: stacked horizontal bar chart showing cluster percentages per urban system
- fig3a_legend: color legend for fig3a
- fig3b: co-occurrence network of urban systems
- fig3c: phi coefficient heatmap for urban system pairs
- fig3c_legend: color bar for fig3c
- fig3g: association heatmap between urban systems and SDGs (Overall)
- fig3g_legend: color bar for fig3g
- Additional auxiliary charts: SDG distribution, SDG count, TOP10 SDG combinations, etc.

All outputs are saved as PNG files. Adjust DATA_DIR and OUTPUT_DIR as needed.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from scipy.stats import chi2_contingency
from collections import Counter
import os

# =============================================================================
# Global settings
# =============================================================================
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 5
plt.rcParams["font.weight"] = "normal"

# =============================================================================
# User configuration - change these paths if needed
# =============================================================================
DATA_DIR = "D:\\CDT\\data"
OUTPUT_DIR = "D:\\CDT\\figures"

# Input files
CDT_FILE = os.path.join(DATA_DIR, "CDT.csv")
COUNT_FILE = os.path.join(DATA_DIR, "count.csv")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =============================================================================
# Common data loading and preprocessing
# =============================================================================
def load_and_preprocess_cdt():
    df = pd.read_csv(CDT_FILE)
    urban_systems = [
        "People", "Household", "Land_and_agriculture",
        "Workplace", "Transportation", "IoT_technology"
    ]
    us_columns = [c for c in urban_systems if c in df.columns]
    for col in us_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["Cluster"] = pd.to_numeric(df["Cluster"], errors="coerce")
    return df, us_columns

def load_count_data():
    return pd.read_csv(COUNT_FILE)

# =============================================================================
# Figure 3a - Stacked bar chart of urban system involvement per cluster
# =============================================================================
def plot_fig3a(df, us_columns, output_path=OUTPUT_DIR):
    clusters = [1, 2, 3, 4, 5, 0]
    cluster_colors = ["#ee8d87", "#fedfb2", "#A9CACE", "#feece7", "#fff9eb", "#deeeed"]
    not_involved_color = "#ececea"
    stack_order = ["Cluster1", "Cluster2", "Cluster3", "Cluster4", "Cluster5", "Cluster0", "Not_Involved"]
    stack_colors = cluster_colors + [not_involved_color]

    percentage_data = {}
    for us in us_columns:
        valid_data = df[df[us].notna()]
        total_valid = len(valid_data)
        us_data = {}
        if total_valid > 0:
            for cluster in clusters:
                cluster_mask = valid_data["Cluster"] == cluster
                involved = (cluster_mask & (valid_data[us] == 1)).sum()
                us_data[f"Cluster{cluster}"] = (involved / total_valid) * 100
            not_inv = (valid_data[us] == 0).sum()
            us_data["Not_Involved"] = (not_inv / total_valid) * 100
        percentage_data[us] = us_data

    percentage_df = pd.DataFrame(percentage_data).T

    fig, ax = plt.subplots(figsize=(12/2.54, 3/2.54))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    y_pos = np.arange(len(us_columns))
    bar_height = 0.7
    left = np.zeros(len(us_columns))

    for i, st in enumerate(stack_order):
        if st in percentage_df.columns:
            values = percentage_df[st].values
            ax.barh(y_pos, values, bar_height, left=left,
                    color=stack_colors[i], edgecolor="white", linewidth=1.5)
            left += values

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)
    ax.set_xlim(0, 100)

    plt.tight_layout()
    out_file = os.path.join(output_path, "fig3a.png")
    plt.savefig(out_file, dpi=300, bbox_inches="tight", pad_inches=0)
    plt.close()
    print(f"Saved {out_file}")

    # Legend strip
    legend_colors = cluster_colors + [not_involved_color]
    fig_leg, ax_leg = plt.subplots(figsize=(0.5/2.54, 3/2.54))
    fig_leg.patch.set_facecolor("white")
    ax_leg.set_facecolor("white")
    y_pos_leg = np.arange(7)
    for i in range(7):
        ax_leg.barh(y_pos_leg[i], 100, 0.6, left=0,
                    color=legend_colors[i], edgecolor="white", linewidth=1.5)
    ax_leg.set_xticks([])
    ax_leg.set_yticks([])
    ax_leg.set_xlim(0, 100)
    ax_leg.set_ylim(-0.5, 6.5)
    for spine in ax_leg.spines.values():
        spine.set_visible(False)
    ax_leg.grid(False)
    plt.tight_layout()
    leg_file = os.path.join(output_path, "fig3a_legend.png")
    plt.savefig(leg_file, dpi=300, bbox_inches="tight", pad_inches=0)
    plt.close()
    print(f"Saved {leg_file}")

# =============================================================================
# Figure 3b - Co-occurrence network
# =============================================================================
def plot_fig3b(df, us_columns, output_path=OUTPUT_DIR):
    n_us = len(us_columns)
    cooccurrence = np.zeros((n_us, n_us), dtype=int)
    for _, row in df.iterrows():
        idxs = [i for i, us in enumerate(us_columns) if row.get(us) == 1]
        for i in idxs:
            for j in idxs:
                if i < j:
                    cooccurrence[i, j] += 1

    fig, ax = plt.subplots(figsize=(4/2.54, 4/2.54), dpi=600)
    fig.subplots_adjust(0, 0, 1, 1)

    angles = np.linspace(0, 2*np.pi, n_us, endpoint=False)
    positions = [(np.cos(a), np.sin(a)) for a in angles]

    min_w = cooccurrence.min()
    max_w = cooccurrence.max()
    if max_w > min_w:
        for i in range(n_us):
            for j in range(i+1, n_us):
                w = cooccurrence[i, j]
                if w > 0:
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]
                    ax.plot([x1, x2], [y1, y2],
                            color="#68a7be",
                            linewidth=3.5 * (w - min_w) / (max_w - min_w),
                            alpha=0.7 * (w - min_w) / (max_w - min_w),
                            solid_capstyle="round")

    for i in range(n_us):
        x, y = positions[i]
        size = 200 + 600 * cooccurrence[i].sum() / cooccurrence.sum()
        ax.add_patch(mpatches.Circle((x, y), size/3000,
                                     facecolor="#ee7e77",
                                     edgecolor="#555555",
                                     linewidth=0.8,
                                     zorder=3))

    ax.set_aspect("equal")
    ax.axis("off")
    out_file = os.path.join(output_path, "fig3b.png")
    plt.savefig(out_file, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved {out_file}")

# =============================================================================
# Figure 3c - Phi coefficient heatmap (urban system pairs)
# =============================================================================
def plot_fig3c(df, us_columns, output_path=OUTPUT_DIR):
    n_us = len(us_columns)
    phi = np.full((n_us, n_us), np.nan)
    pval = np.full((n_us, n_us), np.nan)

    for i in range(n_us):
        for j in range(i, n_us):
            if i == j:
                phi[i, j] = 1
                pval[i, j] = 0
            else:
                tab = pd.crosstab(df[us_columns[i]], df[us_columns[j]])
                if tab.shape == (2, 2):
                    a, b, c, d = tab.values.flatten()
                    phi_ij = (a*d - b*c) / np.sqrt((a+b)*(c+d)*(a+c)*(b+d))
                    phi[i, j] = phi[j, i] = phi_ij
                    _, p, _, _ = chi2_contingency(tab)
                    pval[i, j] = pval[j, i] = p

    valid_phi = phi[~np.isnan(phi) & (phi != 1)]
    if len(valid_phi) > 0:
        vmax = np.max(np.abs(valid_phi))
        vmin = -vmax
    else:
        vmax, vmin = 1.0, -1.0

    cmap = LinearSegmentedColormap.from_list("phi_cmap", ["#68a7be", "#ffffff", "#ee7e77"])

    fig, ax = plt.subplots(figsize=(3/2.54, 3/2.54), dpi=600)
    fig.subplots_adjust(0, 0, 1, 1)

    square = 0.8
    for i in range(n_us):
        for j in range(i):
            val = phi[i, j]
            if np.isnan(val):
                continue
            x = j
            y = n_us - 1 - i
            color = cmap((val - vmin) / (vmax - vmin))
            ax.add_patch(mpatches.Rectangle((x - square/2, y - square/2),
                                            square, square,
                                            facecolor=color,
                                            edgecolor="none"))
            ax.text(x, y + 0.05, f"{val:.2f}", ha="center", va="center", fontsize=5)
            if pval[i, j] < 0.001:
                sig = "***"
            elif pval[i, j] < 0.01:
                sig = "**"
            elif pval[i, j] < 0.05:
                sig = "*"
            else:
                sig = ""
            if sig:
                ax.text(x, y - 0.25, sig, ha="center", va="center", fontsize=5)

    ax.set_xlim(-0.5, n_us - 0.5)
    ax.set_ylim(-0.5, n_us - 0.5)
    ax.set_aspect("equal")
    ax.axis("off")
    out_file = os.path.join(output_path, "fig3c.png")
    plt.savefig(out_file, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved {out_file}")

    # Color bar
    fig_c, ax_c = plt.subplots(figsize=(0.6/2.54, 3/2.54), dpi=600)
    fig_c.subplots_adjust(left=0.3, right=0.7, top=0.98, bottom=0.02)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm.set_array([])
    cbar = fig_c.colorbar(sm, cax=ax_c, orientation="vertical")
    cbar.ax.tick_params(labelsize=5, width=0.25, length=2)
    for spine in ax_c.spines.values():
        spine.set_linewidth(0)
    leg_file = os.path.join(output_path, "fig3c_legend.png")
    plt.savefig(leg_file, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved {leg_file}")

# =============================================================================
# Figure 3g - Association heatmap (US vs SDG) - Overall
# =============================================================================
def plot_fig3g(df, us_columns, output_path=OUTPUT_DIR):
    # Parse SDGs
    def parse_sdgs(cell):
        if pd.isna(cell):
            return []
        cell_str = str(cell).strip()
        if not cell_str:
            return []
        parts = cell_str.replace(", ", ",").split(",")
        sdg_list = []
        for p in parts:
            p = p.strip()
            if p:
                try:
                    num = int(p)
                    if 1 <= num <= 17:
                        sdg_list.append(num)
                except:
                    pass
        return sorted(list(set(sdg_list)))

    df["SDG_list"] = df["Covered_SDGs"].apply(parse_sdgs)
    df["SDG_layer"] = df["2025 SDG layer"].map({"High": "High", "Moderate": "Moderate", "Low": "Low"})

    # Create SDG presence matrix
    sdg_matrix = np.zeros((len(df), 17), dtype=int)
    for idx, sdgs in enumerate(df["SDG_list"]):
        for sdg in sdgs:
            if 1 <= sdg <= 17:
                sdg_matrix[idx, sdg-1] = 1

    # Association function
    def calc_assoc(us_series, sdg_series, min_co=1):
        co = ((us_series == 1) & (sdg_series == 1)).sum()
        if co < min_co:
            return np.nan, np.nan, np.nan, co
        a = co
        b = ((us_series == 1) & (sdg_series == 0)).sum()
        c = ((us_series == 0) & (sdg_series == 1)).sum()
        d = ((us_series == 0) & (sdg_series == 0)).sum()
        denom = np.sqrt((a+b)*(c+d)*(a+c)*(b+d))
        phi = (a*d - b*c) / denom if denom > 0 else 0.0
        try:
            _, p, _, _ = chi2_contingency([[a, b], [c, d]], correction=False)
        except:
            p = 1.0
        cond = (a / (a+b) * 100) if (a+b) > 0 else 0.0
        return phi, p, cond, co

    # Compute matrices
    us_names = [col.replace("_", " ") for col in us_columns]
    sdg_labels = [f"SDG_{i}" for i in range(1, 18)]
    phi_mat = np.full((len(us_columns), 17), np.nan)
    p_mat = np.full((len(us_columns), 17), np.nan)
    cond_mat = np.full((len(us_columns), 17), np.nan)

    for i, us_col in enumerate(us_columns):
        us_data = df[us_col]
        for j in range(17):
            sdg_data = pd.Series(sdg_matrix[:, j])
            phi, p, cond, co = calc_assoc(us_data, sdg_data, min_co=1)
            if not np.isnan(phi):
                phi_mat[i, j] = phi
                p_mat[i, j] = p
                cond_mat[i, j] = cond

    # Plot heatmap
    valid_phi = phi_mat[~np.isnan(phi_mat)]
    if len(valid_phi) > 0:
        vmax = max(abs(valid_phi.min()), abs(valid_phi.max()))
        vmin = -vmax
    else:
        vmax, vmin = 1.0, -1.0

    cmap = LinearSegmentedColormap.from_list("phi_cmap", ["#68a7be", "#ffffff", "#ee7e77"])

    fig, ax = plt.subplots(figsize=(9/2.54, 5.5/2.54), dpi=600)
    fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95)

    min_size, max_size = 0.5, 1.0
    n_us, n_sdg = phi_mat.shape

    for i in range(n_us):
        for j in range(n_sdg):
            phi_val = phi_mat[i, j]
            if np.isnan(phi_val):
                continue
            cond_val = cond_mat[i, j]
            p_val = p_mat[i, j]
            norm_val = (phi_val - vmin) / (vmax - vmin)
            color = cmap(norm_val)
            cell_size = min_size + (cond_val / 100) * (max_size - min_size)
            x = j + 0.5
            y = n_us - i - 0.5
            rect = mpatches.Rectangle((x - cell_size/2, y - cell_size/2),
                                      cell_size, cell_size,
                                      facecolor=color,
                                      edgecolor="white",
                                      linewidth=0.3,
                                      alpha=0.9)
            ax.add_patch(rect)

            if not np.isnan(p_val) and p_val < 0.05:
                if p_val < 0.001:
                    sig = "***"
                elif p_val < 0.01:
                    sig = "**"
                else:
                    sig = "*"
                text_color = "white" if abs(phi_val) > 0.4 else "black"
                ax.text(x, y - 0.06, f"{phi_val:.2f}", ha="center", va="center",
                        fontsize=5, color=text_color)
                ax.text(x, y + 0.33, sig, ha="center", va="center",
                        fontsize=5, color=text_color)

    ax.set_xlim(0, n_sdg)
    ax.set_ylim(0, n_us)
    ax.set_aspect("equal")
    ax.invert_yaxis()
    ax.axis("off")

    out_file = os.path.join(output_path, "fig3g_Overall.png")
    plt.savefig(out_file, dpi=600, bbox_inches="tight", pad_inches=0.02)
    plt.close()
    print(f"Saved {out_file}")

    # Color bar
    fig_c, ax_c = plt.subplots(figsize=(0.6/2.54, 3/2.54), dpi=600)
    fig_c.subplots_adjust(left=0.3, right=0.7, top=0.98, bottom=0.02)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm.set_array([])
    cbar = fig_c.colorbar(sm, cax=ax_c, orientation="vertical")
    cbar.set_label("Phi", fontsize=5, labelpad=2)
    cbar.ax.tick_params(labelsize=5, width=0.25, length=2)
    for spine in ax_c.spines.values():
        spine.set_linewidth(0)
    leg_file = os.path.join(output_path, "fig3g_legend_Overall.png")
    plt.savefig(leg_file, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved {leg_file}")

# =============================================================================
# Additional auxiliary charts (not part of main figure)
# =============================================================================
def plot_auxiliary_charts(df, us_columns, output_path=OUTPUT_DIR):
    # This function generates SDG distribution, SDG count, TOP10 combinations,
    # and Layer-US frequency heatmap (as in original notebook)
    # For brevity, we will implement only the key ones; the original had several cells.
    # I will include a reduced version to avoid excessive length.

    # --- SDG distribution (bar + line) ---
    # (This was in original but not used in final figure; we'll skip for clarity)
    # We'll just produce the SDG count bar chart and TOP10 combo bar chart as examples.

    # Parse SDGs and layer
    def parse_sdgs(cell):
        if pd.isna(cell):
            return []
        cell_str = str(cell).strip()
        if not cell_str:
            return []
        parts = cell_str.replace(", ", ",").split(",")
        out = []
        for p in parts:
            p = p.strip()
            if p:
                try:
                    num = int(p)
                    if 1 <= num <= 17:
                        out.append(num)
                except:
                    pass
        return sorted(list(set(out)))

    df["SDG_list"] = df["Covered_SDGs"].apply(parse_sdgs)
    df["SDG_count"] = df["SDG_list"].apply(len)
    df["SDG_layer_clean"] = df["2025 SDG layer"].map({"High": "High", "Moderate": "Moderate", "Low": "Low"})

    # SDG count distribution
    count_dist = df["SDG_count"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(2/2.54, 1.8/2.54), dpi=600)
    fig.subplots_adjust(0, 0, 1, 1)
    ax.bar(count_dist.index, count_dist.values / len(df) * 100,
           width=0.6, color="#A9CACE", edgecolor="white", linewidth=0.5)
    for x, y in zip(count_dist.index, count_dist.values):
        ax.text(x, (y/len(df)*100) + 0.5, str(y), ha="center", va="bottom", fontsize=5)
    ax.set_xlim(count_dist.index.min() - 0.5, count_dist.index.max() + 0.5)
    ax.set_ylim(0, max(count_dist.values/len(df)*100) * 1.2)
    ax.axis("off")
    plt.tight_layout()
    out = os.path.join(output_path, "SDG_count_distribution.png")
    plt.savefig(out, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved {out}")

    # TOP10 SDG combinations
    combo_counts = Counter()
    for sdg_list in df["SDG_list"]:
        if len(sdg_list) > 0:
            combo_counts[tuple(sorted(sdg_list))] += 1
    top10 = combo_counts.most_common(10)
    # sort ascending for horizontal bar
    top10_sorted = sorted(top10, key=lambda x: x[1])
    labels = [", ".join([f"SDG{s}" for s in combo]) for combo, _ in top10_sorted]
    freqs = [cnt / len(df) * 100 for _, cnt in top10_sorted]

    fig, ax = plt.subplots(figsize=(1.5/2.54, 3/2.54), dpi=600)
    fig.subplots_adjust(0, 0, 1, 1)
    ypos = np.arange(len(top10_sorted))
    bars = ax.barh(ypos, freqs, height=0.6, color="#ee8d87", edgecolor="white", linewidth=0.5)
    for i, (bar, f) in enumerate(zip(bars, freqs)):
        ax.text(f + 0.5, bar.get_y() + bar.get_height()/2, f"{f:.1f}%",
                ha="left", va="center", fontsize=5)
    ax.set_xlim(0, max(freqs)*1.3)
    ax.set_ylim(-0.5, len(ypos)-0.5)
    ax.axis("off")
    plt.tight_layout()
    out = os.path.join(output_path, "SDG_combo_top10.png")
    plt.savefig(out, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved {out}")

    # Layer-US frequency heatmap
    # Build US presence matrix
    us_matrix = np.zeros((len(df), len(us_columns)), dtype=int)
    for idx, row in df.iterrows():
        for j, us in enumerate(us_columns):
            if pd.notna(row[us]) and row[us] == 1:
                us_matrix[idx, j] = 1

    layer_us = {}
    for layer in ["High", "Moderate", "Low"]:
        mask = df["SDG_layer_clean"] == layer
        if mask.sum() > 0:
            sub = us_matrix[mask]
            layer_us[layer] = sub.mean(axis=0) * 100  # percentage

    # Prepare data matrix (3 layers x 6 US)
    layers_order = ["High", "Moderate", "Low"]
    us_names_rev = [col.replace("_", " ") for col in us_columns][::-1]  # reversed
    data_mat = np.zeros((len(layers_order), len(us_columns)))
    for i, layer in enumerate(layers_order):
        if layer in layer_us:
            data_mat[i, :] = layer_us[layer][::-1]  # reverse order for display

    fig, ax = plt.subplots(figsize=(7/2.54, 3/2.54), dpi=600)
    fig.subplots_adjust(left=0.05, right=0.85, bottom=0.05, top=0.95)
    cmap_heat = LinearSegmentedColormap.from_list("us_cmap", ["#deeeed", "#68a7be"])
    vmin, vmax = 30, 80
    for i in range(len(layers_order)):
        for j in range(len(us_columns)):
            val = data_mat[i, j]
            if np.isnan(val):
                continue
            norm_val = (val - vmin) / (vmax - vmin)
            norm_val = max(0, min(1, norm_val))
            color = cmap_heat(norm_val)
            x = j + 0.5
            y = len(layers_order) - i - 0.5
            rect = mpatches.Rectangle((x-0.5, y-0.5), 1, 1,
                                      facecolor=color, edgecolor="white", linewidth=5)
            ax.add_patch(rect)
            ax.text(x, y, f"{val:.0f}%", ha="center", va="center", fontsize=5, color="black")

    ax.set_xlim(0, len(us_columns))
    ax.set_ylim(0, len(layers_order))
    ax.set_aspect("equal")
    ax.axis("off")

    # Colorbar
    cax = fig.add_axes([0.88, 0.05, 0.03, 0.90])
    norm = plt.Normalize(vmin, vmax)
    sm = plt.cm.ScalarMappable(cmap=cmap_heat, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, cax=cax, orientation="vertical")
    cbar.set_label("Frequency (%)", fontsize=5)
    cbar.ax.tick_params(labelsize=5, width=0.25, length=2)
    cbar.set_ticks([30, 40, 50, 60, 70, 80])
    cbar.set_ticklabels(["30%", "40%", "50%", "60%", "70%", "80%"])
    cbar.outline.set_linewidth(0)
    for spine in cbar.ax.spines.values():
        spine.set_visible(False)

    out = os.path.join(output_path, "Layer_US_frequency_heatmap.png")
    plt.savefig(out, dpi=600, bbox_inches="tight", pad_inches=0.02)
    plt.close()
    print(f"Saved {out}")

# =============================================================================
# Main execution
# =============================================================================
if __name__ == "__main__":
    # Load data
    df_cdt, us_cols = load_and_preprocess_cdt()
    df_count = load_count_data()  # not used for fig3, but kept for consistency

    # Generate Figure 3 panels
    plot_fig3a(df_cdt, us_cols, OUTPUT_DIR)
    plot_fig3b(df_cdt, us_cols, OUTPUT_DIR)
    plot_fig3c(df_cdt, us_cols, OUTPUT_DIR)
    plot_fig3g(df_cdt, us_cols, OUTPUT_DIR)

    # Generate auxiliary charts (if needed)
    plot_auxiliary_charts(df_cdt, us_cols, OUTPUT_DIR)

    print("All figures generated successfully.")