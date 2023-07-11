from copies.models import Copie
from .models import Loan
from .serializers import LoanSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .errors import LoanBlockedError


class LoanView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        try:
            copie_filtered = Copie.objects.filter(book_id__pk=self.kwargs["pk"]).filter(
                is_loaned__exact=False
            )
            print(copie_filtered)
            if not self.request.user.is_loan_blocked:
                return serializer.save(copie=copie_filtered[0], user=self.request.user)
            else:
                raise LoanBlockedError("User does not have permission to loan books")
        except Copie.DoesNotExist:
            return
        except LoanBlockedError as err:
            return err.message


class LoanDetailedView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "loan_id"
