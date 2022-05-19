"""
Simple Graph template I can reuse....
author: Jackson Walker
"""
import matplotlib.pyplot as plt


def auto_label(axis, rectangle_group):
    for rect in rectangle_group:     # Want to get the height of each bar.
        height = rect.get_height()
        # " xy=(...), ha='center' " <-- ensures that the numbers will be perfectly centered for each bar.
        axis.annotate(str(height),
                      xy=(rect.get_x() + rect.get_width() / 2, height),
                      ha='center',
                      xytext=(0, 3), textcoords='offset points',    # xytext=(0, 3) puts all text at set position.
                      color='gray')     # textcoords='offset points' ^^<-- Takes this xytext and offsets the text by that set amount instead.\


def graph():
    # X-AXIS'
    phases = ['Mid 90s', 'Early 2k', 'Mid 2k', 'Mid 2010s']
    playstation = [102, 155, 87, 110]
    xbox = [0, 24, 86, 50]
    nintendo = [33, 22, 102, 62]

    # Y-AXIS
    pc_sales = [71, 128, 240, 316]

    width = 0.2  # Width of each of the bars in bar graph
    x_playstation = [x - width for x in range(len(playstation))]  # Look at all entries of playstation and subtract our width so the bars are aligned correctly. Creates the OFFSET for each bar...
    x_xbox = [x for x in range(len(xbox))]    # xbox is in the middle so no need to subtract width.. <--- and ^^ both list comprehension!
    x_nintendo = [x + width for x in range(len(nintendo))]

    fig, ax = plt.subplots()    # Show both plots fig = graph, ax = axis that actually holds the data
    # NOTE: You can create multiple graphs on top of the same axis'

    # When matplotlib creates a bar it creates a value we can store in a variable in this case rect1-rect#....
    # These variables rect1-rect3 are groups of bars. Each of these rect variables stores 4 bars.
    rect1 = ax.bar(x_playstation, playstation, width, label="Playstation", color='darkslategray')    # Create bar chart
    rect2 = ax.bar(x_xbox, xbox, width, label="Xbox", color='limegreen')
    rect3 = ax.bar(x_nintendo, nintendo, width, label="nintendo", color='crimson')

    ax.plot(phases, pc_sales, label="PC Sales", color='black', marker='o')   # Creates the line plot, MARKER ADDS POINTS TO LINE!

    ax.set_title("The hardware market")
    ax.set_ylabel("Total sales (in millions)")
    ax.legend()     # Creates legend for labeling the different elements of the graph/plot

    auto_label(ax, rect1)
    auto_label(ax, rect2)
    auto_label(ax, rect3)

    plt.show()
	

if __name__ == '__main__':
	graph()