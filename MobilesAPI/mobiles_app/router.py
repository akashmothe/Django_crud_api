from mobiles_app.views import MobileViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mobile', MobileViewset)