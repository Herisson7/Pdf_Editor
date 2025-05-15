from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from pdfrw import PdfReader, PdfWriter, PdfName, PdfDict
import os

def criar_campo_editavel(reader, page_index, nome, x, y, largura, altura, valor=""):
    """Cria um campo de texto editável no PDF"""
    page = reader.pages[page_index]
    if PdfName.Annots not in page:
        page[PdfName.Annots] = []
    
    campo = PdfDict(
        Type=PdfName.Annot,
        Subtype=PdfName.Widget,
        FT=PdfName.Tx,  # Tipo Texto
        Rect=[x, y, x + largura, y + altura],
        T=nome,  # Nome do campo
        V=valor,  # Valor padrão
        DA="/Helvetica 12 Tf 0 g",  # Aparência
        Ff=0,  # 0 = Editável
        F=4,  # 4 = Imprimir
        Q=1,  # Alinhamento (1=centro)
    )
    page[PdfName.Annots].append(campo)

def criar_recibo_editavel():
    # Configurações
    temp_pdf = "temp.pdf"
    output_pdf = "Recibo_Pagamento_Editavel.pdf"
    c = canvas.Canvas(temp_pdf, pagesize=A4)
    largura, altura = A4

    # 1. CABEÇALHO
    logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 1*cm, altura-3.5*cm, width=5*cm, height=2*cm)

    # 2. TÍTULO
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(largura/2, altura-6.5*cm, "RECIBO DE PAGAMENTO")

    # 3. TEXTO PRINCIPAL (com espaços para os campos)
    texto = """INSTITUIÇÃO ADV DE EDUC E ASSIS SOCIAL NORTE BRASILEIRA, inscrita no
CNPJ sob o nº 00.000.000/0000-00, declara ter recebido a quantia de R$__________,
pago por ___________________________, CPF: _______________, referente à mensalidade do(a) aluno(a)
____________________________."""

    # Estilo para justificar o texto
    estilo = ParagraphStyle(
        name="Justificado",
        fontName="Helvetica",
        fontSize=12,
        leading=17,  # Espaçamento entre linhas
        alignment=TA_JUSTIFY,  # Justificação
        spaceAfter=10,  # Espaçamento após o parágrafo
    )

    # Criar o parágrafo justificado
    paragrafo = Paragraph(texto, estilo)

    # Definir a largura e altura disponíveis para o texto
    largura_disponivel = largura - 4*cm  # Margens de 2 cm em cada lado
    altura_disponivel = altura - 15*cm  # Ajuste para evitar sobreposição com outros elementos

    # Renderizar o parágrafo no canvas
    paragrafo.wrapOn(c, largura_disponivel, altura_disponivel)
    paragrafo.drawOn(c, 2*cm, altura - 10*cm)  # Posição inicial do texto

    # 4. TABELA DE SERVIÇOS
    dados = [
        ["Serviços Educacionais - ", "R$ ______________"],
        ["Serviços de Pensionato", "R$ ______________"],
        ["Desconto REA - Educacional", "R$ ______________"],
        ["Desconto REA - Pensionato", "R$ ______________"]
    ]

    # Configurar a tabela
    tabela = Table(dados, colWidths=[12*cm, 4*cm])  # Largura das colunas
    tabela.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Fonte para toda a tabela
        ('FONTSIZE', (0, 0), (-1, -1), 10),  # Tamanho da fonte
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),  # Alinhar valores à direita
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Linhas da grade
        ('BOX', (0, 0), (-1, -1), 0.5, colors.black),  # Borda externa
    ]))

    # Definir posição da tabela
    tabela.wrapOn(c, largura, altura)
    tabela.drawOn(c, 2*cm, altura-17*cm)  # Posição inicial da tabela

    # 5. RODAPÉ
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(6.4*cm, 7.9*cm, "AAAAAAAAA AAAAAAAAAA AA AAAAAAAA")#Nome da faculdade
    c.setFont("Helvetica", 11)
    c.drawString(7.5*cm, 7.4*cm, "Port. MEC n° 0.000 de 00/00/2025")#Dados de registro
    c.drawString(6*cm, 6.9*cm, "Rod. AAAAAAA AAAAA, Km 00 - São Paulo, 00.000-000") #Escrever o endereço correto
    c.drawString(15*cm, 4.9*cm, "AAAAAAAAA, ___________")#Cidade e espaço para data (editavel)

    # Salvar PDF temporário
    c.save()

    # Adicionar campos editáveis
    reader = PdfReader(temp_pdf)
    
    # Definir coordenadas dos campos (x, y, largura, altura)
    campos = [
        ("CURSO", 6*cm, altura-14.7*cm, 4*cm, 0.5*cm),
        ("VALOR_EDU", 14.7*cm, altura-14.7*cm, 3*cm, 0.5*cm),
        ("VALOR2", 14.7*cm, altura-14.1*cm, 3*cm, 0.5*cm),
        ("VALOR3", 14.7*cm, altura-13.4*cm, 3*cm, 0.5*cm),
        ("VALOR4", 14.7*cm, altura-12.8*cm, 3*cm, 0.5*cm),
        ("NOME_RESP", 2.0*cm, altura-20.43*cm, 6.3*cm, 0.5*cm),
        ("Nome_aluno", 4.7*cm, altura-19.8*cm, 6.7*cm, 0.5*cm),
        ("CPF2", 10*cm, altura-20.43*cm, 3.56*cm, 0.5*cm),
        ("VALOR_TOTAL", 14.7*cm, altura-21*cm, 2.4*cm, 0.5*cm),
        ("DATA", 17.4*cm, altura-4.79*cm, 2.7*cm, 0.5*cm),
        
    ]

    for nome, x, y, w, h in campos:
        criar_campo_editavel(reader, 0, nome, x, altura-y, w, h)

    # Salvar PDF final
    PdfWriter(output_pdf, trailer=reader).write()
    os.remove(temp_pdf)
    print(f"Recibo editável criado: {output_pdf}")

if __name__ == "__main__":
    criar_recibo_editavel()