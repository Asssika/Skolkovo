from typing import List

from fastapi import APIRouter
from app.wallets.dao import WalletsDAO
from app.wallets.schemas import SWallets, SWalletsAdd, SWalletsUpdate

router = APIRouter(prefix='/wallets', tags=['Работа со счетами'])


@router.get('/all_wallets', summary='Получение всех счетов')
async def get_all_wallets() -> List[SWallets]:
    return await WalletsDAO.find_all()


@router.get('/{id}', summary='Получение конкретного счета')
async def get_wallet_by_id(wallet_id: int) -> SWallets | dict:
    rez = await WalletsDAO.find_by_id(wallet_id)
    if not rez:
        return {'message': f'user with id {wallet_id} not find'}
    return rez


@router.post('/add')
async def post_wallet(wallet: SWalletsAdd):
    return await WalletsDAO.add(**wallet.dict())


@router.put("/update_description/")
async def update_major_description(wallet: SWalletsUpdate) -> dict:
    check = await WalletsDAO.update(filter_by={'uuid': wallet.uuid}, amount=wallet.amount)
    if check:
        return {"message": "Сумма кошелька успешно обновлена!", "amount": wallet.amount}
    else:
        return {"message": "Ошибка при обновлении суммы кошелька!"}