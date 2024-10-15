---
title: apply_updates_parents
hide_title: false
hide_table_of_contents: false
keywords:
  - apply_updates_parents
  - maintenance
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

Creates, updates, deletes, gets or lists a <code>apply_updates_parents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apply_updates_parents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.apply_updates_parents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apply_updates_parents', value: 'view', },
        { label: 'apply_updates_parents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="applyUpdateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_update_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceParentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceParentType" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceType" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for apply update |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applyUpdateName, providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId" /> | Track maintenance updates to resource with parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId" /> | Apply maintenance updates to resource with parent |

## `SELECT` examples

Track maintenance updates to resource with parent

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_apply_updates_parents', value: 'view', },
        { label: 'apply_updates_parents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applyUpdateName,
last_update_time,
providerName,
resourceGroupName,
resourceName,
resourceParentName,
resourceParentType,
resourceType,
resource_id,
status,
subscriptionId,
type
FROM azure.maintenance.vw_apply_updates_parents
WHERE applyUpdateName = '{{ applyUpdateName }}'
AND providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceParentName = '{{ resourceParentName }}'
AND resourceParentType = '{{ resourceParentType }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.maintenance.apply_updates_parents
WHERE applyUpdateName = '{{ applyUpdateName }}'
AND providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceParentName = '{{ resourceParentName }}'
AND resourceParentType = '{{ resourceParentType }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apply_updates_parents</code> resource.

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
INSERT INTO azure.maintenance.apply_updates_parents (
providerName,
resourceGroupName,
resourceName,
resourceParentName,
resourceParentType,
resourceType,
subscriptionId
)
SELECT 
'{{ providerName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ resourceParentName }}',
'{{ resourceParentType }}',
'{{ resourceType }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>
