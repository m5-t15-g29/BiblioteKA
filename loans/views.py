from copies.models import Copie
from .models import Loan
from .serializers import LoanSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .errors import LoanBlockedError, CopiesInsusicient
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAccountOwnerOrIsSuperuser


class LoanView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Loan.objects.all()
        return Loan.objects.filter(user_id__pk=self.request.user.id)

    def perform_create(self, serializer):
        try:
            copie_filtered = Copie.objects.filter(book_id__pk=self.kwargs["pk"]).filter(
                is_loaned__exact=False
            )
            if not copie_filtered:
                raise CopiesInsusicient("This book has no copie available")
            if not self.request.user.is_loan_blocked:
                return serializer.save(copie=copie_filtered[0], user=self.request.user)
            raise LoanBlockedError("User does not have permission to loan books")
        except LoanBlockedError as err:
            return err.message


class LoanDetailedView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrIsSuperuser]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "loan_id"
