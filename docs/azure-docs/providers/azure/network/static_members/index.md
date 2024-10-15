---
title: static_members
hide_title: false
hide_table_of_contents: false
keywords:
  - static_members
  - network
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

Creates, updates, deletes, gets or lists a <code>static_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.static_members" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_static_members', value: 'view', },
        { label: 'static_members', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="networkGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="region" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="staticMemberName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of static member. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, staticMemberName, subscriptionId" /> | Gets the specified static member. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, subscriptionId" /> | Lists the specified static member. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, staticMemberName, subscriptionId" /> | Creates or updates a static member. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, staticMemberName, subscriptionId" /> | Deletes a static member. |

## `SELECT` examples

Lists the specified static member.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_static_members', value: 'view', },
        { label: 'static_members', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
networkGroupName,
networkManagerName,
provisioning_state,
region,
resourceGroupName,
resource_id,
staticMemberName,
subscriptionId,
system_data,
type
FROM azure.network.vw_static_members
WHERE networkGroupName = '{{ networkGroupName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.network.static_members
WHERE networkGroupName = '{{ networkGroupName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>static_members</code> resource.

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
INSERT INTO azure.network.static_members (
networkGroupName,
networkManagerName,
resourceGroupName,
staticMemberName,
subscriptionId,
properties
)
SELECT 
'{{ networkGroupName }}',
'{{ networkManagerName }}',
'{{ resourceGroupName }}',
'{{ staticMemberName }}',
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
        - name: resourceId
          value: string
        - name: region
          value: string
        - name: provisioningState
          value: []
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>static_members</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.static_members
WHERE networkGroupName = '{{ networkGroupName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND staticMemberName = '{{ staticMemberName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
