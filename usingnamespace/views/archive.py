from pyramid.view import view_config
from sqlalchemy.orm import undefer

from ..models import (
    Entry,
)

class Archive:
    def __init__(self, context, request):
        self.request = request
        self.context = context

    @view_config(
        context='..traversal.ArchiveYear',
        renderer='templates/yearly.mako'
    )
    def year(self):
        entries = (
            self.context.entries.
            order_by(Entry.pubdate.desc()).
            options(undefer('current_revision.entry')).
            all()
        )

        return {
            'entries': entries,
            'year': self.context.year,
        }

    @view_config(
        context='..traversal.ArchiveYearMonth',
        renderer='templates/chronological.mako'
    )
    def month(self):
        entries = (
            self.context.entries.
            order_by(Entry.pubdate.desc()).
            options(undefer('current_revision.entry')).
            all()
        )

        return {
            'entries': entries,
        }

    @view_config(
        context='..traversal.ArchiveYearMonthDay',
        renderer='templates/chronological.mako'
    )
    def day(self):
        entries = (
            self.context.entries.
            order_by(Entry.pubdate.desc()).
            options(undefer('current_revision.entry')).
            all()
        )

        return {
            'entries': entries,
        }
