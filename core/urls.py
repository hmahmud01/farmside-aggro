from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    LandingView,
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    AdminIndex,
    AdminProdcutList,
    AdminOrderList,
    AdminUserList,
    AdminApplicantList,
    AdminCoursesList,
    AdminBlogList,
    adminproductlist,
    addproduct,
    saveproduct,
    deleteproduct,
    adminorderlist,
    adminuserlist,
    product_detail
)

app_name = 'core'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('products/', HomeView.as_view(), name='home'),
    path('detail/<int:pid>/', product_detail, name='detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('panel/', AdminIndex.as_view(), name='panel-index'),
    path('panel/orders', adminorderlist, name='panel-order'),
    path('panel/users', adminuserlist, name='panel-user'),
    path('panel/applicants',
         AdminApplicantList.as_view(), name='panel-applicant'),
    path('panel/courses', AdminCoursesList.as_view(), name='panel-course'),
    path('panel/blogs', AdminBlogList.as_view(), name='panel-blog'),
    path('panel/products', adminproductlist, name='panel-product'),
    path('panel/addproduct', addproduct, name='addproduct'),
    path('panel/saveproduct', saveproduct, name='saveproduct'),
    path('panel/deleteproduct/<int:pid>/',
         deleteproduct, name='deleteproduct')
]

# Previous paths noted here. just to remember the paths for updated one
# path ('home/', LandingView.as_view(), name='landing'),
# path('', HomeView.as_view(), name='home'),
