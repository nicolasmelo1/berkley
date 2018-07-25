from login.models import Companies, Profiles, UserExtended
from pipeline.models import RegionalsAccessedBy, SubsidiariesAccessedBy, Regionals, Subsidiaries


class PermissionHandler:
    def __init__(self, user, company=None):
        self.user = user
        self.company = company

    def get_user_company(self):
        company = Companies.objects.get(id=self.user.company_id)
        return company
