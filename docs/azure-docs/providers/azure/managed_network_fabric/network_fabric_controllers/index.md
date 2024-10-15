---
title: network_fabric_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabric_controllers
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_fabric_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_fabric_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_fabric_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_fabric_controllers', value: 'view', },
        { label: 'network_fabric_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure_express_route_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure_services" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv4_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv6_address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_workload_management_network_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkFabricControllerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_fabric_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="nfc_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tenant_internet_gateway_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_express_route_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_management_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_services" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | NetworkFabricControllerProperties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricControllerName, resourceGroupName, subscriptionId" /> | Shows the provisioning status of Network Fabric Controller. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the NetworkFabricControllers thats available in the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the NetworkFabricControllers by subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkFabricControllerName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Network Fabric Controller. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFabricControllerName, resourceGroupName, subscriptionId" /> | Deletes the Network Fabric Controller resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkFabricControllerName, resourceGroupName, subscriptionId" /> | Updates are currently not supported for the Network Fabric Controller resource. |

## `SELECT` examples

Lists all the NetworkFabricControllers by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_fabric_controllers', value: 'view', },
        { label: 'network_fabric_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
annotation,
infrastructure_express_route_connections,
infrastructure_services,
ipv4_address_space,
ipv6_address_space,
is_workload_management_network_enabled,
location,
managed_resource_group_configuration,
networkFabricControllerName,
network_fabric_ids,
nfc_sku,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
tenant_internet_gateway_ids,
workload_express_route_connections,
workload_management_network,
workload_services
FROM azure.managed_network_fabric.vw_network_fabric_controllers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.network_fabric_controllers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_fabric_controllers</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_fabric_controllers (
networkFabricControllerName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ networkFabricControllerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: annotation
          value: string
        - name: infrastructureExpressRouteConnections
          value:
            - - name: expressRouteCircuitId
                value: string
              - name: expressRouteAuthorizationKey
                value: string
        - name: workloadExpressRouteConnections
          value:
            - - name: expressRouteCircuitId
                value: string
              - name: expressRouteAuthorizationKey
                value: string
        - name: infrastructureServices
          value:
            - name: ipv4AddressSpaces
              value:
                - string
            - name: ipv6AddressSpaces
              value:
                - string
        - name: managedResourceGroupConfiguration
          value:
            - name: name
              value: string
            - name: location
              value: string
        - name: networkFabricIds
          value:
            - []
        - name: workloadManagementNetwork
          value: boolean
        - name: isWorkloadManagementNetworkEnabled
          value: string
        - name: tenantInternetGatewayIds
          value:
            - []
        - name: ipv4AddressSpace
          value: string
        - name: ipv6AddressSpace
          value: string
        - name: nfcSku
          value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_fabric_controllers</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_fabric_controllers
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
networkFabricControllerName = '{{ networkFabricControllerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_fabric_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_fabric_controllers
WHERE networkFabricControllerName = '{{ networkFabricControllerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
