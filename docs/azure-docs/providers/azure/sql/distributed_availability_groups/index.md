---
title: distributed_availability_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - distributed_availability_groups
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

Creates, updates, deletes, gets or lists a <code>distributed_availability_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distributed_availability_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.distributed_availability_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_distributed_availability_groups', value: 'view', },
        { label: 'distributed_availability_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="distributedAvailabilityGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="distributed_availability_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_hardened_lsn" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_availability_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_availability_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_replica_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_database" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_replica_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a distributed availability group. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a distributed availability group info. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId" /> | Creates a distributed availability group between Sql On-Prem and Sql Managed Instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId" /> | Drops a distributed availability group between Sql On-Prem and Sql Managed Instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId" /> | Updates a distributed availability group replication mode. |

## `SELECT` examples

Gets a distributed availability group info.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_distributed_availability_groups', value: 'view', },
        { label: 'distributed_availability_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
distributedAvailabilityGroupName,
distributed_availability_group_id,
last_hardened_lsn,
link_state,
managedInstanceName,
primary_availability_group_name,
replication_mode,
resourceGroupName,
secondary_availability_group_name,
source_endpoint,
source_replica_id,
subscriptionId,
target_database,
target_replica_id
FROM azure.sql.vw_distributed_availability_groups
WHERE distributedAvailabilityGroupName = '{{ distributedAvailabilityGroupName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.distributed_availability_groups
WHERE distributedAvailabilityGroupName = '{{ distributedAvailabilityGroupName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>distributed_availability_groups</code> resource.

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
INSERT INTO azure.sql.distributed_availability_groups (
distributedAvailabilityGroupName,
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ distributedAvailabilityGroupName }}',
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: targetDatabase
          value: string
        - name: sourceEndpoint
          value: string
        - name: primaryAvailabilityGroupName
          value: string
        - name: secondaryAvailabilityGroupName
          value: string
        - name: replicationMode
          value: string
        - name: distributedAvailabilityGroupId
          value: string
        - name: sourceReplicaId
          value: string
        - name: targetReplicaId
          value: string
        - name: linkState
          value: string
        - name: lastHardenedLsn
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>distributed_availability_groups</code> resource.

```sql
/*+ update */
UPDATE azure.sql.distributed_availability_groups
SET 
properties = '{{ properties }}'
WHERE 
distributedAvailabilityGroupName = '{{ distributedAvailabilityGroupName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>distributed_availability_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.distributed_availability_groups
WHERE distributedAvailabilityGroupName = '{{ distributedAvailabilityGroupName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
