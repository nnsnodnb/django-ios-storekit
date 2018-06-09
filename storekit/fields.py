from django.db.models.fields import BigIntegerField, PositiveIntegerRelDbTypeMixin


class PositiveBigIntegerField(PositiveIntegerRelDbTypeMixin, BigIntegerField):

    description = 'Big (8 byte) positive integer'

    def get_internal_type(self):
        return 'PositiveSmallIntegerField'

    def formfield(self, **kwargs):
        defaults = {
            'min_value': 0,
            'max_value': BigIntegerField.MAX_BIGINT
        }
        defaults.update(kwargs)
        return super(PositiveBigIntegerField, self).formfield(**defaults)
