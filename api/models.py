from tastypie.resources import ModelResource
from shop.models import Category, Desideorio
from .authentication import CustomAuthentication
from tastypie.authorization import Authorization

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']

class DesideorioResource(ModelResource):
    class Meta:
        queryset = Desideorio.objects.all()
        resource_name = 'desideorios'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data["category_id"]
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category
        return bundle


    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()