---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_groups', value: 'view', },
        { label: 'groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="member_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Properties of network group |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, subscriptionId" /> | Gets the specified network group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Lists the specified network group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, subscriptionId" /> | Creates or updates a network group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkGroupName, networkManagerName, resourceGroupName, subscriptionId" /> | Deletes a network group. |

## `SELECT` examples

Lists the specified network group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_groups', value: 'view', },
        { label: 'groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
etag,
member_type,
networkGroupName,
networkManagerName,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
system_data,
type
FROM azure.network.vw_groups
WHERE networkManagerName = '{{ networkManagerName }}'
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
FROM azure.network.groups
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups</code> resource.

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
INSERT INTO azure.network.groups (
networkGroupName,
networkManagerName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ networkGroupName }}',
'{{ networkManagerName }}',
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
        - name: description
          value: string
        - name: memberType
          value: []
        - name: provisioningState
          value: []
        - name: resourceGuid
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

Deletes the specified <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.groups
WHERE networkGroupName = '{{ networkGroupName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
