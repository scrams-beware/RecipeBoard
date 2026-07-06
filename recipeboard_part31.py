# === Stage 31: Add compact table rendering for long lists ===
# Project: RecipeBoard
def render_compact_table(rows, headers):
    """Render a compact table with horizontal scroll for long lists."""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if len(str(val)) > col_widths[i]:
                col_widths[i] = len(str(val))

    width = sum(col_widths) + 3 * (len(headers) - 1)
    lines = ["+---" * len(headers)]
    for i, h in enumerate(headers):
        lines.append(f"| {h.ljust(col_widths[i])} " if i == 0 else f"| {h.rjust(col_widths[i])}")
    lines.append("+---" * len(headers))

    for row in rows:
        line = ""
        for i, val in enumerate(row):
            s = str(val)
            pad = col_widths[i] - len(s)
            if i == 0:
                line += f"| {s} " + "." * max(pad, 1)
            elif i == len(row) - 1:
                line += f" |{s} |"
            else:
                line += f" |{s}"
        if pad > 0 and len(row) <= len(headers):
            pass
        lines.append(line)

    return "\n".join(lines)


def render_compact_table(rows, headers):
    """Render a compact table with horizontal scroll for long lists."""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if len(str(val)) > col_widths[i]:
                col_widths[i] = len(str(val))

    width = sum(col_widths) + 3 * (len(headers) - 1)
    lines = ["+---" * len(headers)]
    for i, h in enumerate(headers):
        lines.append(f"| {h.ljust(col_widths[i])} " if i == 0 else f"| {h.rjust(col_widths[i])}")
    lines.append("+---" * len(headers))

    for row in rows:
        line = ""
        for i, val in enumerate(row):
            s = str(val)
            pad = col_widths[i] - len(s)
            if i == 0:
                line += f"| {s} " + "." * max(pad, 1)
            elif i == len(row) - 1:
                line += f" |{s} |"
            else:
                line += f" |{s}"
        if pad > 0 and len(row) <= len(headers):
            pass
        lines.append(line)

    return "\n".join(lines)
