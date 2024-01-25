---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
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
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `actions` | `array` | The set of actions that the caller is allowed to perform. |
| `notActions` | `array` | The set of actions that the caller is not allowed to perform. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_billing_account` | `SELECT` | `billingAccountName` | Lists the billing permissions the caller has on a billing account. |
| `list_by_billing_profile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the billing permissions the caller has on a billing profile. |
| `list_by_customer` | `SELECT` | `billingAccountName, customerName` | Lists the billing permissions the caller has for a customer. |
| `list_by_invoice_sections` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Lists the billing permissions the caller has on an invoice section. |
| `_list_by_billing_account` | `EXEC` | `billingAccountName` | Lists the billing permissions the caller has on a billing account. |
| `_list_by_billing_profile` | `EXEC` | `billingAccountName, billingProfileName` | Lists the billing permissions the caller has on a billing profile. |
| `_list_by_customer` | `EXEC` | `billingAccountName, customerName` | Lists the billing permissions the caller has for a customer. |
| `_list_by_invoice_sections` | `EXEC` | `billingAccountName, billingProfileName, invoiceSectionName` | Lists the billing permissions the caller has on an invoice section. |
