""" any dialog or text used in the program """

from modules.config import global_config_program

texts_es = {
    # HomeScreen texts
    "HS_your_text": "TEXTO",
    "HS_delay": "RETRASO",
    "HS_loops": "BUCLES",
    "HS_start": "INICIAR",
    "HS_process_done": "FINALIZADO",
    "HS_writing": "ESCRIBIENDO",
    # LargeScreen texts
    "LS_large_text": "TEXTO LARGO",
    "LS_ready": "LISTO",
    # SettingsScreen texts
    "SS_settings": "AJUSTES",
    "SS_time_to_start": "RETRASO",
    "SS_language": "LENGUAJE",
    "SS_theme": "TEMA",
    "SS_cancel": "CANCELAR",
    "SS_ok": "OK",
    "SS_info_ok": "Para aplicar los cambios, cierre y abra de nuevo el programa",
    # GENERIC texts
    "error": "ERROR",
    "info": "INFO",
    # Error texts
    "error_01": "ERROR 01: El campo 'texto' esta vacio",
}

texts_en = {
    # HomeScreen texts
    "HS_your_text": "YOUR TEXT",
    "HS_delay": "DELAY",
    "HS_loops": "LOOPS",
    "HS_start": "START",
    "HS_process_done": "DONE",
    "HS_writing": "WRITING",
    # LargeScreen texts
    "LS_large_text": "LARGE TEXT",
    "LS_ready": "READY",
    # SettingsScreen texts
    "SS_settings": "SETTINGS",
    "SS_time_to_start": "TIME TO START",
    "SS_language": "LANGUAGE",
    "SS_theme": "THEME",
    "SS_cancel": "CANCEL",
    "SS_ok": "OK",
    "SS_info_ok": "To apply the changes, close and reopen the program.",
    # GENERIC texts
    "error": "ERROR",
    "info": "INFO",
    # Error texts
    "error_01": "ERROR 01: Your text entry is empty",
}

def get_text(language: str) -> dict:
    """
    Select the language you chose in the initial
    setup and get a dictionary with all dialogs.
    """
    match language:
        case "es":
            return texts_es
        case "en":
            return texts_en
        case _:
            return texts_en

TOTAL_LANGUAGES = ["english", "español"]
TEXT = get_text(global_config_program["language"])
FONT = "Arial Black"
