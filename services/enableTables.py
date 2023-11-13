from django.shortcuts import get_object_or_404


class Element:
    def enableElement(self, element, table, id):
        record = get_object_or_404(table, pk=id, status=False)
        record.status = True
        record.save()
        return {"message": f"{element} {record.name} habilitado"}

    def disableElement(self, table, id):
        record = get_object_or_404(table, pk=id, status=True)
        record.status = False
        record.save()
