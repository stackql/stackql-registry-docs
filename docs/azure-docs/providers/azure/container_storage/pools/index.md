---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
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

Creates, updates, deletes, gets or lists a <code>pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_storage.pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pools', value: 'view', },
        { label: 'pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assignments" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="pool_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reclaim_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="zones" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Pool Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | Get a Pool |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Pool resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Pool resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | Create a Pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | Delete a Pool |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | Update a Pool |

## `SELECT` examples

List Pool resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pools', value: 'view', },
        { label: 'pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
assignments,
location,
poolName,
pool_type,
provisioning_state,
reclaim_policy,
resourceGroupName,
resources,
status,
subscriptionId,
tags,
zones
FROM azure.container_storage.vw_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.container_storage.pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pools</code> resource.

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
INSERT INTO azure.container_storage.pools (
poolName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ poolName }}',
'{{ resourceGroupName }}',
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
        - name: provisioningState
          value: []
        - name: status
          value:
            - name: state
              value: []
            - name: message
              value: string
        - name: zones
          value:
            - []
        - name: resources
          value:
            - name: requests
              value:
                - name: storage
                  value: integer
        - name: poolType
          value:
            - name: azureDisk
              value:
                - name: resourceGroup
                  value: string
                - name: skuName
                  value: []
                - name: encryption
                  value:
                    - name: keyName
                      value: string
                    - name: keyVaultUri
                      value: string
                    - name: identity
                      value:
                        - name: principalId
                          value: string
                        - name: tenantId
                          value: string
                        - name: type
                          value: []
                        - name: userAssignedIdentities
                          value: []
                - name: disks
                  value:
                    - - name: id
                        value: string
                      - name: reference
                        value: string
            - name: elasticSan
              value:
                - name: resourceGroup
                  value: string
                - name: skuName
                  value: []
            - name: ephemeralDisk
              value:
                - name: replicas
                  value: integer
                - name: disks
                  value:
                    - - name: id
                        value: string
                      - name: reference
                        value: string
        - name: reclaimPolicy
          value: []
        - name: assignments
          value:
            - - name: status
                value:
                  - name: state
                    value: []
                  - name: message
                    value: string
              - name: id
                value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pools</code> resource.

```sql
/*+ update */
UPDATE azure.container_storage.pools
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_storage.pools
WHERE poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
