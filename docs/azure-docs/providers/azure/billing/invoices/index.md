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
| `Invoices_Get` | `SELECT` | `billingAccountName, invoiceName` | Gets an invoice by billing account name and ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_ListByBillingAccount` | `SELECT` | `billingAccountName, periodEndDate, periodStartDate` | Lists the invoices for a billing account for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_ListByBillingProfile` | `SELECT` | `billingAccountName, billingProfileName, periodEndDate, periodStartDate` | Lists the invoices for a billing profile for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_ListByBillingSubscription` | `SELECT` | `periodEndDate, periodStartDate, subscriptionId` | Lists the invoices for a subscription. |
| `Invoices_DownloadBillingSubscriptionInvoice` | `EXEC` | `downloadToken, invoiceName, subscriptionId` | Gets a URL to download an invoice. |
| `Invoices_DownloadInvoice` | `EXEC` | `billingAccountName, downloadToken, invoiceName` | Gets a URL to download an invoice. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_DownloadMultipleBillingProfileInvoices` | `EXEC` | `billingAccountName` | Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_DownloadMultipleBillingSubscriptionInvoices` | `EXEC` | `subscriptionId` | Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. |
| `Invoices_GetById` | `EXEC` | `invoiceName` | Gets an invoice by ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| `Invoices_GetBySubscriptionAndInvoiceId` | `EXEC` | `invoiceName, subscriptionId` | Gets an invoice by subscription ID and invoice ID. |
