import pandas as pd
from functools import reduce
from collections import Counter
import matplotlib.pyplot as plt


def plot_bar_graph(names, counts, output_file):
    # Plotting
    plt.figure(figsize=(10, 6), constrained_layout=True)
    bars = plt.bar(names, counts, color="skyblue", edgecolor="black")
    plt.xticks(names, rotation=-45, ha="left")
    plt.tick_params(axis="both", labelsize=10)

    # Adding value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.annotate(
            f"{height}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),  # offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    # Labels and title
    plt.xlabel("Patterns of logic structure", fontsize=10)
    plt.ylabel("CA Counts", fontsize=10)
    # plt.title("")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # plt.constrained_layout()
    # plt.show()
    plt.savefig(output_file, dpi=600)


def main():
    df = pd.read_json("dataset/all_agg_ptns.jsonl", lines=True)
    all_ptns = reduce(lambda x, y: x + y, df.ptns.values)
    counter = Counter(all_ptns)
    counter = sorted(dict(counter).items())
    ptn_names = {
        1: "Mitigation",
        2: "Alternative",
        3: "No evidence",
        4: "Another true cause",
        5: "Missing mechanism #1",
        6: "Missing mechanism #2",
        7: "No need to address",
        8: "Negative effect due to y",
        9: "Positive effects of a \ndifferent perspective from y #1",
        10: "Positive effects of a \ndifferent perspective from y #2",
    }
    # breakpoint()
    names = [ptn_names[item[0]] for item in counter]
    counts = [item[1] for item in counter]
    plot_bar_graph(
        names=names,
        counts=counts,
        output_file="./ptn_dist.pdf",
    )


if __name__ == "__main__":
    main()
