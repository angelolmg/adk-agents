import os
import json
from datetime import datetime
from typing import List, Dict, Any

# Path to the shared JSON database file located in the parent directory
DB_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "database.json"))

def load_data() -> List[Dict[str, Any]]:
    """Internal helper to load all registered tasks and events from the JSON database."""
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_data(data: List[Dict[str, Any]]) -> None:
    """Internal helper to save tasks and events to the JSON database."""
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def get_date() -> dict:
    """Retorna o dia, o dia da semana e a hora atual no sistema.

    Esta ferramenta deve ser usada para facilitar as consultas quando o usuário 
    perguntar sobre hoje, amanhã ou um dia específico relacionado ao dia atual.

    Returns:
        dict: Um dicionário contendo o dia atual (formato YYYY-MM-DD), o dia da 
              semana (em português) e o horário atual (HH:MM:SS).
    """
    now = datetime.now()
    weekdays = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }
    return {
        "data_atual": now.strftime("%Y-%m-%d"),
        "dia_da_semana": weekdays[now.weekday()],
        "hora_atual": now.strftime("%H:%M:%S")
    }

def save_event_task(titulo: str, tipo: str, data: str, descricao: str) -> dict:
    """Cadastra um novo evento ou tarefa solicitado pelo usuário.

    Args:
        titulo: O título da tarefa ou do evento.
        tipo: O tipo do cadastro, que deve ser 'evento' ou 'tarefa'.
        data: A data do evento ou o prazo da tarefa no formato YYYY-MM-DD.
        descricao: A descrição detalhada da tarefa ou do evento.

    Returns:
        dict: Um dicionário com o status da operação e os detalhes do item salvo.
    """
    tipo_clean = tipo.lower().strip()
    if tipo_clean not in ["evento", "tarefa"]:
        return {
            "status": "error",
            "message": f"Tipo inválido: '{tipo}'. O tipo deve ser 'evento' ou 'tarefa'."
        }

    try:
        datetime.strptime(data.strip(), "%Y-%m-%d")
        data_clean = data.strip()
    except ValueError:
        return {
            "status": "error",
            "message": f"Formato de data inválido: '{data}'. A data deve estar no formato YYYY-MM-DD."
        }

    new_item = {
        "titulo": titulo.strip(),
        "tipo": tipo_clean,
        "data": data_clean,
        "descrição": descricao.strip()
    }

    data_list = load_data()
    data_list.append(new_item)
    save_data(data_list)

    return {
        "status": "success",
        "message": f"'{tipo_clean.capitalize()}' cadastrado com sucesso.",
        "item": new_item
    }

def list_events(date: str) -> dict:
    """Lista os eventos cadastrados.

    Args:
        date: A data específica para filtrar os eventos (formato YYYY-MM-DD)
              ou uma string vazia "" para listar todos os eventos cadastrados.

    Returns:
        dict: Um dicionário com o status da operação e a lista de eventos encontrados.
    """
    data_list = load_data()
    events = [item for item in data_list if item.get("tipo") == "evento"]
    
    date_filter = date.strip()
    if date_filter:
        events = [item for item in events if item.get("data") == date_filter]

    return {
        "status": "success",
        "events": events
    }

def list_tasks(date: str) -> dict:
    """Lista as tarefas cadastradas.

    Args:
        date: A data específica para filtrar as tarefas (formato YYYY-MM-DD)
              ou uma string vazia "" para listar todas as tarefas cadastradas.

    Returns:
        dict: Um dicionário com o status da operação e a lista de tarefas encontradas.
    """
    data_list = load_data()
    tasks = [item for item in data_list if item.get("tipo") == "tarefa"]

    date_filter = date.strip()
    if date_filter:
        tasks = [item for item in tasks if item.get("data") == date_filter]

    return {
        "status": "success",
        "tasks": tasks
    }

def delete_event_task(titulo: str, tipo: str) -> dict:
    """Remove uma tarefa ou evento cadastrado do banco de dados.

    Args:
        titulo: O título exato ou aproximado da tarefa ou evento a ser removido.
        tipo: O tipo do cadastro a ser removido, que deve ser 'evento' ou 'tarefa'.

    Returns:
        dict: Um dicionário contendo o status da operação e uma mensagem descritiva.
    """
    tipo_clean = tipo.lower().strip()
    if tipo_clean not in ["evento", "tarefa"]:
        return {
            "status": "error",
            "message": f"Tipo inválido: '{tipo}'. O tipo deve ser 'evento' ou 'tarefa'."
        }

    data_list = load_data()
    titulo_clean = titulo.lower().strip()
    
    new_data_list = []
    removed = False
    for item in data_list:
        if item.get("tipo") == tipo_clean and item.get("titulo", "").lower().strip() == titulo_clean:
            removed = True
            continue
        new_data_list.append(item)

    if not removed:
        return {
            "status": "error",
            "message": f"Nenhum {tipo_clean} encontrado com o título '{titulo}'."
        }

    save_data(new_data_list)
    return {
        "status": "success",
        "message": f"'{tipo_clean.capitalize()}' '{titulo}' removido com sucesso."
    }
