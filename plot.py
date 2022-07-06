import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.ticker as mticker
import pandas as pd

def get_labels(ticks_loc, x_axis):
    ticks_loc = [int(x) for x in ticks_loc]

    label_array = [] 
    for i in range(len(ticks_loc)):
        try:
            label_array.append(x_axis[ticks_loc[i]])
        except:
            label_array.append('Index is out of bounds')

    return label_array


def show_finance(x_label, y_label_1, y_label_2, x_axis, y_axis_1, x_axis_2, y_axis_2, lines=None):
    fig=plt.figure()
    ax=fig.add_subplot(111, label="1")
    ax2=fig.add_subplot(111, label="2", frame_on=False)

    ax.plot(x_axis, y_axis_1, color="C2")
    ax.set_xlabel(x_label, color="C0")
    ax.set_ylabel(y_label_1, color="C2")
    ax.tick_params(axis='x', colors="C0")
    ax.tick_params(axis='y', colors="C2")

    ax.xaxis.set_major_locator(mticker.MaxNLocator(4))
    ticks_loc = ax.get_xticks().tolist()
    ax.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
    labels = get_labels(ticks_loc, x_axis)
    ax.set_xticklabels(labels)



    ax2.scatter(x_axis_2, y_axis_2, color="C3")
    ax2.axes.get_xaxis().set_visible(False)
    ax2.yaxis.tick_right()
    ax2.set_ylabel(y_label_2, color="C3")
    ax2.yaxis.set_label_position('right')
    ax2.tick_params(axis='y', colors="C3")

    if lines is not None:
        for line in lines:
            plt.axvline(x=line)

    save_file = './results/' + 'thesis_1'
    plt.savefig(save_file)


def show_correlation(x_label, y_label, x_axis, y_axis):
    fig=plt.figure()
    ax=fig.add_subplot(111, label="1")

    ax.scatter(x_axis, y_axis, color="C2")
    ax.set_xlabel(x_label, color="C0")
    ax.set_ylabel(y_label, color="C2")
    ax.tick_params(axis='x', colors="C0")
    ax.tick_params(axis='y', colors="C2")

    save_file = './results/' + 'thesis_2'
    plt.savefig(save_file)







def show_correlation_2(x_label, y_label, y_label_2, x_axis_1, y_axis_1, x_axis_2, y_axis_2):
    fig=plt.figure()
    ax=fig.add_subplot(111, label="1")

    ax.scatter(x_axis_1, y_axis_1, color="C2")
    ax.set_xlabel(x_label, color="C0")
    ax.set_ylabel(y_label, color="C2")
    ax.tick_params(axis='x', colors="C0")
    ax.tick_params(axis='y', colors="C2")

    ax.xaxis.set_major_locator(mticker.MaxNLocator(4))
    ticks_loc = ax.get_xticks().tolist()
    ax.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
    labels = get_labels(ticks_loc, x_axis_1)
    ax.set_xticklabels(labels)

    save_file = './results/' + 'thesis_3a'
    plt.savefig(save_file)




    fig2=plt.figure()
    ax2=fig2.add_subplot(111, label="1")

    ax2.scatter(x_axis_2, y_axis_2, color="C2", s=4)
    ax2.set_xlabel(x_label, color="C0")
    ax2.set_ylabel(y_label_2, color="C2")
    ax2.tick_params(axis='x', colors="C0")
    ax2.tick_params(axis='y', colors="C2")

    ax2.xaxis.set_major_locator(mticker.MaxNLocator(4))
    ticks_loc = ax2.get_xticks().tolist()
    ax2.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
    labels = get_labels(ticks_loc, x_axis_2)
    ax2.set_xticklabels(labels)

    save_file = './results/' + 'thesis_3b'
    plt.savefig(save_file)
