---
title: invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices
  - account
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.invoices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The Invoice's unique ID. |
| `total` | `number` | The amount of the Invoice after taxes in US Dollars. |
| `date` | `string` | When this Invoice was generated. |
| `label` | `string` | The Invoice's display label. |
| `subtotal` | `number` | The amount of the Invoice before taxes in US Dollars. |
| `tax` | `number` | The amount of tax levied on the Invoice in US Dollars. |
| `tax_summary` | `array` | The amount of tax broken down into subtotals by source. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getInvoice` | `SELECT` | `invoiceId` | Returns a single Invoice object. |
| `getInvoices` | `SELECT` |  | Returns a paginated list of Invoices against your Account.<br /> |
| `_getInvoice` | `EXEC` | `invoiceId` | Returns a single Invoice object. |
| `_getInvoices` | `EXEC` |  | Returns a paginated list of Invoices against your Account.<br /> |
