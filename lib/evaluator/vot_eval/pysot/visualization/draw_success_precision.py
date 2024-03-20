import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

from .draw_utils import COLOR, LINE_STYLE

# def draw_success_precision(success_ret, name, videos, attr, precision_ret=None,
#         norm_precision_ret=None, bold_name=None, axis=[0, 1]):
#     # success plot
#     fig, ax = plt.subplots()
#     ax.grid(b=True)
#     ax.set_aspect(1)
#     plt.xlabel('Overlap threshold')
#     plt.ylabel('Success rate')
#     if attr == 'ALL':
#         plt.title('Success plots of OPE on {}'.format(name))
#     else:
#         plt.title('Success plots of OPE on {}'.format(attr))
#     plt.axis([0, 1]+axis)
#     success = {}
#     thresholds = np.arange(0, 1.05, 0.05)
#     for tracker_name in success_ret.keys():
#         value = [v for k, v in success_ret[tracker_name].items() if k in videos]
#         success[tracker_name] = np.mean(value)
#     for idx, (tracker_name, auc) in  \
#             enumerate(sorted(success.items(), key=lambda x:x[1], reverse=True)):
#         if tracker_name == bold_name:
#             label = "[{:.3f}] {}".format(auc, tracker_name)
#         else:
#             label = "[{:.3f}] {}".format(auc, tracker_name)
#         value = [v for k, v in success_ret[tracker_name].items() if k in videos]
#         plt.plot(thresholds, np.mean(value, axis=0),
#                 color=COLOR[idx], linestyle=LINE_STYLE[idx],label=label, linewidth=2)
#     ax.legend(loc='lower left', labelspacing=0.2)
#     ax.autoscale(enable=True, axis='both', tight=True)
#     xmin, xmax, ymin, ymax = plt.axis()
#     ax.autoscale(enable=False)
#     ymax += 0.03
#     ymin = 0
#     plt.axis([xmin, xmax, ymin, ymax])
#     plt.xticks(np.arange(xmin, xmax+0.01, 0.1))
#     plt.yticks(np.arange(ymin, ymax, 0.1))
#     ax.set_aspect((xmax - xmin)/(ymax-ymin))
#     #plt.savefig(storage_path + 'success.png')
#     plt.show()

#     if precision_ret:
#         # norm precision plot
#         fig, ax = plt.subplots()
#         ax.grid(b=True)
#         ax.set_aspect(50)
#         plt.xlabel('Location error threshold')
#         plt.ylabel('Precision')
#         if attr == 'ALL':
#             plt.title('Precision plots of OPE on {}'.format(name))
#         else:
#             plt.title('Precision plots of OPE on {}'.format(attr))
#         plt.axis([0, 50]+axis)
#         precision = {}
#         thresholds = np.arange(0, 51, 1)
#         for tracker_name in precision_ret.keys():
#             value = [v for k, v in precision_ret[tracker_name].items() if k in videos]
#             precision[tracker_name] = np.mean(value, axis=0)[20]
#         for idx, (tracker_name, pre) in \
#                 enumerate(sorted(precision.items(), key=lambda x:x[1], reverse=True)):
#             if tracker_name == bold_name:
#                 label = "[%.3f] " % (pre) + tracker_name
#             else:
#                 label = "[%.3f] " % (pre) + tracker_name
#             value = [v for k, v in precision_ret[tracker_name].items() if k in videos]
#             plt.plot(thresholds, np.mean(value, axis=0),
#                     color=COLOR[idx], linestyle=LINE_STYLE[idx],label=label, linewidth=2)
#         ax.legend(loc='lower right', labelspacing=0.2)
#         ax.autoscale(enable=True, axis='both', tight=True)
#         xmin, xmax, ymin, ymax = plt.axis()
#         ax.autoscale(enable=False)
#         ymax += 0.03
#         ymin = 0
#         plt.axis([xmin, xmax, ymin, ymax])
#         plt.xticks(np.arange(xmin, xmax+0.01, 5))
#         plt.yticks(np.arange(ymin, ymax, 0.1))
#         ax.set_aspect((xmax - xmin)/(ymax-ymin))
#         plt.savefig(storage_path + 'precision.png')

