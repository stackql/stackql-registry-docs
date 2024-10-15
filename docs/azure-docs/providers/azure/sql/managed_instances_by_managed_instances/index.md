---
title: managed_instances_by_managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instances_by_managed_instances
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instances_by_managed_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instances_by_managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instances_by_managed_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aggregationFunction" /> | `string` | Aggregation function used to calculate query metrics. |
| <CopyableCode code="endTime" /> | `string` | The end time for the metric (ISO-8601 format). |
| <CopyableCode code="intervalType" /> | `string` | Interval type (length). |
| <CopyableCode code="numberOfQueries" /> | `integer` | Requested number of top queries. |
| <CopyableCode code="observationMetric" /> | `string` | Metric used to rank queries. |
| <CopyableCode code="queries" /> | `array` | List of top resource consuming queries with appropriate metric data |
| <CopyableCode code="startTime" /> | `string` | The start time for the metric (ISO-8601 format). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Get top resource consuming queries of a managed instance. |

## `SELECT` examples

Get top resource consuming queries of a managed instance.


```sql
SELECT
aggregationFunction,
endTime,
intervalType,
numberOfQueries,
observationMetric,
queries,
startTime
FROM azure.sql.managed_instances_by_managed_instances
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```