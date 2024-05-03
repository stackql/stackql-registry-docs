---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
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
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.role_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of the role assignment. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the role assignments for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the role assignments for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="list_by_invoice_section" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the role assignments for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="delete_by_billing_account" /> | `DELETE` | <CopyableCode code="billingAccountName, billingRoleAssignmentName" /> | Deletes a role assignment for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="delete_by_billing_profile" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName" /> | Deletes a role assignment for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="delete_by_invoice_section" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName, invoiceSectionName" /> | Deletes a role assignment for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="_list_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Lists the role assignments for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="_list_by_billing_profile" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the role assignments for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="_list_by_invoice_section" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the role assignments for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="get_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName, billingRoleAssignmentName" /> | Gets a role assignment for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="get_by_billing_profile" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName" /> | Gets a role assignment for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="get_by_invoice_section" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, billingRoleAssignmentName, invoiceSectionName" /> | Gets a role assignment for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
