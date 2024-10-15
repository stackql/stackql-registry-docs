---
title: subscription_network_manager_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_network_manager_connections
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

Creates, updates, deletes, gets or lists a <code>subscription_network_manager_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_network_manager_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.subscription_network_manager_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscription_network_manager_connections', value: 'view', },
        { label: 'subscription_network_manager_connections', value: 'resource', },
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
| <CopyableCode code="networkManagerConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_manager_id" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Information about the network manager connection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkManagerConnectionName, subscriptionId" /> | Get a specified connection created by this subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all network manager connections created by this subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkManagerConnectionName, subscriptionId" /> | Create a network manager connection on this subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkManagerConnectionName, subscriptionId" /> | Delete specified connection created by this subscription. |

## `SELECT` examples

List all network manager connections created by this subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscription_network_manager_connections', value: 'view', },
        { label: 'subscription_network_manager_connections', value: 'resource', },
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
networkManagerConnectionName,
network_manager_id,
subscriptionId,
system_data,
type
FROM azure.network.vw_subscription_network_manager_connections
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure.network.subscription_network_manager_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscription_network_manager_connections</code> resource.

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
INSERT INTO azure.network.subscription_network_manager_connections (
networkManagerConnectionName,
subscriptionId,
properties
)
SELECT 
'{{ networkManagerConnectionName }}',
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

Deletes the specified <code>subscription_network_manager_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.subscription_network_manager_connections
WHERE networkManagerConnectionName = '{{ networkManagerConnectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
