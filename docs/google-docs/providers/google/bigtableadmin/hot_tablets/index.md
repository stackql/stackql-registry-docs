---
title: hot_tablets
hide_title: false
hide_table_of_contents: false
keywords:
  - hot_tablets
  - bigtableadmin
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

Creates, updates, deletes, gets or lists a <code>hot_tablets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hot_tablets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigtableadmin.hot_tablets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique name of the hot tablet. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/hotTablets/[a-zA-Z0-9_-]*`. |
| <CopyableCode code="endKey" /> | `string` | Tablet End Key (inclusive). |
| <CopyableCode code="endTime" /> | `string` | Output only. The end time of the hot tablet. |
| <CopyableCode code="nodeCpuUsagePercent" /> | `number` | Output only. The average CPU usage spent by a node on this tablet over the start_time to end_time time range. The percentage is the amount of CPU used by the node to serve the tablet, from 0% (tablet was not interacted with) to 100% (the node spent all cycles serving the hot tablet). |
| <CopyableCode code="startKey" /> | `string` | Tablet Start Key (inclusive). |
| <CopyableCode code="startTime" /> | `string` | Output only. The start time of the hot tablet. |
| <CopyableCode code="tableName" /> | `string` | Name of the table that contains the tablet. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clustersId, instancesId, projectsId" /> | Lists hot tablets in a cluster, within the time range provided. Hot tablets are ordered based on CPU usage. |

## `SELECT` examples

Lists hot tablets in a cluster, within the time range provided. Hot tablets are ordered based on CPU usage.

```sql
SELECT
name,
endKey,
endTime,
nodeCpuUsagePercent,
startKey,
startTime,
tableName
FROM google.bigtableadmin.hot_tablets
WHERE clustersId = '{{ clustersId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'; 
```
