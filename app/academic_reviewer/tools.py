import os

def read_academic_file(file_path: str) -> dict:
    """Lê o conteúdo de um arquivo acadêmico local (.pdf ou .tex) e retorna o seu texto completo.

    Esta ferramenta deve ser usada sempre que o usuário solicitar a revisão de um arquivo de texto
    especificando um caminho (.pdf ou .tex).

    Args:
        file_path: O caminho do arquivo (.pdf ou .tex) no sistema de arquivos local.

    Returns:
        dict: Um dicionário contendo o status da leitura ("success" ou "error") e o texto extraído.
    """
    path = os.path.abspath(file_path.strip())
    if not os.path.exists(path):
        return {
            "status": "error",
            "message": f"Arquivo não encontrado no caminho fornecido: {file_path}"
        }

    ext = os.path.splitext(path)[1].lower()
    if ext == ".tex":
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            return {
                "status": "success",
                "format": "latex",
                "content": content
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erro ao ler o arquivo LaTeX: {str(e)}"
            }
    elif ext == ".pdf":
        try:
            from pypdf import PdfReader
            reader = PdfReader(path)
            content = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    content += text + "\n"
            return {
                "status": "success",
                "format": "pdf",
                "content": content
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Erro ao ler o arquivo PDF: {str(e)}"
            }
    else:
        return {
            "status": "error",
            "message": f"Formato de arquivo não suportado: '{ext}'. Apenas arquivos .pdf e .tex são aceitos."
        }
