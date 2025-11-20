
class RBWallets:
    def __init__(self, wallet_id: int | None = None, uuid: int | None = None, amount: int | None = None):
        self.id = wallet_id
        self.uuid = uuid
        self.amount = amount

    def to_dict(self) -> dict:
        data = {'id': self.id, 'uuid': self.uuid, 'amount': self.amount}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
