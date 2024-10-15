---
title: resource_guards
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guards
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>resource_guards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_guards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.resource_guards" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_guards', value: 'view', },
        { label: 'resource_guards', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `text` | Resource name associated with the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_auto_approvals" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGuardsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| <CopyableCode code="vault_critical_operation_exclusion_list" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="eTag" /> | `string` | Optional ETag. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceGuardsName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceGuardsName, subscriptionId" /> |  |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceGuardsName, subscriptionId" /> |  |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="resourceGroupName, resourceGuardsName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_guards', value: 'view', },
        { label: 'resource_guards', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
allow_auto_approvals,
e_tag,
location,
provisioning_state,
resourceGroupName,
resourceGuardsName,
resource_guard_operations,
subscriptionId,
system_data,
tags,
type,
vault_critical_operation_exclusion_list
FROM azure.data_protection.vw_resource_guards
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardsName = '{{ resourceGuardsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
eTag,
location,
properties,
systemData,
tags,
type
FROM azure.data_protection.resource_guards
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardsName = '{{ resourceGuardsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>resource_guards</code> resource.

```sql
/*+ update */
UPDATE azure.data_protection.resource_guards
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardsName = '{{ resourceGuardsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>resource_guards</code> resource.

```sql
/*+ update */
REPLACE azure.data_protection.resource_guards
SET 
eTag = '{{ eTag }}',
location = '{{ location }}',
tags = '{{ tags }}',
systemData = '{{ systemData }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardsName = '{{ resourceGuardsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>resource_guards</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_protection.resource_guards
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardsName = '{{ resourceGuardsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
