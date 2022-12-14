---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The properties of a product. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Products_Get` | `SELECT` | `billingAccountName, productName` | Gets a product by ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `Products_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the products for a billing account. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| `Products_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the products for a billing profile. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| `Products_ListByCustomer` | `SELECT` | `billingAccountName, customerName` | Lists the products for a customer. These don't include products billed based on usage.The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| `Products_ListByInvoiceSection` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Lists the products for an invoice section. These don't include products billed based on usage. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `Products_Move` | `EXEC` | `billingAccountName, productName` | Moves a product's charges to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement. |
| `Products_Update` | `EXEC` | `billingAccountName, productName` | Updates the properties of a Product. Currently, auto renew can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `Products_ValidateMove` | `EXEC` | `billingAccountName, productName` | Validates if a product's charges can be moved to a new invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement. |
