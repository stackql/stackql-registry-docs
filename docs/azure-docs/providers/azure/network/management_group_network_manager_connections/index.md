---
title: management_group_network_manager_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - management_group_network_manager_connections
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

Creates, updates, deletes, gets or lists a <code>management_group_network_manager_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_group_network_manager_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.management_group_network_manager_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_group_network_manager_connections', value: 'view', },
        { label: 'management_group_network_manager_connections', value: 'resource', },
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
| <CopyableCode code="managementGroupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkManagerConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_manager_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Information about the network manager connection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managementGroupId, networkManagerConnectionName" /> | Get a specified connection created by this management group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managementGroupId" /> | List all network manager connections created by this management group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managementGroupId, networkManagerConnectionName" /> | Create a network manager connection on this management group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managementGroupId, networkManagerConnectionName" /> | Delete specified pending connection created by this management group. |

## `SELECT` examples

List all network manager connections created by this management group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_group_network_manager_connections', value: 'view', },
        { label: 'management_group_network_manager_connections', value: 'resource', },
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
managementGroupId,
networkManagerConnectionName,
network_manager_id,
system_data,
type
FROM azure.network.vw_management_group_network_manager_connections
WHERE managementGroupId = '{{ managementGroupId }}';
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
FROM azure.network.management_group_network_manager_connections
WHERE managementGroupId = '{{ managementGroupId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>management_group_network_manager_connections</code> resource.

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
INSERT INTO azure.network.management_group_network_manager_connections (
managementGroupId,
networkManagerConnectionName,
properties
)
SELECT 
'{{ managementGroupId }}',
'{{ networkManagerConnectionName }}',
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
        - name: networkManagerId
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

Deletes the specified <code>management_group_network_manager_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.management_group_network_manager_connections
WHERE managementGroupId = '{{ managementGroupId }}'
AND networkManagerConnectionName = '{{ networkManagerConnectionName }}';
```
