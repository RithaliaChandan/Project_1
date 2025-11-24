Project — BED Sorting by Custom Chromosome Order

Author: Chandan Rithalia
Date: 24/11/2025

1. Objective
   To sort BED/BED-like genomic intervals using a user-provided chromosome order, and then sort entries within each chromosome by start coordinate. This ensures consistent genome ordering across tools and pipelines.

2. Steps

   2.1 Load chromosome order file
       - Read chromosome names line-by-line.
       - Ignore empty entries.

   2.2 Choose selection file
       - Use file passed in argv or default to standard_selection.tsv.

   2.3 Create chromosome buckets
       - A dictionary mapping each chromosome to a list of its BED lines.

   2.4 Read BED from stdin
       - Skip blank/malformed lines.
       - Accept lines only if chromosome exists in the selection file.

   2.5 Extract start coordinate
       - Convert column 2 to integer.
       - Store tuple (start, original_line) for sorting.

   2.6 Sort & output
       - For each chromosome (in the exact user order):
         * Sort entries by numeric start.
         * Print original lines.

3. Scripts Used
   - load_chrom_order() — loads chromosome order
   - main() — reads stdin, groups, sorts, outputs BED lines

4. Input
   - Chromosome order file — one chromosome name per line
   - BED data via stdin — minimum 3 columns: chrom, start, end

5. Output
   - Sorted BED lines on stdout
   - Ordered by chromosome (user-defined)
   - Sorted by start coordinate inside each chromosome

6. Conclusion
   This script provides a solution for arranging BED data   using a custom chromosome order, keeping genomic intervals clean, consistent,and ready for downstream analysis or visualization.
