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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.invoices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The Invoice's unique ID. |
| <CopyableCode code="date" /> | `string` | When this Invoice was generated. |
| <CopyableCode code="label" /> | `string` | The Invoice's display label. |
| <CopyableCode code="subtotal" /> | `number` | The amount of the Invoice before taxes in US Dollars. |
| <CopyableCode code="tax" /> | `number` | The amount of tax levied on the Invoice in US Dollars. |
| <CopyableCode code="tax_summary" /> | `array` | The amount of tax broken down into subtotals by source. |
| <CopyableCode code="total" /> | `number` | The amount of the Invoice after taxes in US Dollars. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getInvoice" /> | `SELECT` | <CopyableCode code="invoiceId" /> | Returns a single Invoice object. |
| <CopyableCode code="getInvoices" /> | `SELECT` |  | Returns a paginated list of Invoices against your Account.<br /> |
| <CopyableCode code="_getInvoice" /> | `EXEC` | <CopyableCode code="invoiceId" /> | Returns a single Invoice object. |
| <CopyableCode code="_getInvoices" /> | `EXEC` |  | Returns a paginated list of Invoices against your Account.<br /> |
