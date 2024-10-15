---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - container_storage
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_storage.volumes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity_gib" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="volume_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Volume Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId, volumeName" /> | Get a Volume |
| <CopyableCode code="list_by_pool" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | List Volume resources by Pool |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId, volumeName" /> | Create a Volume |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="poolName, resourceGroupName, subscriptionId, volumeName" /> | Delete a Volume |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="poolName, resourceGroupName, subscriptionId, volumeName" /> | Update a Volume |

## `SELECT` examples

List Volume resources by Pool

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
capacity_gib,
labels,
poolName,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
volumeName,
volume_type
FROM azure.container_storage.vw_volumes
WHERE poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_storage.volumes
WHERE poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volumes</code> resource.

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
INSERT INTO azure.container_storage.volumes (
poolName,
resourceGroupName,
subscriptionId,
volumeName,
properties
)
SELECT 
'{{ poolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ volumeName }}',
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
        - name: provisioningState
          value: []
        - name: status
          value:
            - name: state
              value: []
            - name: message
              value: string
        - name: labels
          value: object
        - name: capacityGiB
          value: integer
        - name: volumeType
          value:
            - name: elasticSan
              value:
                - name: targetIqn
                  value: string
                - name: targetPortalHostname
                  value: string
                - name: targetPortalPort
                  value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>volumes</code> resource.

```sql
/*+ update */
UPDATE azure.container_storage.volumes
SET 
properties = '{{ properties }}'
WHERE 
poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```

## `DELETE` example

Deletes the specified <code>volumes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_storage.volumes
WHERE poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}';
```
