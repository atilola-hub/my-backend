from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    message = "You need to be a seller before you can do this!"
    def has_permission(self, request, view):
        user = request.user
        return user.type == "SELLER"

class RiderPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == "RIDER"

class BuyerRiderPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.type in ["BUYER", "RIDER"]