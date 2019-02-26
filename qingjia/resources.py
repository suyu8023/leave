from import_export import resources
from .models import record


class CustomerResource1(resources.ModelResource):

    class Meta:
        model = record
        fields = ('id', 'schoolNum', 'name', 'grade', 'lab', 'begin_time', 'end_time', 'why', 'to', 'last_time', 'last_ip')
