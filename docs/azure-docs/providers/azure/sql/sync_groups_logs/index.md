---
title: sync_groups_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups_logs
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

Creates, updates, deletes, gets or lists a <code>sync_groups_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_groups_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_groups_logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="details" /> | `string` | Details of the sync group log. |
| <CopyableCode code="operationStatus" /> | `string` | OperationStatus of the sync group log. |
| <CopyableCode code="source" /> | `string` | Source of the sync group log. |
| <CopyableCode code="timestamp" /> | `string` | Timestamp of the sync group log. |
| <CopyableCode code="tracingId" /> | `string` | TracingId of the sync group log. |
| <CopyableCode code="type" /> | `string` | Type of the sync group log. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databaseName, endTime, resourceGroupName, serverName, startTime, subscriptionId, syncGroupName, type" /> | Gets a collection of sync group logs. |

## `SELECT` examples

Gets a collection of sync group logs.


```sql
SELECT
details,
operationStatus,
source,
timestamp,
tracingId,
type
FROM azure.sql.sync_groups_logs
WHERE databaseName = '{{ databaseName }}'
AND endTime = '{{ endTime }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND startTime = '{{ startTime }}'
AND subscriptionId = '{{ subscriptionId }}'
AND syncGroupName = '{{ syncGroupName }}'
AND type = '{{ type }}';
```