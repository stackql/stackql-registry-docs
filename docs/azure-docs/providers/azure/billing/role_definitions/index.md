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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.role_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The properties of the a role definition. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BillingRoleDefinitions_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the role definitions for a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleDefinitions_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the role definitions for a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleDefinitions_ListByInvoiceSection` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Lists the role definitions for an invoice section. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleDefinitions_GetByBillingAccount` | `EXEC` | `billingAccountName, billingRoleDefinitionName` | Gets the definition for a role on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleDefinitions_GetByBillingProfile` | `EXEC` | `billingAccountName, billingProfileName, billingRoleDefinitionName` | Gets the definition for a role on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `BillingRoleDefinitions_GetByInvoiceSection` | `EXEC` | `billingAccountName, billingProfileName, billingRoleDefinitionName, invoiceSectionName` | Gets the definition for a role on an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
