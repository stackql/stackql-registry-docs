---
title: invoices_items
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices_items
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
<tr><td><b>Name</b></td><td><code>invoices_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.invoices_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `type` | `string` | The type of service, ether `hourly` or `misc`. |
| `quantity` | `integer` | The quantity of this Item for the specified Invoice. |
| `total` | `number` | The price of this Item after taxes in US Dollars. |
| `to` | `string` | The date the Invoice Item ended, based on month. |
| `from` | `string` | The date the Invoice Item started, based on month. |
| `label` | `string` | The Invoice Item's display label. |
| `unit_price` | `string` | The monthly service fee in US Dollars for this Item. |
| `amount` | `number` | The price, in US dollars, of the Invoice Item. Equal to the unit price multiplied by quantity. |
| `tax` | `number` | The amount of tax levied on this Item in US Dollars. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getInvoiceItems` | `SELECT` | `invoiceId` |
| `_getInvoiceItems` | `EXEC` | `invoiceId` |
