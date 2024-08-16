from django.db import models
from .options import *

class Info(models.Model):
    cat_number = models.CharField(primary_key=True, max_length=7, blank=True, unique=True)
    data = models.DateField()
    codigo_cliente = models.IntegerField()
    cliente = models.CharField(max_length=100)
    codigo_equip = models.CharField(max_length=12)
    equip = models.CharField(max_length=255)
    pessoa_contato = models.CharField(max_length=255)
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    tecnico = models.CharField(max_length=255, choices=TEC, default='Selecione')
    resp_permution = models.CharField(max_length=255, choices=RESP, default='Selecione')

    def __str__(self):
        return self.cat_number
    
class Ordem(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=100)
    ordem = models.TextField()

    def __str__(self):
        return self.ordem
    
class Start(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    preReq = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    matInt = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    preFlu = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    preTrat = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    valv = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    locMemb = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    alarm = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    insCoe = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    sisSeg = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    agua = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)

    def __str__(self):
        return self.pre_req_tec

class Servicos(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    matDisp = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    servExc = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    sistIns = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    equipVaz = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    leiCoer = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)
    amostra = models.CharField(max_length=3, choices=BOOL_NA, default='na', blank=True)

    def __str__(self):
        return self.matDisp
    
class Pressurizador(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    pressaoAlimentacao = models.CharField(max_length=3, blank=True)
    funcionamentoCorreto = models.CharField(max_length=3, choices=BOOL, default='na', blank=True)

    def __str__(self):
        return self.pressaoAlimentacao
    
class Filtros(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    frcl_areia  = models.CharField(max_length=10, null=True, blank=True)
    tr_areia    = models.CharField(max_length=5, null=True, blank=True)
    te_areia    = models.CharField(max_length=5, null=True, blank=True)
    frcl_carvao = models.CharField(max_length=10, null=True, blank=True)
    tr_carvao   = models.CharField(max_length=5, null=True, blank=True)
    te_carvao   = models.CharField(max_length=5, null=True, blank=True)
    frcl_ab     = models.CharField(max_length=10, null=True, blank=True)
    tr_ab       = models.CharField(max_length=5, null=True, blank=True)
    ts_ab       = models.CharField(max_length=5, null=True, blank=True)
    tp_ab       = models.CharField(max_length=5, null=True, blank=True)
    te_ab       = models.CharField(max_length=5, null=True, blank=True)
    trep_ab     = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.frcl_areia
    
class Dosagem(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    prod_dos1 = models.CharField(max_length=50)
    conc_dos1 = models.CharField(max_length=20, null=True, blank=True)
    volume_dos1 = models.CharField(max_length=20, null=True, blank=True)
    prod_dos2 = models.CharField(max_length=50)
    conc_dos2 = models.CharField(max_length=20, null=True, blank=True)
    volume_dos2 = models.CharField(max_length=20, null=True, blank=True)
    aferir_dos = models.CharField(max_length=5)
    padrao = models.CharField(max_length=100, null=True, blank=True)
    info_std = models.TextField()

    def __str__(self):
        return self.prod_dos1

class Desmi(models.Model):
    cat_number  = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    frcl_cat    = models.CharField(max_length=10, null=True, blank=True)
    tr_cat      = models.CharField(max_length=10, null=True, blank=True)
    ts_cat      = models.CharField(max_length=10, null=True, blank=True)
    tp_cat      = models.CharField(max_length=10, null=True, blank=True)
    te_cat      = models.CharField(max_length=10, null=True, blank=True)
    frcl_ani    = models.CharField(max_length=10, null=True, blank=True)
    tr_ani      = models.CharField(max_length=10, null=True, blank=True)
    ts_ani      = models.CharField(max_length=10, null=True, blank=True)
    tp_ani      = models.CharField(max_length=10, null=True, blank=True)
    te_ani      = models.CharField(max_length=10, null=True, blank=True)
    cond_fin    = models.CharField(max_length=10, null=True, blank=True)
    temp        = models.CharField(max_length=10, null=True, blank=True)
    ser_cond    = models.CharField(max_length=10, null=True, blank=True)
    constante   = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return self.ser_cond
    
class Osmose(models.Model):
    tipo_sist       = models.CharField(max_length=3, choices=OSM, default='Selecione', blank=True)
    cat_number      = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente         = models.CharField(max_length=50, blank=True, null=True)
    vaz_alim        = models.CharField(max_length=10, null=True, blank=True)
    p_in_big        = models.CharField(max_length=10, null=True, blank=True)
    p_out_big       = models.CharField(max_length=10, null=True, blank=True)
    p_in_m1         = models.CharField(max_length=10, null=True, blank=True)
    p_out_m1        = models.CharField(max_length=10, null=True, blank=True)
    p_in_m2         = models.CharField(max_length=10, null=True, blank=True)
    p_out_m2        = models.CharField(max_length=10, null=True, blank=True)
    vaz_pr1         = models.CharField(max_length=10, null=True, blank=True)
    vaz_rj1         = models.CharField(max_length=10, null=True, blank=True)
    vaz_rc1         = models.CharField(max_length=10, null=True, blank=True)
    vaz_pr2         = models.CharField(max_length=10, null=True, blank=True)
    vaz_rc2         = models.CharField(max_length=10, null=True, blank=True)
    cond_final      = models.CharField(max_length=10, null=True, blank=True)
    temp_osm        = models.CharField(max_length=10, null=True, blank=True)
    vaz_alim2        = models.CharField(max_length=10, null=True, blank=True)
    p_in_big2        = models.CharField(max_length=10, null=True, blank=True)
    p_out_big2       = models.CharField(max_length=10, null=True, blank=True)
    p_in_m12         = models.CharField(max_length=10, null=True, blank=True)
    p_out_m12        = models.CharField(max_length=10, null=True, blank=True)
    p_in_m22         = models.CharField(max_length=10, null=True, blank=True)
    p_out_m22        = models.CharField(max_length=10, null=True, blank=True)
    vaz_pr12         = models.CharField(max_length=10, null=True, blank=True)
    vaz_rj12         = models.CharField(max_length=10, null=True, blank=True)
    vaz_rc12         = models.CharField(max_length=10, null=True, blank=True)
    vaz_pr22         = models.CharField(max_length=10, null=True, blank=True)
    vaz_rc22         = models.CharField(max_length=10, null=True, blank=True)
    cond_final2      = models.CharField(max_length=10, null=True, blank=True)
    temp_osm2        = models.CharField(max_length=10, null=True, blank=True)
    horas_tr        = models.CharField(max_length=10, null=True, blank=True)
    teste_press     = models.CharField(max_length=25, choices=OSM_OP, default='Selecione', blank=True)
    teste_agua      = models.CharField(max_length=25, choices=OSM_OP, default='Selecione', blank=True)
    ser_cond_osm    = models.CharField(max_length=10, null=True, blank=True)
    constante_osm   = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.vaz_rc1
    
class Leito(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    cond_lei    = models.CharField(max_length=10, null=True, blank=True)
    temp_lei        = models.CharField(max_length=10, null=True, blank=True)
    ser_cond_lei    = models.CharField(max_length=10, null=True, blank=True)
    const_lei    = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.cond_lei
    
class Afericao(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    mod_cond = models.CharField(max_length=40, null=True, blank=True)
    const = models.CharField(max_length=40, null=True, blank=True)
    n_lote = models.CharField(max_length=40, null=True, blank=True)
    cond_std = models.CharField(max_length=40, null=True, blank=True)
    temp_std = models.CharField(max_length=40, null=True, blank=True)
    marca = models.CharField(max_length=40, null=True, blank=True)
    cond_aferida = models.CharField(max_length=40, null=True, blank=True)
    temp_aferida = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.mod_cond

class Ozonio(models.Model):
    OPCOES_VER_OPC = [
        ('FC', 'FC'),
        ('AD', 'AD'),
    ]
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    ver_opc = models.CharField(max_length=2, choices=OPCOES_VER_OPC, blank=True, null=True)
    orp_high = models.CharField(max_length=50, blank=True, null=True)
    orp_low = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ver_opc

class Uv(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    horas_osmose = models.CharField(max_length=50)
    horas_looping = models.CharField(max_length=50)

    def __str__(self):
        return self.horas_osmose

class Recup_Rejeito(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    p_in = models.FloatField()
    p_pos_cart = models.FloatField()
    p_pre_memb = models.FloatField()
    p_pos_memb = models.FloatField()
    vazao_perm = models.FloatField()
    vazao_rej = models.FloatField()

    def __str__(self):
        return self.p_in

class Analise_Agua(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    cliente = models.CharField(max_length=50, blank=True, null=True)
    amostra1 = models.CharField(max_length=100, blank=True, null=True)
    cond1 = models.FloatField(blank=True, null=True)
    ph1 = models.FloatField(blank=True, null=True)
    temp1 = models.FloatField(blank=True, null=True)
    cloro1 = models.FloatField(blank=True, null=True)
    dureza1 = models.FloatField(blank=True, null=True)
    ferro1 = models.FloatField(blank=True, null=True)
    silica1 = models.FloatField(blank=True, null=True)
    cor = models.FloatField(blank=True, null=True)
    turbidez = models.FloatField(blank=True, null=True)
    outro_par_a1 = models.CharField(max_length=100, blank=True)
    outro_par_b1 = models.CharField(max_length=100, blank=True)
    outro_par_c1 = models.CharField(max_length=100, blank=True)
    outro_par_d1 = models.CharField(max_length=100, blank=True)

    amostra2 = models.CharField(max_length=100, blank=True, null=True)
    cond2 = models.FloatField(blank=True, null=True)
    ph2 = models.FloatField(blank=True, null=True)
    temp2 = models.FloatField(blank=True, null=True)
    cloro2 = models.FloatField(blank=True, null=True)
    dureza2 = models.FloatField(blank=True, null=True)
    ferro2 = models.FloatField(blank=True, null=True)
    silica2 = models.FloatField(blank=True, null=True)
    cor2 = models.FloatField(blank=True, null=True)
    turbidez2 = models.FloatField(blank=True, null=True)
    outro_par_a2 = models.CharField(max_length=100, blank=True)
    outro_par_b2 = models.CharField(max_length=100, blank=True)
    outro_par_c2 = models.CharField(max_length=100, blank=True)
    outro_par_d2 = models.CharField(max_length=100, blank=True)

    amostra3 = models.CharField(max_length=100, blank=True, null=True)
    cond3 = models.FloatField(blank=True, null=True)
    ph3 = models.FloatField(blank=True, null=True)
    temp3 = models.FloatField(blank=True, null=True)
    cloro3 = models.FloatField(blank=True, null=True)
    dureza3 = models.FloatField(blank=True, null=True)
    ferro3 = models.FloatField(blank=True, null=True)
    silica3 = models.FloatField(blank=True, null=True)
    cor3 = models.FloatField(blank=True, null=True)
    turbidez3 = models.FloatField(blank=True, null=True)
    outro_par_a3 = models.CharField(max_length=100, blank=True)
    outro_par_b3 = models.CharField(max_length=100, blank=True)
    outro_par_c3 = models.CharField(max_length=100, blank=True)
    outro_par_d3 = models.CharField(max_length=100, blank=True)

    amostra4 = models.CharField(max_length=100, blank=True, null=True)
    cond4 = models.FloatField(blank=True, null=True)
    ph4 = models.FloatField(blank=True, null=True)
    temp4 = models.FloatField(blank=True, null=True)
    cloro4 = models.FloatField(blank=True, null=True)
    dureza4 = models.FloatField(blank=True, null=True)
    ferro4 = models.FloatField(blank=True, null=True)
    silica4 = models.FloatField(blank=True, null=True)
    cor4 = models.FloatField(blank=True, null=True)
    turbidez4 = models.FloatField(blank=True, null=True)
    outro_par_a4 = models.CharField(max_length=100, blank=True)
    outro_par_b4 = models.CharField(max_length=100, blank=True)
    outro_par_c4 = models.CharField(max_length=100, blank=True)
    outro_par_d4 = models.CharField(max_length=100, blank=True)

    amostra5 = models.CharField(max_length=100, blank=True, null=True)
    cond5 = models.FloatField(blank=True, null=True)
    ph5 = models.FloatField(blank=True, null=True)
    temp5 = models.FloatField(blank=True, null=True)
    cloro5 = models.FloatField(blank=True, null=True)
    dureza5 = models.FloatField(blank=True, null=True)
    ferro5 = models.FloatField(blank=True, null=True)
    silica5 = models.FloatField(blank=True, null=True)
    cor5 = models.FloatField(blank=True, null=True)
    turbidez5 = models.FloatField(blank=True, null=True)
    outro_par_a5 = models.CharField(max_length=100, blank=True)
    outro_par_b5 = models.CharField(max_length=100, blank=True)
    outro_par_c5 = models.CharField(max_length=100, blank=True)
    outro_par_d5 = models.CharField(max_length=100, blank=True)

    amostra6 = models.CharField(max_length=100, blank=True, null=True)
    cond6 = models.FloatField(blank=True, null=True)
    ph6 = models.FloatField(blank=True, null=True)
    temp6 = models.FloatField(blank=True, null=True)
    cloro6 = models.FloatField(blank=True, null=True)
    dureza6 = models.FloatField(blank=True, null=True)
    ferro6 = models.FloatField(blank=True, null=True)
    silica6 = models.FloatField(blank=True, null=True)
    cor6 = models.FloatField(blank=True, null=True)
    turbidez6 = models.FloatField(blank=True, null=True)
    outro_par_a6 = models.CharField(max_length=100, blank=True)
    outro_par_b6 = models.CharField(max_length=100, blank=True)
    outro_par_c6 = models.CharField(max_length=100, blank=True)
    outro_par_d6 = models.CharField(max_length=100, blank=True)

    amostra7 = models.CharField(max_length=100, blank=True, null=True)
    cond7 = models.FloatField(blank=True, null=True)
    ph7 = models.FloatField(blank=True, null=True)
    temp7 = models.FloatField(blank=True, null=True)
    cloro7 = models.FloatField(blank=True, null=True)
    dureza7 = models.FloatField(blank=True, null=True)
    ferro7 = models.FloatField(blank=True, null=True)
    silica7 = models.FloatField(blank=True, null=True)
    cor7 = models.FloatField(blank=True, null=True)
    turbidez7 = models.FloatField(blank=True, null=True)
    outro_par_a7 = models.CharField(max_length=100, blank=True)
    outro_par_b7 = models.CharField(max_length=100, blank=True)
    outro_par_c7 = models.CharField(max_length=100, blank=True)
    outro_par_d7 = models.CharField(max_length=100, blank=True)

    amostra8 = models.CharField(max_length=100, blank=True, null=True)
    cond8 = models.FloatField(blank=True, null=True)
    ph8 = models.FloatField(blank=True, null=True)
    temp8 = models.FloatField(blank=True, null=True)
    cloro8 = models.FloatField(blank=True, null=True)
    dureza8 = models.FloatField(blank=True, null=True)
    ferro8 = models.FloatField(blank=True, null=True)
    silica8 = models.FloatField(blank=True, null=True)
    cor8 = models.FloatField(blank=True, null=True)
    turbidez8 = models.FloatField(blank=True, null=True)
    outro_par_a8 = models.CharField(max_length=100, blank=True)
    outro_par_b8 = models.CharField(max_length=100, blank=True)
    outro_par_c8 = models.CharField(max_length=100, blank=True)
    outro_par_d8 = models.CharField(max_length=100, blank=True)

    amostra9 = models.CharField(max_length=100, blank=True, null=True)
    cond9 = models.FloatField(blank=True, null=True)
    ph9 = models.FloatField(blank=True, null=True)
    temp9 = models.FloatField(blank=True, null=True)
    cloro9 = models.FloatField(blank=True, null=True)
    dureza9 = models.FloatField(blank=True, null=True)
    ferro9 = models.FloatField(blank=True, null=True)
    silica9 = models.FloatField(blank=True, null=True)
    cor9 = models.FloatField(blank=True, null=True)
    turbidez9 = models.FloatField(blank=True, null=True)
    outro_par_a9 = models.CharField(max_length=100, blank=True)
    outro_par_b9 = models.CharField(max_length=100, blank=True)
    outro_par_c9 = models.CharField(max_length=100, blank=True)
    outro_par_d9 = models.CharField(max_length=100, blank=True)

    amostra10 = models.CharField(max_length=100, blank=True, null=True)
    cond10 = models.FloatField(blank=True, null=True)
    ph10 = models.FloatField(blank=True, null=True)
    temp10 = models.FloatField(blank=True, null=True)
    cloro10 = models.FloatField(blank=True, null=True)
    dureza10 = models.FloatField(blank=True, null=True)
    ferro10 = models.FloatField(blank=True, null=True)
    silica10 = models.FloatField(blank=True, null=True)
    cor10 = models.FloatField(blank=True, null=True)
    turbidez10 = models.FloatField(blank=True, null=True)
    outro_par_a10 = models.CharField(max_length=100, blank=True)
    outro_par_b10 = models.CharField(max_length=100, blank=True)
    outro_par_c10 = models.CharField(max_length=100, blank=True)
    outro_par_d10 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.amostra1

class Treinamento(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    curso = models.CharField(max_length=50)
    data = models.DateField()
    assinatura = models.ImageField(upload_to='assinaturas/')
   
class Parte_Tec(models.Model):
    cat_number = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True)
    data_at1 = models.DateField(blank=True, null=True)
    hora_cheg1 = models.TimeField(blank=True, null=True)
    hora_sai1 = models.TimeField(blank=True, null=True)

    data_at2 = models.DateField(blank=True, null=True)
    hora_cheg2 = models.TimeField(blank=True, null=True)
    hora_sai2 = models.TimeField(blank=True, null=True)

    data_at3 = models.DateField(blank=True, null=True)
    hora_cheg3 = models.TimeField(blank=True, null=True)
    hora_sai3 = models.TimeField(blank=True, null=True)

    data_at4 = models.DateField(blank=True, null=True)
    hora_cheg4 = models.TimeField(blank=True, null=True)
    hora_sai4 = models.TimeField(blank=True, null=True)

    data_at5 = models.DateField(blank=True, null=True)
    hora_cheg5 = models.TimeField(blank=True, null=True)
    hora_sai5 = models.TimeField(blank=True, null=True)

    data_at6 = models.DateField(blank=True, null=True)
    hora_cheg6 = models.TimeField(blank=True, null=True)
    hora_sai6 = models.TimeField(blank=True, null=True)

    data_at7 = models.DateField(blank=True, null=True)
    hora_cheg7 = models.TimeField(blank=True, null=True)
    hora_sai7 = models.TimeField(blank=True, null=True)

    data_at8 = models.DateField(blank=True, null=True)
    hora_cheg8 = models.TimeField(blank=True, null=True)
    hora_sai8 = models.TimeField(blank=True, null=True)

    data_at9 = models.DateField(blank=True, null=True)
    hora_cheg9 = models.TimeField(blank=True, null=True)
    hora_sai9 = models.TimeField(blank=True, null=True)

    data_at10 = models.DateField(blank=True, null=True)
    hora_cheg10 = models.TimeField(blank=True, null=True)
    hora_sai10 = models.TimeField(blank=True, null=True)

    data_at11 = models.DateField(blank=True, null=True)
    hora_cheg11 = models.TimeField(blank=True, null=True)
    hora_sai11 = models.TimeField(blank=True, null=True)

    data_at12 = models.DateField(blank=True, null=True)
    hora_cheg12 = models.TimeField(blank=True, null=True)
    hora_sai12 = models.TimeField(blank=True, null=True)

    data_at13 = models.DateField(blank=True, null=True)
    hora_cheg13 = models.TimeField(blank=True, null=True)
    hora_sai13 = models.TimeField(blank=True, null=True)

    data_at14 = models.DateField(blank=True, null=True)
    hora_cheg14 = models.TimeField(blank=True, null=True)
    hora_sai14 = models.TimeField(blank=True, null=True)

    obs_tecnicas = models.TextField(blank=True, null=True)
    pendencias = models.TextField(blank=True, null=True)
    assinatura1 = models.ImageField(upload_to='assinaturas/', blank=True, null=True)
    assinatura2 = models.ImageField(upload_to='assinaturas/', blank=True, null=True)

class Conferencia(models.Model):
    resp_conferencia = models.CharField(max_length=25, choices=RESP_CONF, default='Selecione', blank=True)