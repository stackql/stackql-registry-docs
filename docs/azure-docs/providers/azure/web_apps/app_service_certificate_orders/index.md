---
title: app_service_certificate_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - app_service_certificate_orders
  - web_apps
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_service_certificate_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.app_service_certificate_orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `kind` | `string` | Kind of resource. |
| `location` | `string` | Resource Location. |
| `properties` | `object` | AppServiceCertificateOrder resource specific properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AppServiceCertificateOrders_Get` | `SELECT` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Get a certificate order. |
| `AppServiceCertificateOrders_List` | `SELECT` | `subscriptionId` | Description for List all certificate orders in a subscription. |
| `AppServiceCertificateOrders_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get certificate orders in a resource group. |
| `AppServiceCertificateOrders_CreateOrUpdate` | `INSERT` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Create or update a certificate purchase order. |
| `AppServiceCertificateOrders_Delete` | `DELETE` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Delete an existing certificate order. |
| `AppServiceCertificateOrders_CreateOrUpdateCertificate` | `EXEC` | `certificateOrderName, name, resourceGroupName, subscriptionId` | Description for Creates or updates a certificate and associates with key vault secret. |
| `AppServiceCertificateOrders_DeleteCertificate` | `EXEC` | `certificateOrderName, name, resourceGroupName, subscriptionId` | Description for Delete the certificate associated with a certificate order. |
| `AppServiceCertificateOrders_GetCertificate` | `EXEC` | `certificateOrderName, name, resourceGroupName, subscriptionId` | Description for Get the certificate associated with a certificate order. |
| `AppServiceCertificateOrders_ListCertificates` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for List all certificates associated with a certificate order. |
| `AppServiceCertificateOrders_Reissue` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Reissue an existing certificate order. |
| `AppServiceCertificateOrders_Renew` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Renew an existing certificate order. |
| `AppServiceCertificateOrders_ResendEmail` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Resend certificate email. |
| `AppServiceCertificateOrders_ResendRequestEmails` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Resend domain verification ownership email containing steps on how to verify a domain for a given certificate order |
| `AppServiceCertificateOrders_RetrieveCertificateActions` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Retrieve the list of certificate actions. |
| `AppServiceCertificateOrders_RetrieveCertificateEmailHistory` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Retrieve email history. |
| `AppServiceCertificateOrders_RetrieveSiteSeal` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted by the reseller, to minimize delays for customer page load times. |
| `AppServiceCertificateOrders_Update` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Create or update a certificate purchase order. |
| `AppServiceCertificateOrders_UpdateCertificate` | `EXEC` | `certificateOrderName, name, resourceGroupName, subscriptionId` | Description for Creates or updates a certificate and associates with key vault secret. |
| `AppServiceCertificateOrders_ValidatePurchaseInformation` | `EXEC` | `subscriptionId` | Description for Validate information for a certificate order. |
| `AppServiceCertificateOrders_VerifyDomainOwnership` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Verify domain ownership for this certificate order. |
