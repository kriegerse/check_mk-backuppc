# define metrics colot/unit
metric_info['total_host_count'] = {
    'title': _('Total hosts'),
    'unit': 'count',
    'help': _('Total number of hosts with backup'),
    'color': '33/a',
}

metric_info['total_disabled_count'] = {
    'title': _('Disabled hosts'),
    'unit': 'count',
    'help': _('Number of hosts with disabled backup'),
    'color': '44/a',
}

metric_info['total_tooold_count'] = {
    'title': _('Hosts with too old Backup'),
    'unit': 'count',
    'help': _('Number of hosts with too old backups'),
    'color': '14/a',
}


# define graphs
# BackupPC Host Summary Statistic 
graph_info.append({
   'title': _('BackupPC Hosts Summary'),
   'metrics': [
       ( 'total_host_count',        'area'),
       ( 'total_disabled_count',    'line'),
       ( 'total_tooold_count',      'line'),
   ],
})
