---
title: file_shares_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares_metric_definitions
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>file_shares_metric_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_shares_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.file_shares_metric_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The name of the metric |
| <CopyableCode code="dimensions" /> | `array` | The supported dimensions |
| <CopyableCode code="metricAvailabilities" /> | `array` | The available metric granularities |
| <CopyableCode code="primaryAggregationType" /> | `string` | The metric aggregation type |
| <CopyableCode code="resourceId" /> | `string` | The metric source id |
| <CopyableCode code="type" /> | `string` | The metric definition type |
| <CopyableCode code="unit" /> | `string` | The metric unit |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId" /> | Retrieves metric definitions of all metrics aggregated at the file share. |

## `SELECT` examples

Retrieves metric definitions of all metrics aggregated at the file share.


```sql
SELECT
name,
dimensions,
metricAvailabilities,
primaryAggregationType,
resourceId,
type,
unit
FROM azure_extras.storsimple_1200_series.file_shares_metric_definitions
WHERE deviceName = '{{ deviceName }}'
AND fileServerName = '{{ fileServerName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```