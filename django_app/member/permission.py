from rest_framework import permissions


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Give write permission only to the owner of the object.
    Give read permission to all.
    객체의 소유자에게만 쓰기 권한을 허용한다.
    모두에게 읽기 권한을 허용한다.
    """

    def has_object_permission(self, request, view, obj):
        """
        Param obj is the same instance type to user instance, however, not always the same instance as request.user.
        obj 매개변수는 유저 인스턴스와 같은 타입이지만 항상 request.user와 같지는 않다.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user
