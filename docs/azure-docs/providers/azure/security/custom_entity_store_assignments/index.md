---
title: custom_entity_store_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_entity_store_assignments
  - security
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

Creates, updates, deletes, gets or lists a <code>custom_entity_store_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_entity_store_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.custom_entity_store_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_entity_store_assignments', value: 'view', },
        { label: 'custom_entity_store_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="customEntityStoreAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_store_database_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes the custom entity store assignment properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customEntityStoreAssignmentName, resourceGroupName, subscriptionId" /> | Gets a single custom entity store assignment by name for the provided subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List custom entity store assignments by a provided subscription and resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List custom entity store assignments by provided subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customEntityStoreAssignmentName, resourceGroupName, subscriptionId" /> | Creates a custom entity store assignment for the provided subscription, if not already exists. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customEntityStoreAssignmentName, resourceGroupName, subscriptionId" /> | Delete a custom entity store assignment by name for a provided subscription |

## `SELECT` examples

List custom entity store assignments by provided subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_entity_store_assignments', value: 'view', },
        { label: 'custom_entity_store_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
customEntityStoreAssignmentName,
entity_store_database_link,
principal,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.security.vw_custom_entity_store_assignments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.security.custom_entity_store_assignments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_entity_store_assignments</code> resource.

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
INSERT INTO azure.security.custom_entity_store_assignments (
customEntityStoreAssignmentName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ customEntityStoreAssignmentName }}',
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
        - name: principal
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>custom_entity_store_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.custom_entity_store_assignments
WHERE customEntityStoreAssignmentName = '{{ customEntityStoreAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
