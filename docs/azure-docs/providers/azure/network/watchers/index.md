---
title: watchers
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers
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

Creates, updates, deletes, gets or lists a <code>watchers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchers', value: 'view', },
        { label: 'watchers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="networkWatcherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The network watcher properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Gets the specified network watcher by resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all network watchers by resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all network watchers by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Creates or updates a network watcher in the specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Deletes the specified network watcher resource. |
| <CopyableCode code="check_connectivity" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__destination, data__source" /> | Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server. |
| <CopyableCode code="set_flow_log_configuration" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__properties, data__targetResourceId" /> | Configures flow log and traffic analytics (optional) on a specified resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Updates a network watcher tags. |
| <CopyableCode code="verify_ip_flow" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__direction, data__localIPAddress, data__localPort, data__protocol, data__remoteIPAddress, data__remotePort, data__targetResourceId" /> | Verify IP flow from the specified VM to a location given the currently configured NSG rules. |

## `SELECT` examples

Gets all network watchers by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchers', value: 'view', },
        { label: 'watchers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
location,
networkWatcherName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.network.vw_watchers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.watchers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>watchers</code> resource.

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
INSERT INTO azure.network.watchers (
networkWatcherName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ networkWatcherName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ id }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>watchers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.watchers
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
