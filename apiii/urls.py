from rest_framework import routers
from .api import UserrViewset

router= routers.DefaultRouter()
router.register("api/user",UserrViewset,"user")

urlpatterns = router.urls