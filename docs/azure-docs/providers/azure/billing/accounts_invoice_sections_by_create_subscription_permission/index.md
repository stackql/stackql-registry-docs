---
title: accounts_invoice_sections_by_create_subscription_permission
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_invoice_sections_by_create_subscription_permission
  - billing
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
<tr><td><b>Name</b></td><td><code>accounts_invoice_sections_by_create_subscription_permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.accounts_invoice_sections_by_create_subscription_permission" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billingProfileDisplayName" /> | `string` | The name of the billing profile for the invoice section. |
| <CopyableCode code="billingProfileId" /> | `string` | The ID of the billing profile for the invoice section. |
| <CopyableCode code="billingProfileSpendingLimit" /> | `string` | The billing profile spending limit. |
| <CopyableCode code="billingProfileStatus" /> | `string` | The status of the billing profile. |
| <CopyableCode code="billingProfileStatusReasonCode" /> | `string` | Reason for the specified billing profile status. |
| <CopyableCode code="billingProfileSystemId" /> | `string` | The system generated unique identifier for a billing profile. |
| <CopyableCode code="enabledAzurePlans" /> | `array` | Enabled azure plans for the associated billing profile. |
| <CopyableCode code="invoiceSectionDisplayName" /> | `string` | The name of the invoice section. |
| <CopyableCode code="invoiceSectionId" /> | `string` | The ID of the invoice section. |
| <CopyableCode code="invoiceSectionSystemId" /> | `string` | The system generated unique identifier for an invoice section. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName" /> |
