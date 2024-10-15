---
title: virtual_hub_bgp_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_bgp_connections
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

Creates, updates, deletes, gets or lists a <code>virtual_hub_bgp_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_hub_bgp_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hub_bgp_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_hub_bgp_connections', value: 'view', },
        { label: 'virtual_hub_bgp_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of the connection. |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="hub_virtual_network_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Connection type. |
| <CopyableCode code="virtualHubName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the connection. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the bgp connection. |
| <CopyableCode code="type" /> | `string` | Connection type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of a Virtual Hub Bgp Connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all VirtualHubBgpConnections. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, virtualHubName" /> | Creates a VirtualHubBgpConnection resource if it doesn't exist else updates the existing VirtualHubBgpConnection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, virtualHubName" /> | Deletes a VirtualHubBgpConnection. |

## `SELECT` examples

Retrieves the details of all VirtualHubBgpConnections.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_hub_bgp_connections', value: 'view', },
        { label: 'virtual_hub_bgp_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connectionName,
connection_state,
etag,
hub_virtual_network_connection,
peer_asn,
peer_ip,
provisioning_state,
resourceGroupName,
subscriptionId,
type,
virtualHubName
FROM azure.network.vw_virtual_hub_bgp_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.virtual_hub_bgp_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_hub_bgp_connections</code> resource.

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
INSERT INTO azure.network.virtual_hub_bgp_connections (
connectionName,
resourceGroupName,
subscriptionId,
virtualHubName,
properties,
name,
id
)
SELECT 
'{{ connectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualHubName }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: peerAsn
          value: integer
        - name: peerIp
          value: string
        - name: hubVirtualNetworkConnection
          value:
            - name: id
              value: string
        - name: provisioningState
          value: []
        - name: connectionState
          value: string
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_hub_bgp_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_hub_bgp_connections
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
