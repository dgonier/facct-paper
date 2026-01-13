#!/usr/bin/env python3
"""Generate compact, publication-quality figures for FAccT paper."""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np

# Set publication-quality defaults
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'legend.fontsize': 7,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
})

# Data from tournament results (CORRECTED from classification_scores_data.csv)
categories = ['FOAM\n(Ours)', 'Human\nExperts', 'Zero-shot\nAI']
overall_scores = [73.5, 62.4, 46.3]
argumentation = [74.0, 67.4, 62.0]
evidence = [78.3, 51.4, 20.5]
coherence = [71.6, 62.3, 61.0]
innovation = [81.1, 74.6, 63.3]
viability = [65.8, 57.5, 35.9]

# Perfect validation rates
validation_rates = [76.2, 8.7, 0.0]

# Colors
colors = ['#2ecc71', '#3498db', '#e74c3c']  # green, blue, red


def fig1_main_results():
    """Bar chart of main tournament results - compact."""
    fig, ax = plt.subplots(figsize=(3.3, 2.0))

    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax.bar(x - width/2, overall_scores, width, label='Overall Score', color=colors, alpha=0.9)
    bars2 = ax.bar(x + width/2, evidence, width, label='Evidence Quality', color=colors, alpha=0.5, hatch='//')

    ax.set_ylabel('Score')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 100)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.0f}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 2), textcoords="offset points", ha='center', va='bottom', fontsize=6)

    plt.tight_layout()
    plt.savefig('main_results.png', dpi=300)
    plt.savefig('main_results.pdf')
    plt.close()
    print("Created main_results.png/pdf")


def fig2_validation_rates():
    """Bar chart of perfect validation rates - very compact."""
    fig, ax = plt.subplots(figsize=(2.5, 1.8))

    x = np.arange(len(categories))
    bars = ax.bar(x, validation_rates, color=colors, alpha=0.85)

    ax.set_ylabel('CFVR (%)')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 100)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 2), textcoords="offset points", ha='center', va='bottom', fontsize=7)

    plt.tight_layout()
    plt.savefig('validation_rates.png', dpi=300)
    plt.savefig('validation_rates.pdf')
    plt.close()
    print("Created validation_rates.png/pdf")


def fig3_radar_compact():
    """Compact radar chart of all dimensions."""
    categories_radar = ['Overall', 'Argument.', 'Evidence', 'Coherence', 'Innovation', 'Viability']

    foam_data = [73.5, 74.0, 78.3, 71.6, 81.1, 65.8]
    human_data = [62.4, 67.4, 51.4, 62.3, 74.6, 57.5]
    ai_data = [46.3, 62.0, 20.5, 61.0, 63.3, 35.9]

    # Close the radar
    foam_data += foam_data[:1]
    human_data += human_data[:1]
    ai_data += ai_data[:1]

    angles = np.linspace(0, 2 * np.pi, len(categories_radar), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(2.8, 2.8), subplot_kw=dict(polar=True))

    ax.fill(angles, foam_data, alpha=0.25, color='#2ecc71')
    ax.plot(angles, foam_data, 'o-', linewidth=1.5, color='#2ecc71', label='FOAM', markersize=3)

    ax.fill(angles, human_data, alpha=0.15, color='#3498db')
    ax.plot(angles, human_data, 's--', linewidth=1, color='#3498db', label='Human', markersize=2)

    ax.fill(angles, ai_data, alpha=0.1, color='#e74c3c')
    ax.plot(angles, ai_data, '^:', linewidth=1, color='#e74c3c', label='Zero-shot', markersize=2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories_radar, size=6)
    ax.set_ylim(0, 100)
    ax.set_yticks([25, 50, 75])
    ax.set_yticklabels(['25', '50', '75'], size=5)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=6)

    plt.tight_layout()
    plt.savefig('radar_compact.png', dpi=300)
    plt.savefig('radar_compact.pdf')
    plt.close()
    print("Created radar_compact.png/pdf")


def fig4_combined():
    """Combined figure with results and validation side by side."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.5, 2.0))

    # Left: Main results
    x = np.arange(len(categories))
    width = 0.35

    bars1 = ax1.bar(x - width/2, overall_scores, width, label='Overall', color=colors, alpha=0.9)
    bars2 = ax1.bar(x + width/2, evidence, width, label='Evidence', color=colors, alpha=0.5, hatch='//')

    ax1.set_ylabel('Score')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)
    ax1.set_ylim(0, 100)
    ax1.legend(loc='upper right', framealpha=0.9, fontsize=6)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.set_title('(a) Tournament Scores', fontsize=8)

    for bar in bars1:
        height = bar.get_height()
        ax1.annotate(f'{height:.0f}', xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 1), textcoords="offset points", ha='center', va='bottom', fontsize=5)

    # Right: Validation rates
    bars = ax2.bar(x, validation_rates, color=colors, alpha=0.85)
    ax2.set_ylabel('Perfect Validation (%)')
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories)
    ax2.set_ylim(0, 100)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.set_title('(b) Evidence Verifiability', fontsize=8)

    for bar in bars:
        height = bar.get_height()
        label = f'{height:.1f}%' if height > 0 else '0%'
        ax2.annotate(label, xy=(bar.get_x() + bar.get_width()/2, max(height, 3)),
                    xytext=(0, 1), textcoords="offset points", ha='center', va='bottom', fontsize=6)

    plt.tight_layout()
    plt.savefig('combined_results.png', dpi=300)
    plt.savefig('combined_results.pdf')
    plt.close()
    print("Created combined_results.png/pdf")


if __name__ == '__main__':
    fig1_main_results()
    fig2_validation_rates()
    fig3_radar_compact()
    fig4_combined()
    print("\nAll figures generated successfully!")
