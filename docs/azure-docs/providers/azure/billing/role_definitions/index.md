---
title: role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_definitions
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
<tr><td><b>Name</b></td><td><code>role_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.role_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of the a role definition. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the role definitions for a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the role definitions for a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="list_by_invoice_section" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the role definitions for an invoice section. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="_list_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Lists the role definitions for a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="_list_by_billing_profile" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the role definitions for a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="_list_by_invoice_section" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the role definitions for an invoice section. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="get_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName, billingRoleDefinitionName" /> | Gets the definition for a role on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="get_by_billing_profile" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleDefinitionName" /> | Gets the definition for a role on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="get_by_invoice_section" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleDefinitionName, invoiceSectionName" /> | Gets the definition for a role on an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
