from django.db import models

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)
    tipo = models.IntegerField()

    class Meta:
        db_table = 'tabelas"."menu'  # 'schema"."objeto'
       # ordering = ["menu_id"]

    def __str__(self):
        return self.nome

    objects = models.Manager()


class SubMenu(models.Model):
    id = models.IntegerField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    link = models.CharField(max_length=50)
    classe = models.CharField(max_length=50)

    class Meta:
        db_table = 'tabelas"."submenu'
        #ordering = ["submenu_id"]

    def __str__(self):
        return self.id

    objects = models.Manager()


