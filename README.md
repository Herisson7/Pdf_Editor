Recibo de Pagamento Editável
Este projeto gera um PDF de recibo de pagamento editável com campos predefinidos que podem ser preenchidos posteriormente em softwares compatíveis (como Adobe Acrobat Reader). Ele utiliza Python e bibliotecas como reportlab para a criação do layout e pdfrw para inserir campos editáveis no documento.

📋 Descrição
O script gera automaticamente um modelo de recibo de pagamento contendo:

Cabeçalho com logo da instituição (se disponível)
Título centralizado
Texto principal com campos vazios para preenchimento
Tabela com serviços educacionais e valores
Informações institucionais no rodapé
Campos editáveis prontos para uso

🧰 Requisitos
Certifique-se de ter as seguintes bibliotecas instaladas:
pip install reportlab pdfrw

📁Estrutura do Projeto
.
├── README.md
├── main.py     # Script principal
└── logo.png               # Logo da instituição (opcional)

🔧 Como Usar
Clone ou copie o arquivo main.py.

Realize as alterações/ajustes no texto principal na linha 47 do código original e na Tabela de Serviços a partir da linha 74 do código.
Toda alteração no texto também deve ser acompanhada dos ajustes nas coordenadas dos campos editáveis. Pode faze-los seguindo o exemplo do código original a partir da linha 111.

Adicione uma imagem chamada logo.png na mesma pasta do script.

Execute o script:
python recibo_editavel.py

📄 Saída Gerada
O PDF resultante conterá campos editáveis com os rótulos definidos a sua escolha.

✅ Benefícios
Automatiza a criação de recibos profissionais
Permite edição manual posterior
Flexível e fácil de personalizar
Não requer software gráfico para edição de PDFs

🛠️ Personalização
Você pode ajustar:

Cores, fontes e posicionamento dos elementos
Campos adicionais
Layout e conteúdo textual
Estilo da tabela

📦 Dependências
reportlab: Para criar o layout do PDF
pdfrw: Para adicionar campos editáveis ao PDF

📬 Suporte e Contribuições
Se encontrar algum problema ou desejar contribuir com melhorias, fique à vontade para abrir uma issue ou pull request no repositório.

📜 Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais informações.



