---
title: clusters_streaming_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_streaming_jobs
  - stream_analytics
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

Creates, updates, deletes, gets or lists a <code>clusters_streaming_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_streaming_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.clusters_streaming_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID of the streaming job. |
| <CopyableCode code="jobState" /> | `string` | The current execution state of the streaming job. |
| <CopyableCode code="streamingUnits" /> | `integer` | The number of streaming units that are used by the streaming job. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists all of the streaming jobs in the given cluster. |

## `SELECT` examples

Lists all of the streaming jobs in the given cluster.


```sql
SELECT
id,
jobState,
streamingUnits
FROM azure.stream_analytics.clusters_streaming_jobs
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```