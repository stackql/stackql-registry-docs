---
title: cache_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_rules
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

Creates, updates, deletes, gets or lists a <code>cache_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cache_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.cache_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cache_rules', value: 'view', },
        { label: 'cache_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cacheRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="credential_set_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_repository" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_repository" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a cache rule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheRuleName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified cache rule resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all cache rule resources for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="cacheRuleName, registryName, resourceGroupName, subscriptionId" /> | Creates a cache rule for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheRuleName, registryName, resourceGroupName, subscriptionId" /> | Deletes a cache rule resource from a container registry. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="cacheRuleName, registryName, resourceGroupName, subscriptionId" /> | Updates a cache rule for a container registry with the specified parameters. |

## `SELECT` examples

Lists all cache rule resources for the specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cache_rules', value: 'view', },
        { label: 'cache_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cacheRuleName,
creation_date,
credential_set_resource_id,
provisioning_state,
registryName,
resourceGroupName,
source_repository,
subscriptionId,
target_repository
FROM azure.container_registry.vw_cache_rules
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_registry.cache_rules
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cache_rules</code> resource.

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
INSERT INTO azure.container_registry.cache_rules (
cacheRuleName,
registryName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ cacheRuleName }}',
'{{ registryName }}',
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
        - name: credentialSetResourceId
          value: string
        - name: sourceRepository
          value: string
        - name: targetRepository
          value: string
        - name: creationDate
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cache_rules</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.cache_rules
SET 
properties = '{{ properties }}'
WHERE 
cacheRuleName = '{{ cacheRuleName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cache_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.cache_rules
WHERE cacheRuleName = '{{ cacheRuleName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
