---
title: services_metric_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - services_metric_metadata
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>services_metric_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_metric_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="displayName" /> | `string` | The display name for the metric. |
| <CopyableCode code="groupings" /> | `array` | The groupings for the metrics. |
| <CopyableCode code="isDefault" /> | `boolean` | Indicates if the metric is a default metric or not. |
| <CopyableCode code="isDevOps" /> | `boolean` | Indicates if the metric is visible to DevOps or not. |
| <CopyableCode code="isPerfCounter" /> | `boolean` | Indicates if the metric is a performance counter metric or not. |
| <CopyableCode code="kind" /> | `string` | Indicates whether the dashboard to represent the metric is a line, bar,pie, area or donut chart. |
| <CopyableCode code="maxValue" /> | `integer` | The maximum value. |
| <CopyableCode code="metricName" /> | `string` | The metric name |
| <CopyableCode code="metricsProcessorClassName" /> | `string` | The name of the class which retrieve and process the metric. |
| <CopyableCode code="minValue" /> | `integer` | The minimum value. |
| <CopyableCode code="valueKind" /> | `string` | Indicates if the metrics is a rate,value, percent or duration type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="metricName, serviceName" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="serviceName" /> |
