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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoices_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.invoices_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="amount" /> | `number` | The price, in US dollars, of the Invoice Item. Equal to the unit price multiplied by quantity. |
| <CopyableCode code="from" /> | `string` | The date the Invoice Item started, based on month. |
| <CopyableCode code="label" /> | `string` | The Invoice Item's display label. |
| <CopyableCode code="quantity" /> | `integer` | The quantity of this Item for the specified Invoice. |
| <CopyableCode code="tax" /> | `number` | The amount of tax levied on this Item in US Dollars. |
| <CopyableCode code="to" /> | `string` | The date the Invoice Item ended, based on month. |
| <CopyableCode code="total" /> | `number` | The price of this Item after taxes in US Dollars. |
| <CopyableCode code="type" /> | `string` | The type of service, ether `hourly` or `misc`. |
| <CopyableCode code="unit_price" /> | `string` | The monthly service fee in US Dollars for this Item. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getInvoiceItems" /> | `SELECT` | <CopyableCode code="invoiceId" /> |
| <CopyableCode code="_getInvoiceItems" /> | `EXEC` | <CopyableCode code="invoiceId" /> |
