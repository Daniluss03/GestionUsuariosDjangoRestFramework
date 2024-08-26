from rest_framework import routers 
from .api import RoleViewSet

router= routers.DefaultRouter()

router.register('api/roles',RoleViewSet,'Roles')

urlpatterns=router.urls