---
title: invoices_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices_summary
  - billing
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoices_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.billing.invoices_summary</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `product_charges` | `object` | A summary of the product usage charges contributing to the invoice.  This will include an amount, and grouped aggregates by resource type  under the `items` key. |
| `taxes` | `object` | A summary of the taxes contributing to the invoice. |
| `invoice_uuid` | `string` | UUID of the invoice |
| `overages` | `object` | A summary of the overages contributing to the invoice. |
| `user_company` | `string` | Company of the DigitalOcean customer being invoiced, if set. |
| `user_name` | `string` | Name of the DigitalOcean customer being invoiced. |
| `credits_and_adjustments` | `object` | A summary of the credits and adjustments contributing to the invoice. |
| `user_billing_address` | `object` | The billing address of the customer being invoiced. |
| `amount` | `string` | Total amount of the invoice, in USD.  This will reflect month-to-date usage in the invoice preview. |
| `billing_period` | `string` | Billing period of usage for which the invoice is issued, in `YYYY-MM`  format. |
| `user_email` | `string` | Email of the DigitalOcean customer being invoiced. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `invoices_get_summaryByUUID` | `SELECT` | `invoice_uuid` |
