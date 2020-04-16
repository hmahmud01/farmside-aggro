from django.urls import path
from .views import (
    AdminIndex,
    AdminProdcutList,
    AdminOrderList,
    AdminUserList,
    AdminApplicantList,
    AdminCoursesList,
    AdminBlogList,
    addproduct,
    saveproduct
)

app_name = 'core'

urlpatterns = [
    path('panel/', AdminIndex.as_view(), name='admin-panel'),
    path('panel/products', AdminProdcutList.as_view(), name='admin-product'),
    path('panel/orders', AdminOrderList.as_view(), name='admin-order'),
    path('panel/users', AdminUserList.as_view(), name='admin-user'),
    path('panel/applicants',
         AdminApplicantList.as_view(), name='admin-applicant'),
    path('panel/courses', AdminCoursesList.as_view(), name='admin-course'),
    path('panel/blogs', AdminBlogList.as_view(), name='admin-blog'),
    path('panel/addproduct', addproduct, name='addproduct'),
    path('panel/saveproduct', saveproduct, name='saveproduct')
]
