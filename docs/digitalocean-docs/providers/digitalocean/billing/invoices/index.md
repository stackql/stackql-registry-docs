---
title: invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices
  - billing
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>invoices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.billing.invoices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Description of the invoice item. |
| <CopyableCode code="amount" /> | `string` | Billed amount of this invoice item. Billed in USD. |
| <CopyableCode code="duration" /> | `string` | Duration of time this invoice item was used and subsequently billed. |
| <CopyableCode code="duration_unit" /> | `string` | Unit of time for duration. |
| <CopyableCode code="end_time" /> | `string` | Time the invoice item stopped being billed for usage. |
| <CopyableCode code="group_description" /> | `string` | Description of the invoice item when it is a grouped set of usage, such as DOKS or databases. |
| <CopyableCode code="product" /> | `string` | Name of the product being billed in the invoice item. |
| <CopyableCode code="project_name" /> | `string` | Name of the DigitalOcean Project this resource belongs to. |
| <CopyableCode code="resource_id" /> | `string` | ID of the resource billing in the invoice item if available. |
| <CopyableCode code="resource_uuid" /> | `string` | UUID of the resource billing in the invoice item if available. |
| <CopyableCode code="start_time" /> | `string` | Time the invoice item began to be billed for usage. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="invoices_get_by_uuid" /> | `SELECT` | <CopyableCode code="invoice_uuid" /> | To retrieve the invoice items for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID`. |
| <CopyableCode code="invoices_list" /> | `SELECT` | <CopyableCode code="" /> | To retrieve a list of all invoices, send a GET request to `/v2/customers/my/invoices`. |
| <CopyableCode code="invoices_get_csv_by_uuid" /> | `EXEC` | <CopyableCode code="invoice_uuid" /> | To retrieve a CSV for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/csv`. |
| <CopyableCode code="invoices_get_pdf_by_uuid" /> | `EXEC` | <CopyableCode code="invoice_uuid" /> | To retrieve a PDF for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/pdf`. |

## `SELECT` examples

To retrieve a list of all invoices, send a GET request to `/v2/customers/my/invoices`.


```sql
SELECT
description,
amount,
duration,
duration_unit,
end_time,
group_description,
product,
project_name,
resource_id,
resource_uuid,
start_time
FROM digitalocean.billing.invoices
;
```