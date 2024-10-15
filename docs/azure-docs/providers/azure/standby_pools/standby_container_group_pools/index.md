---
title: standby_container_group_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - standby_container_group_pools
  - standby_pools
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

Creates, updates, deletes, gets or lists a <code>standby_container_group_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standby_container_group_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.standby_pools.standby_container_group_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_standby_container_group_pools', value: 'view', },
        { label: 'standby_container_group_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="container_group_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="elasticity_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="standbyContainerGroupPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the StandbyContainerGroupPool. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, standbyContainerGroupPoolName, subscriptionId" /> | Get a StandbyContainerGroupPoolResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List StandbyContainerGroupPoolResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List StandbyContainerGroupPoolResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, standbyContainerGroupPoolName, subscriptionId" /> | Create a StandbyContainerGroupPoolResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, standbyContainerGroupPoolName, subscriptionId" /> | Delete a StandbyContainerGroupPoolResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, standbyContainerGroupPoolName, subscriptionId" /> | Update a StandbyContainerGroupPoolResource |

## `SELECT` examples

List StandbyContainerGroupPoolResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_standby_container_group_pools', value: 'view', },
        { label: 'standby_container_group_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
container_group_properties,
elasticity_profile,
location,
provisioning_state,
resourceGroupName,
standbyContainerGroupPoolName,
subscriptionId,
tags
FROM azure.standby_pools.vw_standby_container_group_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.standby_pools.standby_container_group_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>standby_container_group_pools</code> resource.

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
INSERT INTO azure.standby_pools.standby_container_group_pools (
resourceGroupName,
standbyContainerGroupPoolName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ standbyContainerGroupPoolName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: elasticityProfile
          value:
            - name: maxReadyCapacity
              value: integer
            - name: refillPolicy
              value: []
        - name: containerGroupProperties
          value:
            - name: containerGroupProfile
              value:
                - name: id
                  value: string
                - name: revision
                  value: integer
            - name: subnetIds
              value:
                - - name: id
                    value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>standby_container_group_pools</code> resource.

```sql
/*+ update */
UPDATE azure.standby_pools.standby_container_group_pools
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND standbyContainerGroupPoolName = '{{ standbyContainerGroupPoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>standby_container_group_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.standby_pools.standby_container_group_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND standbyContainerGroupPoolName = '{{ standbyContainerGroupPoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
