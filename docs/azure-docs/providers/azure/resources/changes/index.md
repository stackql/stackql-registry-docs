---
title: changes
hide_title: false
hide_table_of_contents: false
keywords:
  - changes
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>changes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.changes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_changes', value: 'view', },
        { label: 'changes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="changeResourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="change_attributes" /> | `text` | field from the `properties` object |
| <CopyableCode code="change_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="changes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceProviderNamespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceType" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of a change |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="changeResourceId, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Obtains the specified change resource for the target resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Obtains a list of change resources from the past 14 days for the target resource |

## `SELECT` examples

Obtains a list of change resources from the past 14 days for the target resource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_changes', value: 'view', },
        { label: 'changes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
changeResourceId,
change_attributes,
change_type,
changes,
resourceGroupName,
resourceName,
resourceProviderNamespace,
resourceType,
subscriptionId,
target_resource_id,
target_resource_type,
type
FROM azure.resources.vw_changes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceProviderNamespace = '{{ resourceProviderNamespace }}'
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
FROM azure.resources.changes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceProviderNamespace = '{{ resourceProviderNamespace }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

