from bot.models import ParsedResult, Trip

def parse_document(file_path: str, file_type: str) -> ParsedResult:
    """
    Заглушка для OpenAI-парсера.
    file_type: PDF | IMAGE
    Возвращает ParsedResult
    """
    # TODO: здесь интегрируем OpenAI
    # Пример возврата для теста:
    dummy_trip = Trip(
        trip_type="FLIGHT" if file_type=="PDF" else "AEROEXPRESS",
        segments=[]
    )
    return ParsedResult(success=True, trip=dummy_trip)
