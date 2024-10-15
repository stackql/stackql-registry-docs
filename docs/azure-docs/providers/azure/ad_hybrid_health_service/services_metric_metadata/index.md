---
title: services_metric_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - services_metric_metadata
  - ad_hybrid_health_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>services_metric_metadata</code> resource.

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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="metricName, serviceName" /> | Gets the service related metrics information. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the service related metrics information. |

## `SELECT` examples

Gets the service related metrics information.


```sql
SELECT
displayName,
groupings,
isDefault,
isDevOps,
isPerfCounter,
kind,
maxValue,
metricName,
metricsProcessorClassName,
minValue,
valueKind
FROM azure.ad_hybrid_health_service.services_metric_metadata
WHERE serviceName = '{{ serviceName }}';
```