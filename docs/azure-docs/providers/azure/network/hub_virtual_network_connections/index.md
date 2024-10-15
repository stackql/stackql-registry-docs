---
title: hub_virtual_network_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - hub_virtual_network_connections
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

Creates, updates, deletes, gets or lists a <code>hub_virtual_network_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hub_virtual_network_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.hub_virtual_network_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hub_virtual_network_connections', value: 'view', },
        { label: 'hub_virtual_network_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="allow_hub_to_remote_vnet_transit" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_remote_vnet_to_use_hub_vnet_gateways" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_internet_security" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_virtual_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualHubName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for HubVirtualNetworkConnection. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of a HubVirtualNetworkConnection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all HubVirtualNetworkConnections. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, virtualHubName" /> | Creates a hub virtual network connection if it doesn't exist else updates the existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, virtualHubName" /> | Deletes a HubVirtualNetworkConnection. |

## `SELECT` examples

Retrieves the details of all HubVirtualNetworkConnections.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hub_virtual_network_connections', value: 'view', },
        { label: 'hub_virtual_network_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allow_hub_to_remote_vnet_transit,
allow_remote_vnet_to_use_hub_vnet_gateways,
connectionName,
enable_internet_security,
etag,
provisioning_state,
remote_virtual_network,
resourceGroupName,
routing_configuration,
subscriptionId,
virtualHubName
FROM azure.network.vw_hub_virtual_network_connections
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
properties
FROM azure.network.hub_virtual_network_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hub_virtual_network_connections</code> resource.

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
INSERT INTO azure.network.hub_virtual_network_connections (
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
        - name: remoteVirtualNetwork
          value:
            - name: id
              value: string
        - name: allowHubToRemoteVnetTransit
          value: boolean
        - name: allowRemoteVnetToUseHubVnetGateways
          value: boolean
        - name: enableInternetSecurity
          value: boolean
        - name: routingConfiguration
          value:
            - name: propagatedRouteTables
              value:
                - name: labels
                  value:
                    - string
                - name: ids
                  value:
                    - - name: id
                        value: string
            - name: vnetRoutes
              value:
                - name: staticRoutesConfig
                  value:
                    - name: propagateStaticRoutes
                      value: boolean
                    - name: vnetLocalRouteOverrideCriteria
                      value: []
                - name: staticRoutes
                  value:
                    - - name: name
                        value: string
                      - name: addressPrefixes
                        value:
                          - string
                      - name: nextHopIpAddress
                        value: string
                - name: bgpConnections
                  value:
                    - - name: id
                        value: string
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: etag
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>hub_virtual_network_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.hub_virtual_network_connections
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
