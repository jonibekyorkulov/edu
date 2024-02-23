from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken
from datetime import datetime, timezone
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
# from api.account.exceptions import BAD_REQUESTException
from apps.base.enum import UserRol

class IsAdmin(permissions.BasePermission):
    object_class = None
    role_method_name = UserRol.ADMIN

    def has_permission(self, request, view):
        if request.user.uuid is None:
            return False
        user = request.user
        if user.role == None:
            return False
        if self.role_method_name.value == user.role:
            try:
                token = OutstandingToken.objects.filter(user=user).order_by('-id')[0]
                block = BlacklistedToken.objects.filter(token=token)
                if not block:
                    return True
                else:
                    error = {
                    'detail': f"please login again"}
                    raise ValidationError(error)
            except OutstandingToken.DoesNotExist:
                error = {
                    'detail': f"DoesNotExist"}
                raise ValidationError(error)
        return False


class IsTeacher(permissions.BasePermission):
    object_class = None
    role_method_name = UserRol.TEACHER

    def has_permission(self, request, view):
        if request.user.uuid is None:
            return False
        user = request.user
        if user.role == None:
            return False
        if self.role_method_name.value == user.role:
            try:
                token = OutstandingToken.objects.filter(user=user).order_by('-id')[0]
                block = BlacklistedToken.objects.filter(token=token)
                if not block:
                    return True
                else:
                    error = {
                    'detail': f"please login again"}
                    raise ValidationError(error)
            except OutstandingToken.DoesNotExist:
                error = {
                    'detail': f"DoesNotExist"}
                raise ValidationError(error)
        return False


class IsStudent(permissions.BasePermission):
    object_class = None
    role_method_name = UserRol.STUDENT.value

    def has_permission(self, request, view):
        if request.user.uuid is None:
            return False
        user = request.user
        if user.role == None:
            return False
        if self.role_method_name.value == user.role:
            try:
                token = OutstandingToken.objects.filter(user=user).order_by('-id')[0]
                block = BlacklistedToken.objects.filter(token=token)
                if not block:
                    return True
                else:
                    error = {
                        'detail': f"please login again"}
                    raise ValidationError(error)
            except OutstandingToken.DoesNotExist:
                error = {
                    'detail': f"DoesNotExist"}
                raise ValidationError(error)
        return False


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.uuid is None:
            return False
        user = request.user
        if user.role == None:
            return False
        try:
            token = OutstandingToken.objects.filter(
                user=user).order_by('-id')[0]
            block = BlacklistedToken.objects.filter(token=token)
            if not block:
                return True
            else:
                error = {
                    'detail': f"please login again"}
                raise ValidationError(error)
        except OutstandingToken.DoesNotExist:
            error = {
                'detail': f"DoesNotExist"}
            raise ValidationError(error)