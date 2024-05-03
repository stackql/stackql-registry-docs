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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.billing.invoices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="invoice_preview" /> | `object` | The invoice preview. |
| <CopyableCode code="invoices" /> | `array` |  |
| <CopyableCode code="links" /> | `object` |  |
| <CopyableCode code="meta" /> | `object` | Information about the response itself. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_byUUID" /> | `SELECT` | <CopyableCode code="invoice_uuid" /> | To retrieve the invoice items for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID`. |
| <CopyableCode code="list" /> | `SELECT` |  | To retrieve a list of all invoices, send a GET request to `/v2/customers/my/invoices`. |
| <CopyableCode code="get_csvByUUID" /> | `EXEC` | <CopyableCode code="invoice_uuid" /> | To retrieve a CSV for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/csv`. |
| <CopyableCode code="get_pdfByUUID" /> | `EXEC` | <CopyableCode code="invoice_uuid" /> | To retrieve a PDF for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/pdf`. |
