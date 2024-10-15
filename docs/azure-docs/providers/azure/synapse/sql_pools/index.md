---
title: sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pools
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

Creates, updates, deletes, gets or lists a <code>sql_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pools', value: 'view', },
        { label: 'sql_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="max_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoverable_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="source_database_deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a SQL Analytics pool |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get SQL pool properties |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List all SQL pools |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Create a SQL pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Delete a SQL pool |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Apply a partial update to a SQL pool |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Pause a SQL pool |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Resume a SQL pool |

## `SELECT` examples

List all SQL pools

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pools', value: 'view', },
        { label: 'sql_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
collation,
create_mode,
creation_date,
location,
max_size_bytes,
provisioning_state,
recoverable_database_id,
resourceGroupName,
restore_point_in_time,
sku,
source_database_deletion_date,
source_database_id,
sqlPoolName,
status,
storage_account_type,
subscriptionId,
tags,
workspaceName
FROM azure.synapse.vw_sql_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.synapse.sql_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pools</code> resource.

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
INSERT INTO azure.synapse.sql_pools (
resourceGroupName,
sqlPoolName,
subscriptionId,
workspaceName,
tags,
location,
sku,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ tags }}',
'{{ location }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: properties
      value:
        - name: maxSizeBytes
          value: integer
        - name: collation
          value: string
        - name: sourceDatabaseId
          value: string
        - name: recoverableDatabaseId
          value: string
        - name: provisioningState
          value: string
        - name: status
          value: string
        - name: restorePointInTime
          value: string
        - name: createMode
          value: string
        - name: creationDate
          value: string
        - name: storageAccountType
          value: string
        - name: sourceDatabaseDeletionDate
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_pools</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.sql_pools
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>sql_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.sql_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
