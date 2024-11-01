---
title: costs
hide_title: false
hide_table_of_contents: false
keywords:
  - costs
  - billing
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>costs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.billing.costs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="amount" /> | `number` | Final amount after deducting discounts. |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="discount_amount" /> | `number` | Amount discounted from the original amount in dollars. |
| <CopyableCode code="end_date" /> | `string` | End date of time period (exclusive) to retrieve billing costs. It is represented in RFC3339 format and is in UTC. |
| <CopyableCode code="granularity" /> | `string` | Granularity at which each line item is aggregated. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="line_type" /> | `string` | Type of the line item. |
| <CopyableCode code="network_access_type" /> | `string` | Network access type for the cluster. |
| <CopyableCode code="original_amount" /> | `number` | Original amount accrued for this line item. |
| <CopyableCode code="price" /> | `number` | Price for the line item in dollars. |
| <CopyableCode code="product" /> | `string` | Product name. |
| <CopyableCode code="quantity" /> | `number` | Quantity of the line item. |
| <CopyableCode code="resource" /> | `object` | The resource for a given object |
| <CopyableCode code="start_date" /> | `string` | Start date of time period (inclusive) to retrieve billing costs. It is represented in RFC3339 format and is in UTC. |
| <CopyableCode code="unit" /> | `string` | Unit of the line item. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_billing_v1costs" /> | `SELECT` | <CopyableCode code="end_date, start_date" /> |
