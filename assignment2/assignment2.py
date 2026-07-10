def write_sorted_list():
    # Sort by the datetime object in tuple index 1
    sorted_minutes = sorted(minutes_list, key=lambda t: t[1])

    # Convert datetime objects back to strings
    converted = [
        (t[0], t[1].strftime('%B %d, %Y'))
        for t in sorted_minutes
    ]

    try:
        with open('./minutes.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(minutes1['fields'])  # header row
            for row in converted:
                writer.writerow(row)
    except Exception as e:
        print("Error writing minutes.csv:", e)
        raise

    return converted
