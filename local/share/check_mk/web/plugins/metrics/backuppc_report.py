## BackupPC Host Summary Statistic 
# define metrics colot/unit
metric_info['total_host_count'] = {
    'title': _('Total hosts'),
    'unit': 'count',
    'help': _('Total number of hosts with backup'),
    'color': indexed_color(4,4),
}

metric_info['total_disabled_count'] = {
    'title': _('Disabled hosts'),
    'unit': 'count',
    'help': _('Number of hosts with disabled backup'),
    'color': indexed_color(1,4),
}

metric_info['total_tooold_count'] = {
    'title': _('Hosts with too old Backup'),
    'unit': 'count',
    'help': _('Number of hosts with too old backups'),
    'color': indexed_color(2,4),
}

metric_info['total_progress_count'] = {
    'title': _('Host in progress'),
    'unit': 'count',
    'help': _('Number of hosts with backup in progress'),
    'color': indexed_color(3,4),
}


# define graph
graph_info.append({
   'title': _('BackupPC Hosts Summary'),
   'metrics': [
       ( 'total_tooold_count',      'stack'),
       ( 'total_disabled_count',    'stack'),
       ( 'total_progress_count',    'stack'),
       ( 'total_host_count',        'line'),
   ],
})


## BackupPC Backup Summary
# define metrics colot/unit
metric_info['total_backup_count'] = {
    'title': _('Total backups'),
    'unit': 'count',
    'help': _('Total number of backups'),
    'color': indexed_color(1,3),
}

metric_info['total_error_count'] = {
    'title': _('Total errors'),
    'unit': 'count',
    'help': _('Total number of erroneous backups'),
    'color': indexed_color(2,3),
}

metric_info['total_partial_count'] = {
    'title': _('Total partial backups'),
    'unit': 'count',
    'help': _('Total number of partial backups'),
    'color': indexed_color(3,3),
}


# define graph
graph_info.append({
    'title': _('BackupPC Backup Summary'),
    'metrics': [
        ( 'total_backup_count',     'area'),
        ( 'total_error_count' ,     'area'),
        ( 'total_partial_count',    'area'),
    ],
})
