---
title: container_registry_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registry_configurations
  - container_registry_admin
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

Creates, updates, deletes, gets or lists a <code>container_registry_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_registry_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.container_registry_admin.container_registry_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_container_registry_configurations', value: 'view', },
        { label: 'container_registry_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="maximum_capacity_in_gib" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Container registry configuration property. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, location, subscriptionId" /> | Returns the specified configuration details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of configuration at the given location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName, location, subscriptionId" /> | Delete an existing container registry configuration |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="configurationName, location, subscriptionId, data__properties" /> | Configure container registry overall configuration properties. |

## `SELECT` examples

Returns a list of configuration at the given location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_container_registry_configurations', value: 'view', },
        { label: 'container_registry_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configurationName,
location,
maximum_capacity_in_gib,
subscriptionId,
type
FROM azure_stack.container_registry_admin.vw_container_registry_configurations
WHERE location = '{{ location }}'
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
FROM azure_stack.container_registry_admin.container_registry_configurations
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>container_registry_configurations</code> resource.

```sql
/*+ update */
REPLACE azure_stack.container_registry_admin.container_registry_configurations
SET 
properties = '{{ properties }}'
WHERE 
configurationName = '{{ configurationName }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}';
```

## `DELETE` example

Deletes the specified <code>container_registry_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.container_registry_admin.container_registry_configurations
WHERE configurationName = '{{ configurationName }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
