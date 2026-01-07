from aiogram import Router, types
from services.parser import parse_document
from services.excel_writer import ExcelWriter
from models import ExcelPayload

router = Router()

@router.message(types.ContentType.DOCUMENT)
@router.message(types.ContentType.PHOTO)
async def handle_file(message: types.Message):
    # 1️⃣ Проверка профиля
    telegram_id = message.from_user.id
    # TODO: достать User из БД
    user = None
    if not user:
        await message.reply("Сначала заполните профиль (/start)")
        return

    # 2️⃣ Скачивание файла
    file_path = f"tmp/{message.document.file_id}.pdf"  # или photo.jpg
    await message.document.download(file_path)

    # 3️⃣ Определяем тип документа
    file_type = "PDF" if message.content_type=="document" else "IMAGE"

    # 4️⃣ Парсим документ
    parsed = parse_document(file_path, file_type)
    if not parsed.success:
        await message.reply("Не удалось распознать документ. Проверьте файл.")
        return

    # 5️⃣ Формируем ExcelPayload
    payload = ExcelPayload(
        user_id=telegram_id,
        user_full_name=f"{user.last_name} {user.first_name} {user.middle_name}",
        position=user.position,
        employee_id=user.employee_id,
        trips=[parsed.trip]
    )

    # 6️⃣ Генерация Excel
    writer = ExcelWriter(template_path="template.xlsx")
    excel_path = writer.generate(payload)

    # 7️⃣ Отправка пользователю
    await message.answer_document(types.InputFile(excel_path), caption="Ваш отчёт готов ✅")
