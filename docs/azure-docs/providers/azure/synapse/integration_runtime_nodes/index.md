---
title: integration_runtime_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_nodes
  - synapse
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

Creates, updates, deletes, gets or lists a <code>integration_runtime_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtime_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.integration_runtime_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capabilities" /> | `object` | The integration runtime capabilities dictionary |
| <CopyableCode code="concurrentJobsLimit" /> | `integer` | Maximum concurrent jobs on the integration runtime node. |
| <CopyableCode code="expiryTime" /> | `string` | The time at which the integration runtime will expire in ISO8601 format. |
| <CopyableCode code="hostServiceUri" /> | `string` | URI for the host machine of the integration runtime. |
| <CopyableCode code="isActiveDispatcher" /> | `boolean` | Indicates whether this node is the active dispatcher for integration runtime requests. |
| <CopyableCode code="lastConnectTime" /> | `string` | The most recent time at which the integration runtime was connected in ISO8601 format. |
| <CopyableCode code="lastEndUpdateTime" /> | `string` | The last time for the integration runtime node update end. |
| <CopyableCode code="lastStartTime" /> | `string` | The time the node last started up. |
| <CopyableCode code="lastStartUpdateTime" /> | `string` | The last time for the integration runtime node update start. |
| <CopyableCode code="lastStopTime" /> | `string` | The integration runtime node last stop time. |
| <CopyableCode code="lastUpdateResult" /> | `string` | The result of the last integration runtime node update. |
| <CopyableCode code="machineName" /> | `string` | Machine name of the integration runtime node. |
| <CopyableCode code="maxConcurrentJobs" /> | `integer` | The maximum concurrent jobs in this integration runtime. |
| <CopyableCode code="nodeName" /> | `string` | Name of the integration runtime node. |
| <CopyableCode code="registerTime" /> | `string` | The time at which the integration runtime node was registered in ISO8601 format. |
| <CopyableCode code="status" /> | `string` | Status of the integration runtime node. |
| <CopyableCode code="version" /> | `string` | Version of the integration runtime node. |
| <CopyableCode code="versionStatus" /> | `string` | Status of the integration runtime node version. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName" /> | Get an integration runtime node |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName" /> | Delete an integration runtime node |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName" /> | Create an integration runtime node |

## `SELECT` examples

Get an integration runtime node


```sql
SELECT
capabilities,
concurrentJobsLimit,
expiryTime,
hostServiceUri,
isActiveDispatcher,
lastConnectTime,
lastEndUpdateTime,
lastStartTime,
lastStartUpdateTime,
lastStopTime,
lastUpdateResult,
machineName,
maxConcurrentJobs,
nodeName,
registerTime,
status,
version,
versionStatus
FROM azure.synapse.integration_runtime_nodes
WHERE integrationRuntimeName = '{{ integrationRuntimeName }}'
AND nodeName = '{{ nodeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
## `UPDATE` example

Updates a <code>integration_runtime_nodes</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.integration_runtime_nodes
SET 
concurrentJobsLimit = '{{ concurrentJobsLimit }}'
WHERE 
integrationRuntimeName = '{{ integrationRuntimeName }}'
AND nodeName = '{{ nodeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>integration_runtime_nodes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.integration_runtime_nodes
WHERE integrationRuntimeName = '{{ integrationRuntimeName }}'
AND nodeName = '{{ nodeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
