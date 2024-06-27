# import libraries
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
endpoint = os.environ["AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT"]
key = os.environ["AZURE_DOCUMENT_INTELLIGENCE_KEY"]
document_file_path = './Closing-Disclosure-Form-Sample.pdf'

def analyze_closing_disclosures():
    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    with open(document_file_path, "rb") as f:
        # Use begin_analyze_document to start the analysis process
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-mortgage.us.closingDisclosure", analyze_request=f, content_type="application/octet-stream"
        )
    closing_disclosures = poller.result()

    if closing_disclosures.documents:
        for idx, closing_disclosure in enumerate(closing_disclosures.documents):
            print(f"--------Analyzing Closing Disclosure #{idx + 1}--------")
            closing = closing_disclosure.fields.get("Closing")
            if closing:
                print("Closing data:")
                closing_date = closing.get("valueObject").get("ClosingDate")
                if closing_date:
                    print(f"...Closing Date: {closing_date.get('content')} has confidence: {closing_date.confidence}")
                disbursement_date = closing.get("valueObject").get("DisbursementDate")
                if disbursement_date:
                    print(f"...Disbursement Date: {disbursement_date.get('content')} has confidence: {disbursement_date.confidence}")
                file_number = closing.get("valueObject").get("FileNumber")
                if file_number:
                    print(f"...File Number: {file_number.get('content')} has confidence: {file_number.confidence}")
                issue_date = closing.get("valueObject").get("IssueDate")
                if issue_date:
                    print(f"...Issue Date: {issue_date.get('content')} has confidence: {issue_date.confidence}")
                property_address = closing.get("valueObject").get("PropertyAddress")
                if property_address:
                    print(f"...Property Address: {property_address.get('content')} has confidence: {property_address.confidence}")
                sale_price = closing.get("valueObject").get("SalePrice")
                if sale_price:
                    print(f"...Sale Price: {sale_price.get('content')} has confidence: {sale_price.confidence}")
                settlement_agent = closing.get("valueObject").get("SettlementAgent")
                if settlement_agent:
                    print(f"...Settlement Agent: {settlement_agent.get('content')} has confidence: {settlement_agent.confidence}")
            loan = closing_disclosure.fields.get("Loan")
            if loan:
                print("Loan data:")
                amount = loan.get("valueObject").get("Amount")
                if amount:
                    print(f"...Amount: {amount.get('content')} has confidence: {amount.confidence}")
                estimated_tax_insurance_and_assessments_per_month = loan.get("valueObject").get("EstimatedTaxInsuranceAndAssessmentsPerMonth")
                if estimated_tax_insurance_and_assessments_per_month:
                    print(f"...Estimated Tax, Insurance, and Assessments Per Month: {estimated_tax_insurance_and_assessments_per_month.get('content')} has confidence: {estimated_tax_insurance_and_assessments_per_month.confidence}")
                identification_number = loan.get("valueObject").get("IdentificationNumber")
                if identification_number:
                    print(f"...Identification Number: {identification_number.get('content')} has confidence: {identification_number.confidence}")
                interest_rate = loan.get("valueObject").get("InterestRate")
                if interest_rate:
                    print(f"...Interest Rate: {interest_rate.get('content')} has confidence: {interest_rate.confidence}")
                monthly_principal_and_interest = loan.get("valueObject").get("MonthlyPrincipalAndInterest")
                if monthly_principal_and_interest:
                    print(f"...Monthly Principal and Interest: {monthly_principal_and_interest.get('content')} has confidence: {monthly_principal_and_interest.confidence}")
                mortgage_insurance_case_number = loan.get("valueObject").get("MortgageInsuranceCaseNumber")
                if mortgage_insurance_case_number:
                    print(f"...Mortgage Insurance Case Number: {mortgage_insurance_case_number.get('content')} has confidence: {mortgage_insurance_case_number.confidence}")
                product = loan.get("valueObject").get("Product")
                if product:
                    print(f"...Product: {product.get('content')} has confidence: {product.confidence}")
                purpose = loan.get("valueObject").get("Purpose")
                if purpose:
                    print(f"...Purpose: {purpose.get('content')} has confidence: {purpose.confidence}")
                term = loan.get("valueObject").get("Term")
                if term:
                    print(f"...Term: {term.get('content')} has confidence: {term.confidence}")
                type_ = loan.get("valueObject").get("Type")
                if type_:
                    print(f"...Type: {type_.get('valueSelectionGroup')} has confidence: {type_.confidence}")
            transaction = closing_disclosure.fields.get("Transaction")
            if transaction:
                print("Transaction data:")
                borrower_address = transaction.get("valueObject").get("BorrowerAddress")
                if borrower_address:
                    address_content = borrower_address.get('content').replace("\n", " ")
                    print(f"...Borrower Address: {address_content} has confidence: {borrower_address.confidence}")
                borrower_cash_to_close_amount = transaction.get("valueObject").get("BorrowerCashToCloseAmount")
                if borrower_cash_to_close_amount:
                    print(f"...Borrower Cash to Close Amount: {borrower_cash_to_close_amount.get('content')} has confidence: {borrower_cash_to_close_amount.confidence}")
                borrower_closing_costs = transaction.get("valueObject").get("BorrowerClosingCosts")
                if borrower_closing_costs:
                    print(f"...Borrower Closing Costs: {borrower_closing_costs.get('content')} has confidence: {borrower_closing_costs.confidence}")
                borrower_name = transaction.get("valueObject").get("BorrowerName")
                if borrower_name:
                    print(f"...Borrower Name: {borrower_name.get('content')} has confidence: {borrower_name.confidence}")
                lender_name = transaction.get("valueObject").get("LenderName")
                if lender_name:
                    print(f"...Lender Name: {lender_name.get('content')} has confidence: {lender_name.confidence}")
                seller_address = transaction.get("valueObject").get("SellerAddress")
                if seller_address:
                    address_content = seller_address.get('content').replace("\n", " ")
                    print(f"...Seller Address: {address_content} has confidence: {seller_address.confidence}")
                seller_cash_to_close_amount = transaction.get("valueObject").get("SellerCashToCloseAmount")
                if seller_cash_to_close_amount:
                    print(f"...Seller Cash to Close Amount: {seller_cash_to_close_amount.get('content')} has confidence: {seller_cash_to_close_amount.confidence}")
                seller_name = transaction.get("valueObject").get("SellerName")
                if seller_name:
                    print(f"...Seller Name: {seller_name.get('content')} has confidence: {seller_name.confidence}")
                borrower_cash_to_close_type = transaction.get("valueObject").get("BorrowerCashToCloseType")
                if borrower_cash_to_close_type:
                    print(f"...Borrower Cash to Close Type: {borrower_cash_to_close_type.get('valueSelectionGroup')} has confidence: {borrower_cash_to_close_type.confidence}")
                seller_cash_to_close_type = transaction.get("valueObject").get("SellerCashToCloseType")
                if seller_cash_to_close_type:
                    print(f"...Seller Cash to Close Type: {seller_cash_to_close_type.get('valueSelectionGroup')} has confidence: {seller_cash_to_close_type.confidence}")
        
if __name__ == "__main__":
    analyze_closing_disclosures()