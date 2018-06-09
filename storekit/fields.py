from django.db.models import BigIntegerField
from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from django.utils.translation import gettext_lazy as _


class PositiveBigIntegerField(PositiveIntegerRelDbTypeMixin, BigIntegerField):

    description = _('Big (8 byte) positive integer')

    def db_type(self, connection):
        return 'bigint UNSIGNED'

    def get_internal_type(self):
        return 'PositiveSmallIntegerField'

    def formfield(self, **kwargs):
        defaults = {
            'min_value': 0,
            'max_value': BigIntegerField.MAX_BIGINT
        }
        defaults.update(kwargs)
        return super(PositiveBigIntegerField, self).formfield(**defaults)
