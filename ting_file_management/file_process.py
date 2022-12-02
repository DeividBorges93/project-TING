from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file = txt_importer(path_file)
    fileInfos = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(fileInfos)
    return print(fileInfos, file=sys.stdout)


def remove(instance):
    if not instance or len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    path = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(f"Arquivo {path} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
