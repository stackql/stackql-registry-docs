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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.certificate_orders" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | AppServiceCertificateOrder resource specific properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Get a certificate order. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for List all certificate orders in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get certificate orders in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Create or update a certificate purchase order. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Delete an existing certificate order. |
| <CopyableCode code="reissue" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Reissue an existing certificate order. |
| <CopyableCode code="renew" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Renew an existing certificate order. |
| <CopyableCode code="resend_email" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Resend certificate email. |
| <CopyableCode code="resend_request_emails" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Resend domain verification ownership email containing steps on how to verify a domain for a given certificate order |
| <CopyableCode code="retrieve_certificate_actions" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Retrieve the list of certificate actions. |
| <CopyableCode code="retrieve_certificate_email_history" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Retrieve email history. |
| <CopyableCode code="retrieve_site_seal" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted by the reseller, to minimize delays for customer page load times. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Create or update a certificate purchase order. |
| <CopyableCode code="validate_purchase_information" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Validate information for a certificate order. |
| <CopyableCode code="verify_domain_ownership" /> | `EXEC` | <CopyableCode code="certificateOrderName, resourceGroupName, subscriptionId" /> | Description for Verify domain ownership for this certificate order. |
