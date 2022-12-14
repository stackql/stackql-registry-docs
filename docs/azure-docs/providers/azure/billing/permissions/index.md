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
| `notActions` | `array` | The set of actions that the caller is not allowed to perform. |
| `actions` | `array` | The set of actions that the caller is allowed to perform. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BillingPermissions_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the billing permissions the caller has on a billing account. |
| `BillingPermissions_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the billing permissions the caller has on a billing profile. |
| `BillingPermissions_ListByCustomer` | `SELECT` | `billingAccountName, customerName` | Lists the billing permissions the caller has for a customer. |
| `BillingPermissions_ListByInvoiceSections` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Lists the billing permissions the caller has on an invoice section. |
