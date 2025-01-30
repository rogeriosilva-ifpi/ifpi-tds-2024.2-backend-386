from django.db import models
from django.core.exceptions import ValidationError

CHOICES_UF = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

CHOICES_SEXO = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro')
)

def tamanho_sigla(valor):
    if len(valor) <= 2:
        raise ValidationError('Sigla deve ter no mínimo 2 caracteres')

class Universidade(models.Model):
    sigla = models.CharField(max_length=10, 
                             null=False, blank=False,
                             validators=[tamanho_sigla,],
                             help_text='Em maiúsculo!',
        )
    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=240)
    uf = models.CharField(choices=CHOICES_UF, max_length=2)

    def __str__(self):
        return self.sigla
    
    def qtd_curso(self):
        return self.cursos.count()

CURSO_AREA_CHOICE = (
    ('HUMANAS', 'Humanas'),
    ('EXATAS', 'Exatas'),
    ('BIOLÓGICAS', 'Biológicas'),
    ('SAÚDE', 'Saúde')
)    


class Curso(models.Model):
    nome = models.CharField(max_length=200)
    area = models.CharField(choices=CURSO_AREA_CHOICE,max_length=200)

    # Relacionamento
    universidade = models.ForeignKey(Universidade,
                                     on_delete=models.RESTRICT,
                                     related_name='cursos',
                                     null=True, blank=True)