#     # norm precision plot
#     if norm_precision_ret:
#         fig, ax = plt.subplots()
#         ax.grid(b=True)
#         plt.xlabel('Location error threshold')
#         plt.ylabel('Precision')
#         if attr == 'ALL':
#             plt.title('Normalized Precision plots of OPE - {}'.format(name))
#         else:
#             plt.title('Normalized Precision plots of OPE - {}'.format(attr))
#         norm_precision = {}
#         thresholds = np.arange(0, 51, 1) / 100
#         for tracker_name in precision_ret.keys():
#             value = [v for k, v in norm_precision_ret[tracker_name].items() if k in videos]
#             norm_precision[tracker_name] = np.mean(value, axis=0)[20]
#         for idx, (tracker_name, pre) in \
#                 enumerate(sorted(norm_precision.items(), key=lambda x:x[1], reverse=True)):
#             if tracker_name == bold_name:
#                 label = "[%.3f] " % (pre) + tracker_name
#             else:
#                 label = "[%.3f] " % (pre) + tracker_name
#             value = [v for k, v in norm_precision_ret[tracker_name].items() if k in videos]
#             plt.plot(thresholds, np.mean(value, axis=0),
#                     color=COLOR[idx], linestyle=LINE_STYLE[idx],label=label, linewidth=2)
#         ax.legend(loc='lower right', labelspacing=0.2)
#         ax.autoscale(enable=True, axis='both', tight=True)
#         xmin, xmax, ymin, ymax = plt.axis()
#         ax.autoscale(enable=False)
#         ymax += 0.03
#         ymin = 0
#         plt.axis([xmin, xmax, ymin, ymax])
#         plt.xticks(np.arange(xmin, xmax+0.01, 0.05))
#         plt.yticks(np.arange(ymin, ymax, 0.1))
#         ax.set_aspect((xmax - xmin)/(ymax-ymin))
#         plt.savefig(storage_path + 'norm_precision.png')

def draw_success_precision(success_ret, name, videos, attr, precision_ret=None,
                                          norm_precision_ret=None, bold_name=None, axis=[0, 1]):

    success_file="./figs/success_plot" + " - {}".format(name) + ".png"
    thresholds = np.arange(0, 1.05, 0.05)
    
    # Success plot
    fig_success = go.Figure()
    for tracker_name, values in success_ret.items():
        filtered_values = [v for k, v in values.items() if k in videos]
        success_rate = np.mean(filtered_values, axis=0)
        fig_success.add_trace(go.Scatter(x=thresholds, y=success_rate,
                                         mode='lines',
                                         name=f"{tracker_name} AUC: {np.mean(success_rate):.3f}",
                                         line=dict(width=2)))
    fig_success.update_layout(title=f"Success Rate on {attr if attr != 'ALL' else name}",
                              xaxis_title='Overlap threshold',
                              yaxis_title='Success rate',
                              legend=dict(title="Trackers"),
                              width=800, height=600)
    pio.write_image(fig_success, success_file)
    
    # Precision plot
    precision_file="./figs/precision_plot" + " - {}".format(name) + ".png"
    fig_precision = go.Figure()
    for tracker_name, values in precision_ret.items():
        filtered_values = [v for k, v in values.items() if k in videos]
        precision_rate = np.mean(filtered_values, axis=0)
        fig_precision.add_trace(go.Scatter(x=thresholds, y=precision_rate,
                                           mode='lines',
                                           name=f"{tracker_name} AUC: {np.mean(precision_rate):.3f}",
                                           line=dict(width=2)))
    fig_precision.update_layout(title=f"Precision Rate on {attr if attr != 'ALL' else name}",
                                xaxis_title='Overlap threshold',
                                yaxis_title='Precision rate',
                                legend=dict(title="Trackers"),
                                width=800, height=600)
    pio.write_image(fig_precision, precision_file)
