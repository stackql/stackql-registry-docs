---
title: private_link_scoped_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scoped_resources
  - monitor
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

Creates, updates, deletes, gets or lists a <code>private_link_scoped_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_scoped_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.private_link_scoped_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_scoped_resources', value: 'view', },
        { label: 'private_link_scoped_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="linked_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Properties of a private link scoped resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, scopeName, subscriptionId" /> | Gets a scoped resource in a private link scope. |
| <CopyableCode code="list_by_private_link_scope" /> | `SELECT` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Gets all private endpoint connections on a private link scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, scopeName, subscriptionId" /> | Approve or reject a private endpoint connection with a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, scopeName, subscriptionId" /> | Deletes a private endpoint connection with a given name. |

## `SELECT` examples

Gets all private endpoint connections on a private link scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_scoped_resources', value: 'view', },
        { label: 'private_link_scoped_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
linked_resource_id,
provisioning_state,
resourceGroupName,
scopeName,
subscriptionId,
system_data,
type
FROM azure.monitor.vw_private_link_scoped_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scopeName = '{{ scopeName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.monitor.private_link_scoped_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scopeName = '{{ scopeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_link_scoped_resources</code> resource.

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
INSERT INTO azure.monitor.private_link_scoped_resources (
name,
resourceGroupName,
scopeName,
subscriptionId,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ scopeName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: linkedResourceId
          value: string
        - name: provisioningState
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_link_scoped_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.private_link_scoped_resources
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scopeName = '{{ scopeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
