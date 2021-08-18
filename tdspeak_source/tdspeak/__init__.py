from django.db.backends.signals import connection_created
def activate_foreign_keys(sender, connection, **kwargs):
    """Enable integrity constraint with sqlite."""
    if connection.vendor == 'sqlite':
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON; PRAGMA synchronous = NORMAL; PRAGMA journal_mode = WAL;')

connection_created.connect(activate_foreign_keys)
