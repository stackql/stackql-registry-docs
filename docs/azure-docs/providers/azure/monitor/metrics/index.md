---
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
  - monitor
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

Creates, updates, deletes, gets or lists a <code>metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.metrics" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="interval, metricName, resourceUri, timespan" /> | **Lists the metric values for a resource**. |

## `SELECT` examples

**Lists the metric values for a resource**.


```sql
SELECT
id,
name,
displayDescription,
errorCode,
errorMessage,
timeseries,
type,
unit
FROM azure.monitor.metrics
WHERE interval = '{{ interval }}'
AND metricName = '{{ metricName }}'
AND resourceUri = '{{ resourceUri }}'
AND timespan = '{{ timespan }}';
```