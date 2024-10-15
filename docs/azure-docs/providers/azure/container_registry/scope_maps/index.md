---
title: scope_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_maps
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>scope_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scope_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.scope_maps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_maps', value: 'view', },
        { label: 'scope_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopeMapName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a scope map. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, scopeMapName, subscriptionId" /> | Gets the properties of the specified scope map. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the scope maps for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, scopeMapName, subscriptionId" /> | Creates a scope map for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, scopeMapName, subscriptionId" /> | Deletes a scope map from a container registry. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="registryName, resourceGroupName, scopeMapName, subscriptionId" /> | Updates a scope map with the specified parameters. |

## `SELECT` examples

Lists all the scope maps for the specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_maps', value: 'view', },
        { label: 'scope_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
actions,
creation_date,
provisioning_state,
registryName,
resourceGroupName,
scopeMapName,
subscriptionId,
type
FROM azure.container_registry.vw_scope_maps
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_registry.scope_maps
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scope_maps</code> resource.

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
INSERT INTO azure.container_registry.scope_maps (
registryName,
resourceGroupName,
scopeMapName,
subscriptionId,
properties
)
SELECT 
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ scopeMapName }}',
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
        - name: description
          value: string
        - name: type
          value: string
        - name: creationDate
          value: string
        - name: provisioningState
          value: string
        - name: actions
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>scope_maps</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.scope_maps
SET 
properties = '{{ properties }}'
WHERE 
registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scopeMapName = '{{ scopeMapName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>scope_maps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.scope_maps
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scopeMapName = '{{ scopeMapName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
