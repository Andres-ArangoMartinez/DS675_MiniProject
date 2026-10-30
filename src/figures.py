"""Regenerate the report's descriptive figures using portable Matplotlib fonts."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.patches import Patch, FancyBboxPatch

NAVY = '#12324A'
TEAL = '#16697A'
GOLD = '#E9A23B'


def style():
    plt.rcParams.update({
        'font.family': 'DejaVu Serif', 'font.size': 9, 'text.color': NAVY,
        'axes.labelcolor': NAVY, 'xtick.color': NAVY, 'ytick.color': NAVY,
        'axes.spines.top': False, 'axes.spines.right': False,
    })


def save(fig, folder, name):
    for extension in ['png', 'svg']:
        target = folder / f'{name}.{extension}'
        fig.savefig(target, dpi=240, facecolor='white')
        if extension == 'svg':
            target.write_text(target.read_text(encoding='utf-8'), encoding='utf-8', newline='\n')
    plt.close(fig)


def daily_profiles(x, folder):
    style()
    fig = plt.figure(figsize=(10.4, 3.68))
    bottom, top, gap = .13, .87, .085
    span = top - bottom
    left_height = (span - gap) / 2
    right_height = (span - 2 * gap) / 3
    axes = {
        'T1': fig.add_axes([.075, top-left_height, .365, left_height]),
        'PUMP_1': fig.add_axes([.075, bottom, .365, left_height]),
        'n1': fig.add_axes([.60, top-right_height, .365, right_height]),
        'n4': fig.add_axes([.60, top-2*right_height-gap, .365, right_height]),
        'n31': fig.add_axes([.60, bottom, .365, right_height]),
    }
    palette = [TEAL, '#2A9D8F', GOLD, NAVY]
    for name, ax in axes.items():
        daily = x[[name]].assign(day=x.index.date, slot=x.index.hour*12+x.index.minute//5)
        matrix = daily.pivot(index='day', columns='slot', values=name)
        assert matrix.shape == (273, 288) and not matrix.isna().any().any()
        hours = np.arange(288) / 12
        for number, row in enumerate(matrix.to_numpy()):
            ax.plot(hours, row, color=palette[number % 4], alpha=.14, lw=.35)
        ax.plot(hours, matrix.mean(axis=0), color='#A81738', lw=1.7)
        ax.set_xlim(0, 24)
        ax.set_xticks([0, 6, 12, 18, 24], ['00:00', '06:00', '12:00', '18:00', '24:00'])
        ax.tick_params(labelsize=8, pad=2, length=2.3)
        ax.grid(alpha=.16)
        ax.margins(y=.08)
        label = 'T1 level (m)' if name == 'T1' else 'PUMP_1 (m$^3$/h)' if name == 'PUMP_1' else name+' (m)'
        ax.set_ylabel(label, fontsize=9, labelpad=4)
        if name == 'PUMP_1':
            ax.set_ylim(bottom=0)
        if name in ['PUMP_1', 'n31']:
            ax.set_xlabel('Time of day (hh:mm)', fontsize=9, labelpad=3)
        else:
            ax.tick_params(axis='x', labelbottom=False)
    fig.legend([plt.Line2D([0], [0], color='#A81738', lw=1.7)],
               ['Clock-time mean; thin lines = 273 observed days'], loc='upper center',
               bbox_to_anchor=(.53, 1.005), frameon=False, fontsize=10)
    save(fig, folder, 'figure2_daily_profiles')


def correlations(corr, folder):
    style()
    fig = plt.figure(figsize=(8.9, 3.12))
    ax = fig.add_axes([.29, .19, .47, .77])
    cmap = colors.LinearSegmentedColormap.from_list('correlations', [NAVY, '#EDF5F7', '#2A9D8F'])
    im = ax.imshow(corr, vmin=-1, vmax=1, cmap=cmap, aspect='equal')
    labels = ['n1', 'n4', 'n31', 'T1', 'PUMP_1', 'AMR_n1', 'n1 +15']
    ax.set_xticks(range(7), labels, fontsize=10, rotation=32, ha='right')
    ax.set_yticks(range(7), labels, fontsize=10)
    ax.tick_params(length=0, pad=4)
    for i in range(7):
        for j in range(7):
            value = corr.iloc[i, j]
            ax.text(j, i, f'{value:.2f}', ha='center', va='center', fontsize=8.5,
                    color='white' if abs(value) > .68 else NAVY)
    ax.axhline(5.5, color=GOLD, lw=1.5)
    ax.axvline(5.5, color=GOLD, lw=1.5)
    cax = fig.add_axes([.705, .26, .014, .59])
    fig.colorbar(im, cax=cax, ticks=[-1, -.5, 0, .5, 1], label='Pearson r')
    cax.tick_params(labelsize=9)
    save(fig, folder, 'figure3_correlations')


def screening(summary, folder):
    style()
    rows = summary['categories']
    fig = plt.figure(figsize=(7.18, 1.40), facecolor='white')
    ax = fig.add_axes([.065, .29, .92, .40])
    positions = list(range(len(rows)))
    ax.set_axisbelow(True)
    ax.grid(axis='y', color='#E4EBEE', linewidth=.5)
    ax.bar(positions, [row['groups'] for row in rows], width=.62, color=TEAL)
    ax.bar(positions, [row['selected'] for row in rows], width=.24, color=GOLD)
    labels = ['Leaks /\nlocalization', 'Current-state\nestimation', 'Pressure/head\nforecasting',
              'Anomalies /\nsensor faults', 'Sensor\nplacement']
    ax.set_xticks(positions, [label+'\n'+str(row['selected'])+' selected' for label, row in zip(labels, rows)])
    ax.tick_params(axis='x', length=0, pad=2, labelsize=7.7)
    ax.set_yticks([0, 15, 30])
    ax.tick_params(axis='y', length=0, pad=3, labelsize=7.4)
    ax.set_ylabel('Groups', fontsize=7.7, labelpad=3)
    ax.set_ylim(0, max(row['groups'] for row in rows)+8)
    ax.set_xlim(-.65, len(rows)-.35)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for position, row in zip(positions, rows):
        ax.text(position, row['groups']+1, f"{row['groups']} ({row['percent']:.1f}%)",
                ha='center', va='bottom', fontsize=8, color=NAVY)
    total = summary['groups']
    fig.text(.005, .99, f'{total} groups of related works on L-Town', va='top',
             fontsize=9, fontweight='bold', color=NAVY)
    fig.legend(handles=[Patch(color=TEAL, label=f'Eligible groups (N={total})'),
                        Patch(color=GOLD, label=f"Selected for comparison (n={summary['selected_groups']})")],
               loc='upper left', bbox_to_anchor=(.06, .865), ncol=2, frameon=False,
               fontsize=8, handlelength=1.4, columnspacing=2, borderaxespad=0)
    save(fig, folder, 'figure4_historical_screening')



def supply_boundary(topology, folder):
    """Manual functional layout; all labeled model settings/connections are checked."""
    style()
    values = {r['id']: r['nominal_setting_m'] for r in topology['PRVs']}
    assert topology['sectors']['C']['pressure_sensors'] == ['n1', 'n4', 'n31']
    assert topology['sectors']['B']['pressure_sensors'] == ['n215']
    evidence = topology['supply_schematic_evidence']
    assert evidence['reservoirs'] == ['R1', 'R2']
    assert evidence['pumps'] == [{'id': 'PUMP_1', 'from': 'n54', 'to': 'T1'}]
    fig, ax = plt.subplots(figsize=(11.4, 3.45))
    fig.subplots_adjust(left=.01, right=.99, bottom=.02, top=.94)
    ax.set(xlim=(0, 11.5), ylim=(0, 3.25))
    ax.axis('off')
    def box(x, y, width, text):
        ax.add_patch(FancyBboxPatch((x, y), width, .58, boxstyle='round,pad=.03,rounding_size=.10', facecolor=NAVY, edgecolor='none'))
        ax.text(x + width/2, y+.29, text, ha='center', va='center', color='white', fontsize=10)
    def arrow(a, b):
        ax.annotate('', xy=b, xytext=a, arrowprops={'arrowstyle':'->', 'lw':1.4, 'color':'#7D8E95'})
    ax.add_patch(FancyBboxPatch((3.7,.28),7.65,1.17,boxstyle='round,pad=.10,rounding_size=.20',facecolor='#F1FAF8',edgecolor='#2A9D8F',lw=2))
    box(.12,2.03,1.35,'Reservoir R1')
    box(.12,1.11,1.35,'Reservoir R2')
    box(1.93,2.03,1.25,f"PRV-1\n{values['PRV-1']:g} m")
    box(1.93,1.11,1.25,f"PRV-2\n{values['PRV-2']:g} m")
    box(3.85,1.56,1.48,'Main network\nArea A')
    box(5.97,2.03,1.25,f"PRV-3\n{values['PRV-3']:g} m")
    box(7.83,2.03,3.15,'Sector B: n215\n1 pressure sensor')
    box(3.97,.56,1.68,'PUMP_1\nMeasured inflow')
    box(6.31,.56,1.52,'Tank T1\nMeasured level')
    box(8.45,.56,2.53,'Area C: n1 target\nn4 / n31 peers')
    for a,b in [((1.49,2.32),(1.91,2.32)),((1.49,1.40),(1.91,1.40)),((3.20,2.32),(3.83,1.98)),((3.20,1.40),(3.83,1.72)),((5.35,1.98),(5.95,2.32)),((7.24,2.32),(7.81,2.32)),((4.63,1.53),(4.63,1.16)),((5.67,.85),(6.29,.85)),((7.85,.85),(8.43,.85))]:arrow(a,b)
    ax.text(1.68,2.73,'p227 flow',color=TEAL,ha='center',fontsize=9)
    ax.text(1.68,.98,'p235 flow',color=TEAL,ha='center',fontsize=9)
    ax.text(8.12,1.30,'p239: no flow meter',color=TEAL,ha='center',fontsize=9)
    ax.text(7.58,.31,'Retained boundary measurements and local signals',color=TEAL,ha='center',fontsize=9)
    ax.text(.12,.77,'PRVs: nominal settings.\nRemote pressures are not fixed.\nInterpretive supply schematic.',ha='left',va='top',fontsize=9)
    ax.text(.10,3.08,'Hydraulic scope: retain the tank-fed branch',fontsize=13,color=NAVY)
    save(fig, folder, 'figure1_supply_boundary')
