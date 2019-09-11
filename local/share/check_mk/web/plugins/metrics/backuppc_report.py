## BackupPC Host Summary Statistic 
# define metrics colot/unit
metric_info['hosts'] = {
    'title': _('Hosts'),
    'unit': 'count',
    'help': _('Total number of hosts with backup'),
    'color': indexed_color(4,4),
}

metric_info['hosts_disabled'] = {
    'title': _('Hosts disabled'),
    'unit': 'count',
    'help': _('Number of hosts with disabled backup'),
    'color': indexed_color(1,4),
}

metric_info['hosts_overage'] = {
    'title': _('Hosts overaged'),
    'unit': 'count',
    'help': _('Number of hosts with too old backups'),
    'color': indexed_color(2,4),
}

metric_info['hosts_progress'] = {
    'title': _('Hosts in progress'),
    'unit': 'count',
    'help': _('Number of hosts with backup in progress'),
    'color': indexed_color(3,4),
}


# define graph
graph_info.append({
   'title': _('BackupPC Host Summary'),
   'metrics': [
       ( 'hosts_overage',      'stack'),
       ( 'hosts_disabled',    'stack'),
       ( 'hosts_progress',    'stack'),
       ( 'hosts',        'line'),
   ],
})


## BackupPC Backup Summary
# define metrics colot/unit
metric_info['bkp_count'] = {
    'title': _('Total backups'),
    'unit': 'count',
    'help': _('Total number of backups'),
    'color': indexed_color(1,3),
}

metric_info['bkp_errors'] = {
    'title': _('Total errors'),
    'unit': 'count',
    'help': _('Total number of erroneous backups'),
    'color': indexed_color(2,3),
}

metric_info['bkp_partial'] = {
    'title': _('Total partial'),
    'unit': 'count',
    'help': _('Total number of partial backups'),
    'color': indexed_color(3,3),
}


# define graph
graph_info.append({
    'title': _('BackupPC Backup Summary'),
    'metrics': [
        ( 'bkp_count',     'area'),
        ( 'bkp_errors' ,     'area'),
        ( 'bkp_partial',    'area'),
    ],
})
