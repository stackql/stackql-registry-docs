---
title: invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices
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
<tr><td><b>Name</b></td><td><code>invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing.invoices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The properties of the invoice. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `billingAccountName, invoiceName` | Gets an invoice by billing account name and ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `list_by_billing_account` | `SELECT` | `billingAccountName, periodEndDate, periodStartDate` | Lists the invoices for a billing account for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `list_by_billing_profile` | `SELECT` | `billingAccountName, billingProfileName, periodEndDate, periodStartDate` | Lists the invoices for a billing profile for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `list_by_billing_subscription` | `SELECT` | `periodEndDate, periodStartDate, subscriptionId` | Lists the invoices for a subscription. |
| `_list_by_billing_account` | `EXEC` | `billingAccountName, periodEndDate, periodStartDate` | Lists the invoices for a billing account for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `_list_by_billing_profile` | `EXEC` | `billingAccountName, billingProfileName, periodEndDate, periodStartDate` | Lists the invoices for a billing profile for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `_list_by_billing_subscription` | `EXEC` | `periodEndDate, periodStartDate, subscriptionId` | Lists the invoices for a subscription. |
| `download_billing_subscription_invoice` | `EXEC` | `downloadToken, invoiceName, subscriptionId` | Gets a URL to download an invoice. |
| `download_invoice` | `EXEC` | `billingAccountName, downloadToken, invoiceName` | Gets a URL to download an invoice. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `download_multiple_billing_profile_invoices` | `EXEC` | `billingAccountName` | Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `download_multiple_billing_subscription_invoices` | `EXEC` | `subscriptionId` | Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. |
| `get_by_id` | `EXEC` | `invoiceName` | Gets an invoice by ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `get_by_subscription_and_invoice_id` | `EXEC` | `invoiceName, subscriptionId` | Gets an invoice by subscription ID and invoice ID. |
