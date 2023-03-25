---
title: invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices
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
<tr><td><b>Name</b></td><td><code>invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.billing.invoices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `links` | `object` |  |
| `meta` | `object` | Information about the response itself. |
| `invoice_preview` | `object` | The invoice preview. |
| `invoices` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_byUUID` | `SELECT` | `invoice_uuid` | To retrieve the invoice items for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID`. |
| `list` | `SELECT` |  | To retrieve a list of all invoices, send a GET request to `/v2/customers/my/invoices`. |
| `get_csvByUUID` | `EXEC` | `invoice_uuid` | To retrieve a CSV for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/csv`. |
| `get_pdfByUUID` | `EXEC` | `invoice_uuid` | To retrieve a PDF for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/pdf`. |
