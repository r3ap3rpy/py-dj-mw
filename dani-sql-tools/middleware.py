from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.sql import SqliteConsoleLexer
from sqlparse import format
from django.db import connection
from django.conf import settings
from decimal import Decimal

def new_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        total_execution_time = Decimal()
        check_duplicates = set()
        if settings.DEBUG:
            num_queries = len(connection.queries)
            for qs in connection.queries:
                total_execution_time += Decimal(qs["time"])
                check_duplicates.add(qs["sql"])
                sqlformatted = format(str(qs["sql"]),reindent = True)
                print(highlight(sqlformatted,SqliteConsoleLexer(),TerminalFormatter()))
        print("#" * 20)
        print("[SQL Stats]")
        print(f"Total queries: {num_queries}")
        print(f"Duplicate queries: {len(connection.queries) - len(check_duplicates)}")
        print(f"Total time: {total_execution_time}")
        print("#" * 20)

        
        return response
    return middleware