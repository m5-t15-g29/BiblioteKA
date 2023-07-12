from users.models import User
from datetime import datetime
from loans.models import Loan
from users.models import User


def verify_if_user_can_loan():
    users = User.objects.all()
    now = datetime.now()
    for user in users:
        loans = Loan.objects.filter(user_id__exact=user.id)
        is_loan_blocked = any(loan.return_date.day < now.day for loan in loans)
        if is_loan_blocked != user.is_loan_blocked:
            user.is_loan_blocked = is_loan_blocked
            user.save()
