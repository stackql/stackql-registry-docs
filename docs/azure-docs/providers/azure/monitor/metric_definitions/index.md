---
title: metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_definitions
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
<tr><td><b>Name</b></td><td><code>metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.metric_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier of the metric definition. |
| <CopyableCode code="name" /> | `object` | The localizable string class. |
| <CopyableCode code="category" /> | `string` | Custom category name for this metric. |
| <CopyableCode code="dimensions" /> | `array` | The name and the display name of the dimension, i.e. it is a localizable string. |
| <CopyableCode code="displayDescription" /> | `string` | Detailed description of this metric. |
| <CopyableCode code="isDimensionRequired" /> | `boolean` | Flag to indicate whether the dimension is required. |
| <CopyableCode code="metricAvailabilities" /> | `array` | The collection of what aggregation intervals are available to be queried. |
| <CopyableCode code="metricClass" /> | `string` | The class of the metric. |
| <CopyableCode code="namespace" /> | `string` | The namespace the metric belongs to. |
| <CopyableCode code="primaryAggregationType" /> | `string` | The aggregation type of the metric. |
| <CopyableCode code="resourceId" /> | `string` | The resource identifier of the resource that emitted the metric. |
| <CopyableCode code="supportedAggregationTypes" /> | `array` | The collection of what aggregation types are supported. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceUri" /> |
