---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The billing properties of a subscription. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BillingSubscriptions_Get` | `SELECT` | `billingAccountName, subscriptionId` | Gets a subscription by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. |
| `BillingSubscriptions_ListByBillingAccount` | `SELECT` | `billingAccountName` | Lists the subscriptions for a billing account. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| `BillingSubscriptions_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName` | Lists the subscriptions that are billed to a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| `BillingSubscriptions_ListByCustomer` | `SELECT` | `billingAccountName, customerName` | Lists the subscriptions for a customer. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| `BillingSubscriptions_ListByInvoiceSection` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Lists the subscriptions that are billed to an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `BillingSubscriptions_Move` | `EXEC` | `billingAccountName, subscriptionId, data__destinationInvoiceSectionId` | Moves a subscription's charges to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| `BillingSubscriptions_Update` | `EXEC` | `billingAccountName, subscriptionId` | Updates the properties of a billing subscription. Currently, cost center can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| `BillingSubscriptions_ValidateMove` | `EXEC` | `billingAccountName, subscriptionId, data__destinationInvoiceSectionId` | Validates if a subscription's charges can be moved to a new invoice section. This operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
