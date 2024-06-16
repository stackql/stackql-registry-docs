---
title: metrics_at_subscription_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_at_subscription_scope
  - monitor
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_at_subscription_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.metrics_at_subscription_scope" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The metric Id. |
| <CopyableCode code="name" /> | `object` | The localizable string class. |
| <CopyableCode code="displayDescription" /> | `string` | Detailed description of this metric. |
| <CopyableCode code="errorCode" /> | `string` | 'Success' or the error details on query failures for this metric. |
| <CopyableCode code="errorMessage" /> | `string` | Error message encountered querying this specific metric. |
| <CopyableCode code="timeseries" /> | `array` | The time series returned when a data query is performed. |
| <CopyableCode code="type" /> | `string` | The resource type of the metric resource. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="region, subscriptionId" /> |
