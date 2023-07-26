from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    message = "sorry for that but you are not the owner so you cant edit these feilds !!"
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True
        
        if request.user == obj.owner :
            return True 
        else : 
            return False 
        # if request.method == 'GET':
        #     return True
        # return request.user == obj.owner