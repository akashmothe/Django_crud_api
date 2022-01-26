from studentapi_app.viewsets import StudentsViewsets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('student', StudentsViewsets)
