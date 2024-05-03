---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
  - orders
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.orders.orders" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domains" /> | `array` | A collection of domain names purchased if the current product is domain |
| <CopyableCode code="label" /> | `string` | Human readable description of the current product |
| <CopyableCode code="period" /> | `number` |  |
| <CopyableCode code="periodUnit" /> | `string` | The unit of time that periodCount is measured in |
| <CopyableCode code="pfid" /> | `integer` | Unique identifier of the current product |
| <CopyableCode code="pricing" /> | `object` |  |
| <CopyableCode code="quantity" /> | `integer` | Number of the current product included in the specified order |
| <CopyableCode code="taxCollector" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="order_id" /> |
| <CopyableCode code="list" /> | `SELECT` |  |
| <CopyableCode code="_list" /> | `EXEC` |  |
