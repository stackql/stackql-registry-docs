---
title: local_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - local_network_gateways
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

Creates, updates, deletes, gets or lists a <code>local_network_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_network_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.local_network_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_local_network_gateways', value: 'view', },
        { label: 'local_network_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="bgp_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="localNetworkGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_network_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | LocalNetworkGateway properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="localNetworkGatewayName, resourceGroupName, subscriptionId" /> | Gets the specified local network gateway in a resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the local network gateways in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="localNetworkGatewayName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a local network gateway in the specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="localNetworkGatewayName, resourceGroupName, subscriptionId" /> | Deletes the specified local network gateway. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="localNetworkGatewayName, resourceGroupName, subscriptionId" /> | Updates a local network gateway tags. |

## `SELECT` examples

Gets all the local network gateways in a resource group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_local_network_gateways', value: 'view', },
        { label: 'local_network_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bgp_settings,
etag,
fqdn,
gateway_ip_address,
localNetworkGatewayName,
local_network_address_space,
location,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
tags,
type
FROM azure.network.vw_local_network_gateways
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.network.local_network_gateways
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>local_network_gateways</code> resource.

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
INSERT INTO azure.network.local_network_gateways (
localNetworkGatewayName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
id,
location,
tags
)
SELECT 
'{{ localNetworkGatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: properties
      value:
        - name: localNetworkAddressSpace
          value:
            - name: addressPrefixes
              value:
                - string
        - name: gatewayIpAddress
          value: string
        - name: fqdn
          value: string
        - name: bgpSettings
          value:
            - name: asn
              value: integer
            - name: bgpPeeringAddress
              value: string
            - name: peerWeight
              value: integer
            - name: bgpPeeringAddresses
              value:
                - - name: ipconfigurationId
                    value: string
                  - name: defaultBgpIpAddresses
                    value:
                      - string
                  - name: customBgpIpAddresses
                    value:
                      - string
                  - name: tunnelIpAddresses
                    value:
                      - string
        - name: resourceGuid
          value: string
        - name: provisioningState
          value: []
    - name: etag
      value: string
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

Deletes the specified <code>local_network_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.local_network_gateways
WHERE localNetworkGatewayName = '{{ localNetworkGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
