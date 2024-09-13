---
title: node_groups_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - node_groups_nodes
  - compute
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

Creates, updates, deletes, gets or lists a <code>node_groups_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_groups_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.node_groups_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the node. |
| <CopyableCode code="accelerators" /> | `array` | Accelerators for this node. |
| <CopyableCode code="consumedResources" /> | `object` |  |
| <CopyableCode code="cpuOvercommitType" /> | `string` | CPU overcommit. |
| <CopyableCode code="disks" /> | `array` | Local disk configurations. |
| <CopyableCode code="instanceConsumptionData" /> | `array` | Instance data that shows consumed resources on the node. |
| <CopyableCode code="instances" /> | `array` | Instances scheduled on this node. |
| <CopyableCode code="nodeType" /> | `string` | The type of this node. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | [Output Only] Reserved for future use. |
| <CopyableCode code="serverBinding" /> | `object` |  |
| <CopyableCode code="serverId" /> | `string` | Server ID associated with this node. |
| <CopyableCode code="status" /> | `string` |  |
| <CopyableCode code="totalResources" /> | `object` |  |
| <CopyableCode code="upcomingMaintenance" /> | `object` | Upcoming Maintenance notification information. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_nodes" /> | `SELECT` | <CopyableCode code="nodeGroup, project, zone" /> | Lists nodes in the node group. |
| <CopyableCode code="add_nodes" /> | `INSERT` | <CopyableCode code="nodeGroup, project, zone" /> | Adds specified number of nodes to the node group. |
| <CopyableCode code="delete_nodes" /> | `DELETE` | <CopyableCode code="nodeGroup, project, zone" /> | Deletes specified nodes from the node group. |

## `SELECT` examples

Lists nodes in the node group.

```sql
SELECT
name,
accelerators,
consumedResources,
cpuOvercommitType,
disks,
instanceConsumptionData,
instances,
nodeType,
satisfiesPzs,
serverBinding,
serverId,
status,
totalResources,
upcomingMaintenance
FROM google.compute.node_groups_nodes
WHERE nodeGroup = '{{ nodeGroup }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>node_groups_nodes</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.compute.node_groups_nodes (
nodeGroup,
project,
zone,
additionalNodeCount
)
SELECT 
'{{ nodeGroup }}',
'{{ project }}',
'{{ zone }}',
'{{ additionalNodeCount }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: additionalNodeCount
        value: '{{ additionalNodeCount }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>node_groups_nodes</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.node_groups_nodes
WHERE nodeGroup = '{{ nodeGroup }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
