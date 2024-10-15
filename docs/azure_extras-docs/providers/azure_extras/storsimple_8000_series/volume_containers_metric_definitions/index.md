---
title: volume_containers_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_containers_metric_definitions
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>volume_containers_metric_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_containers_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.volume_containers_metric_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The metric name. |
| <CopyableCode code="category" /> | `string` | The category of the metric. |
| <CopyableCode code="dimensions" /> | `array` | The available metric dimensions. |
| <CopyableCode code="metricAvailabilities" /> | `array` | The available metric granularities. |
| <CopyableCode code="primaryAggregationType" /> | `string` | The metric aggregation type. |
| <CopyableCode code="resourceId" /> | `string` | The metric source ID. |
| <CopyableCode code="type" /> | `string` | The metric definition type. |
| <CopyableCode code="unit" /> | `string` | The metric unit. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName" /> | Gets the metric definitions for the specified volume container. |

## `SELECT` examples

Gets the metric definitions for the specified volume container.


```sql
SELECT
name,
category,
dimensions,
metricAvailabilities,
primaryAggregationType,
resourceId,
type,
unit
FROM azure_extras.storsimple_8000_series.volume_containers_metric_definitions
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeContainerName = '{{ volumeContainerName }}';
```