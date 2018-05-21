from rest_framework import routers
from api.rest.views import (UserViewSet, EmployeeViewSet, EmployerViewSet,
                            CompanyViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employers', EmployerViewSet)
router.register(r'companies', CompanyViewSet)
