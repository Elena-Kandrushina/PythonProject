from src.masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция принимает аргумент — строку, содержащую тип и номер карты или счета и
    возвращает строку с замаскированным номером"""
    if "Счет" in account_card:
        mask_account_card = f"{account_card[:4]} **{account_card[-5:-1]}"
        return mask_account_card
    else:
        tip_card = f"{account_card[:-16]}"

        card_number = f"{account_card[-17:-1]}"
        card_number  = get_mask_card_number(card_number)
        mask_account_card = tip_card + card_number
        return mask_account_card



if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(date_t02: str) -> str:
    date_1 = f"{date_t02[:10]}"
    date_2 = f"{date_1[8:10]}{date_1[4:8]}{date_1[:4]}"

    return date_2


if __name__ == "__main__":
    print(get_date("2025-07-20T02:26:18.671407"))

