from django.urls import path
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
    addproduct,
    saveproduct
)

app_name = 'core'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('products/', HomeView.as_view(), name='home'),
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
    path('panel/products', AdminProdcutList.as_view(), name='panel-product'),
    path('panel/orders', AdminOrderList.as_view(), name='panel-order'),
    path('panel/users', AdminUserList.as_view(), name='panel-user'),
    path('panel/applicants',
         AdminApplicantList.as_view(), name='panel-applicant'),
    path('panel/courses', AdminCoursesList.as_view(), name='panel-course'),
    path('panel/blogs', AdminBlogList.as_view(), name='panel-blog'),
    path('panel/addproduct', addproduct, name='addproduct')
]

# Previous paths noted here. just to remember the paths for updated one
# path ('home/', LandingView.as_view(), name='landing'),
# path('', HomeView.as_view(), name='home'),
