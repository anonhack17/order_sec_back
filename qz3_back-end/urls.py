from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect, render
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from cmd_kali.views import executeCommandView
from django.shortcuts import render

from by_pass_sheet.urls import router as by_pass_sheet_router
from post.urls import router as post_router
from customer.urls import router as customer_router
from employee.urls import router as employee_router
from company.urls import router as company_router
from project.urls import router as project_router

from security.urls import router as security_router

from two_factor.urls import urlpatterns as tf_urls

def base(request):
    log_entries = []

    try:
        with open('django.log', 'r') as log_file:

            log_entries = log_file.readlines()
    except FileNotFoundError:
        pass  # Handle the case when the log file doesn't exist
    return render(request, 'base.html',  {'log_entries': log_entries})


router = DefaultRouter()

router.registry.extend(post_router.registry)
router.registry.extend(customer_router.registry)
router.registry.extend(employee_router.registry)
router.registry.extend(by_pass_sheet_router.registry)
router.registry.extend(company_router.registry)
router.registry.extend(project_router.registry)
router.registry.extend(security_router.registry)

urlpatterns = [
                  path('', base),
                  path(r'', include(tf_urls)),
                  path('api/', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls')),
                  path('auth/', include('djoser.urls')),
                  path('auth/', include('djoser.urls.authtoken')),
                  path('auth/', include('djoser.urls.jwt')),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                  path('cmd_kali/', executeCommandView),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
