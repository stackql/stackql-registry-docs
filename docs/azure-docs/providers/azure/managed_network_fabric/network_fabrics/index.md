---
title: network_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabrics
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

Creates, updates, deletes, gets or lists a <code>network_fabrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_fabrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_fabrics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_fabrics', value: 'view', },
        { label: 'network_fabrics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv4_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipv6_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="l2_isolation_domains" /> | `text` | field from the `properties` object |
| <CopyableCode code="l3_isolation_domains" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="management_network_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkFabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_fabric_controller_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_fabric_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="racks" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="router_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_count_per_rack" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="terminal_server_configuration" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Fabric Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Get Network Fabric resource details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Fabric resources in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the Network Fabric resources in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId, data__properties" /> | Create Network Fabric resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Delete Network Fabric resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Fabric resource. |
| <CopyableCode code="commit_configuration" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Atomic update of the given Network Fabric instance. Sync update of NFA resources at Fabric level. |
| <CopyableCode code="deprovision" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Deprovisions the underlying resources in the given Network Fabric instance. |
| <CopyableCode code="provision" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Provisions the underlying resources in the given Network Fabric instance. |
| <CopyableCode code="refresh_configuration" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Refreshes the configuration of the underlying resources in the given Network Fabric instance. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Upgrades the version of the underlying resources in the given Network Fabric instance. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Validates the configuration of the underlying resources in the given Network Fabric instance. |

## `SELECT` examples

List all the Network Fabric resources in the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_fabrics', value: 'view', },
        { label: 'network_fabrics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
configuration_state,
fabric_asn,
fabric_version,
ipv4_prefix,
ipv6_prefix,
l2_isolation_domains,
l3_isolation_domains,
location,
management_network_configuration,
networkFabricName,
network_fabric_controller_id,
network_fabric_sku,
provisioning_state,
rack_count,
racks,
resourceGroupName,
router_ids,
server_count_per_rack,
subscriptionId,
tags,
terminal_server_configuration
FROM azure.managed_network_fabric.vw_network_fabrics
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.network_fabrics
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_fabrics</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_fabrics (
networkFabricName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ networkFabricName }}',
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
        - name: networkFabricSku
          value: string
        - name: fabricVersion
          value: string
        - name: routerIds
          value:
            - string
        - name: networkFabricControllerId
          value: []
        - name: rackCount
          value: integer
        - name: serverCountPerRack
          value: integer
        - name: ipv4Prefix
          value: string
        - name: ipv6Prefix
          value: string
        - name: fabricASN
          value: integer
        - name: terminalServerConfiguration
          value:
            - name: networkDeviceId
              value: string
            - name: username
              value: string
            - name: password
              value: string
            - name: serialNumber
              value: string
            - name: primaryIpv4Prefix
              value: string
            - name: primaryIpv6Prefix
              value: string
            - name: secondaryIpv4Prefix
              value: string
            - name: secondaryIpv6Prefix
              value: string
        - name: managementNetworkConfiguration
          value:
            - name: infrastructureVpnConfiguration
              value:
                - name: networkToNetworkInterconnectId
                  value: []
                - name: administrativeState
                  value: []
                - name: peeringOption
                  value: []
                - name: optionBProperties
                  value:
                    - name: importRouteTargets
                      value:
                        - string
                    - name: exportRouteTargets
                      value:
                        - string
                    - name: routeTargets
                      value:
                        - name: importIpv4RouteTargets
                          value:
                            - string
                        - name: importIpv6RouteTargets
                          value:
                            - string
                        - name: exportIpv4RouteTargets
                          value:
                            - string
                        - name: exportIpv6RouteTargets
                          value:
                            - string
                - name: optionAProperties
                  value: object
        - name: racks
          value:
            - string
        - name: l2IsolationDomains
          value:
            - string
        - name: l3IsolationDomains
          value:
            - string
        - name: configurationState
          value: []
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

Updates a <code>network_fabrics</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_fabrics
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
networkFabricName = '{{ networkFabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_fabrics</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_fabrics
WHERE networkFabricName = '{{ networkFabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
