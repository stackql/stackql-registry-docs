---
title: certificate_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_orders
  - app_service
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
<tr><td><b>Name</b></td><td><code>certificate_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.certificate_orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | AppServiceCertificateOrder resource specific properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Get a certificate order. |
| `list` | `SELECT` | `subscriptionId` | Description for List all certificate orders in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get certificate orders in a resource group. |
| `create_or_update` | `INSERT` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Create or update a certificate purchase order. |
| `delete` | `DELETE` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Delete an existing certificate order. |
| `_list` | `EXEC` | `subscriptionId` | Description for List all certificate orders in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Get certificate orders in a resource group. |
| `reissue` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Reissue an existing certificate order. |
| `renew` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Renew an existing certificate order. |
| `resend_email` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Resend certificate email. |
| `resend_request_emails` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Resend domain verification ownership email containing steps on how to verify a domain for a given certificate order |
| `retrieve_certificate_actions` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Retrieve the list of certificate actions. |
| `retrieve_certificate_email_history` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Retrieve email history. |
| `retrieve_site_seal` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted by the reseller, to minimize delays for customer page load times. |
| `update` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Create or update a certificate purchase order. |
| `validate_purchase_information` | `EXEC` | `subscriptionId` | Description for Validate information for a certificate order. |
| `verify_domain_ownership` | `EXEC` | `certificateOrderName, resourceGroupName, subscriptionId` | Description for Verify domain ownership for this certificate order. |
