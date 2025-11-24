import sys

def load_chrom_order(sel_path):
    """
    Read chromosome names (one per line) from a file
    and return them as a list, skipping blank lines.
    """
    chrom_list = []
    with open(sel_path, "r") as fh:
        for raw in fh:
            name = raw.strip()
            if not name:      # skip empty or whitespace-only lines
                continue
            chrom_list.append(name)
    return chrom_list


def main():
    # Decide which selection file to use
    sel_path = sys.argv[1] if len(sys.argv) >= 2 else "standard_selection.tsv"

    # Read desired chromosome order
    chrom_order = load_chrom_order(sel_path)

    # Prepare a bucket for each chromosome
    per_chrom = {chrom: [] for chrom in chrom_order}

    # Read BED-like lines from stdin
    for raw_line in sys.stdin:
        stripped = raw_line.strip()
        if not stripped:
            continue  # ignore blank lines

        fields = stripped.split("\t")
        if len(fields) < 3:
            continue  # not a valid BED-like line

        chrom = fields[0]
        if chrom not in per_chrom:
            continue  # chromosome not in our selection/order

        # Parse start coordinate; skip if non-numeric
        try:
            start_val = int(fields[1])
        except ValueError:
            continue

        # Keep original line (with its newline) together with start coordinate
        per_chrom[chrom].append((start_val, raw_line))

    out = sys.stdout

    # Emit lines in the requested chromosome order and sorted by start
    for chrom in chrom_order:
        entries = per_chrom[chrom]
        entries.sort(key=lambda item: item[0])
        for _, line in entries:
            out.write(line)


if __name__ == "__main__":
    main()