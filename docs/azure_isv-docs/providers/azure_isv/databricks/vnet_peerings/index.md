---
title: vnet_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - vnet_peerings
  - databricks
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

Creates, updates, deletes, gets or lists a <code>vnet_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vnet_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.databricks.vnet_peerings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vnet_peerings', value: 'view', },
        { label: 'vnet_peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of the virtual network peering resource |
| <CopyableCode code="allow_forwarded_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_gateway_transit" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_virtual_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="databricks_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="databricks_virtual_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="peeringName" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_virtual_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | type of the virtual network peering resource |
| <CopyableCode code="use_remote_gateways" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the virtual network peering resource |
| <CopyableCode code="properties" /> | `object` | Properties of the virtual network peering. |
| <CopyableCode code="type" /> | `string` | type of the virtual network peering resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the workspace vNet Peering. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists the workspace vNet Peerings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Creates vNet Peering for workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the workspace vNetPeering. |

## `SELECT` examples

Lists the workspace vNet Peerings.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vnet_peerings', value: 'view', },
        { label: 'vnet_peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allow_forwarded_traffic,
allow_gateway_transit,
allow_virtual_network_access,
databricks_address_space,
databricks_virtual_network,
peeringName,
peering_state,
provisioning_state,
remote_address_space,
remote_virtual_network,
resourceGroupName,
subscriptionId,
type,
use_remote_gateways,
workspaceName
FROM azure_isv.databricks.vw_vnet_peerings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure_isv.databricks.vnet_peerings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vnet_peerings</code> resource.

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
INSERT INTO azure_isv.databricks.vnet_peerings (
peeringName,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ peeringName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
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
        - name: allowVirtualNetworkAccess
          value: boolean
        - name: allowForwardedTraffic
          value: boolean
        - name: allowGatewayTransit
          value: boolean
        - name: useRemoteGateways
          value: boolean
        - name: databricksVirtualNetwork
          value: string
        - name: databricksAddressSpace
          value:
            - name: addressPrefixes
              value:
                - string
        - name: remoteVirtualNetwork
          value: string
        - name: peeringState
          value: string
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>vnet_peerings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.databricks.vnet_peerings
WHERE peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
