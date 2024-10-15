---
title: scope_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_connections
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

Creates, updates, deletes, gets or lists a <code>scope_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scope_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.scope_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_connections', value: 'view', },
        { label: 'scope_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="networkManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopeConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Scope connection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, scopeConnectionName, subscriptionId" /> | Get specified scope connection created by this Network Manager. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | List all scope connections created by this network manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkManagerName, resourceGroupName, scopeConnectionName, subscriptionId" /> | Creates or updates scope connection from Network Manager |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkManagerName, resourceGroupName, scopeConnectionName, subscriptionId" /> | Delete the pending scope connection created by this network manager. |

## `SELECT` examples

List all scope connections created by this network manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_connections', value: 'view', },
        { label: 'scope_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
connection_state,
etag,
networkManagerName,
resourceGroupName,
resource_id,
scopeConnectionName,
subscriptionId,
system_data,
tenant_id,
type
FROM azure.network.vw_scope_connections
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
FROM azure.network.scope_connections
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scope_connections</code> resource.

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
INSERT INTO azure.network.scope_connections (
networkManagerName,
resourceGroupName,
scopeConnectionName,
subscriptionId,
properties
)
SELECT 
'{{ networkManagerName }}',
'{{ resourceGroupName }}',
'{{ scopeConnectionName }}',
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
        - name: tenantId
          value: string
        - name: resourceId
          value: string
        - name: connectionState
          value: []
        - name: description
          value: string
    - name: etag
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>scope_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.scope_connections
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scopeConnectionName = '{{ scopeConnectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
