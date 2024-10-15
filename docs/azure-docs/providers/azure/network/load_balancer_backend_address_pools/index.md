---
title: load_balancer_backend_address_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_backend_address_pools
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

Creates, updates, deletes, gets or lists a <code>load_balancer_backend_address_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_backend_address_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_backend_address_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancer_backend_address_pools', value: 'view', },
        { label: 'load_balancer_backend_address_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within the set of backend address pools used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="backendAddressPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="drain_period_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="inbound_nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="loadBalancerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_backend_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancing_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="outbound_rule" /> | `text` | field from the `properties` object |
| <CopyableCode code="outbound_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="tunnel_interfaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
| <CopyableCode code="virtual_network" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within the set of backend address pools used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the backend address pool. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId" /> | Gets load balancer backend address pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets all the load balancer backed address pools. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId" /> | Creates or updates a load balancer backend address pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId" /> | Deletes the specified load balancer backend address pool. |

## `SELECT` examples

Gets all the load balancer backed address pools.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancer_backend_address_pools', value: 'view', },
        { label: 'load_balancer_backend_address_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backendAddressPoolName,
backend_ip_configurations,
drain_period_in_seconds,
etag,
inbound_nat_rules,
loadBalancerName,
load_balancer_backend_addresses,
load_balancing_rules,
location,
outbound_rule,
outbound_rules,
provisioning_state,
resourceGroupName,
subscriptionId,
sync_mode,
tunnel_interfaces,
type,
virtual_network
FROM azure.network.vw_load_balancer_backend_address_pools
WHERE loadBalancerName = '{{ loadBalancerName }}'
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
type
FROM azure.network.load_balancer_backend_address_pools
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>load_balancer_backend_address_pools</code> resource.

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
INSERT INTO azure.network.load_balancer_backend_address_pools (
backendAddressPoolName,
loadBalancerName,
resourceGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ backendAddressPoolName }}',
'{{ loadBalancerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: location
          value: string
        - name: tunnelInterfaces
          value:
            - - name: port
                value: integer
              - name: identifier
                value: integer
              - name: protocol
                value: string
              - name: type
                value: string
        - name: loadBalancerBackendAddresses
          value:
            - - name: properties
                value:
                  - name: virtualNetwork
                    value:
                      - name: id
                        value: string
                  - name: ipAddress
                    value: string
                  - name: inboundNatRulesPortMapping
                    value:
                      - - name: inboundNatRuleName
                          value: string
                        - name: frontendPort
                          value: integer
                        - name: backendPort
                          value: integer
                  - name: adminState
                    value: string
              - name: name
                value: string
        - name: backendIPConfigurations
          value:
            - - name: properties
                value:
                  - name: virtualNetworkTaps
                    value:
                      - - name: properties
                          value:
                            - name: networkInterfaceTapConfigurations
                              value:
                                - - name: properties
                                    value:
                                      - name: virtualNetworkTap
                                        value:
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
                                      - name: provisioningState
                                        value: []
                                  - name: name
                                    value: string
                                  - name: etag
                                    value: string
                                  - name: type
                                    value: string
                                  - name: id
                                    value: string
                            - name: resourceGuid
                              value: string
                            - name: destinationNetworkInterfaceIPConfiguration
                              value:
                                - name: name
                                  value: string
                                - name: etag
                                  value: string
                                - name: type
                                  value: string
                                - name: id
                                  value: string
                            - name: destinationLoadBalancerFrontEndIPConfiguration
                              value:
                                - name: properties
                                  value:
                                    - name: inboundNatRules
                                      value:
                                        - - name: id
                                            value: string
                                    - name: inboundNatPools
                                      value:
                                        - - name: id
                                            value: string
                                    - name: outboundRules
                                      value:
                                        - - name: id
                                            value: string
                                    - name: loadBalancingRules
                                      value:
                                        - - name: id
                                            value: string
                                    - name: privateIPAddress
                                      value: string
                                    - name: privateIPAllocationMethod
                                      value: []
                                    - name: privateIPAddressVersion
                                      value: []
                                    - name: subnet
                                      value:
                                        - name: properties
                                          value:
                                            - name: addressPrefix
                                              value: string
                                            - name: addressPrefixes
                                              value:
                                                - string
                                            - name: networkSecurityGroup
                                              value:
                                                - name: properties
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
                                            - name: routeTable
                                              value:
                                                - name: properties
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
                                            - name: serviceEndpoints
                                              value:
                                                - - name: service
                                                    value: string
                                                  - name: locations
                                                    value:
                                                      - string
                                            - name: serviceEndpointPolicies
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: etag
                                                    value: string
                                                  - name: kind
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
                                            - name: privateEndpoints
                                              value:
                                                - - name: extendedLocation
                                                    value: []
                                                  - name: properties
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
                                            - name: ipConfigurations
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: ipConfigurationProfiles
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: ipAllocations
                                              value:
                                                - - name: id
                                                    value: string
                                            - name: resourceNavigationLinks
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: id
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: type
                                                    value: string
                                            - name: serviceAssociationLinks
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: delegations
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: purpose
                                              value: string
                                            - name: privateEndpointNetworkPolicies
                                              value: string
                                            - name: privateLinkServiceNetworkPolicies
                                              value: string
                                            - name: applicationGatewayIPConfigurations
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: sharingScope
                                              value: string
                                            - name: defaultOutboundAccess
                                              value: boolean
                                        - name: name
                                          value: string
                                        - name: etag
                                          value: string
                                        - name: type
                                          value: string
                                        - name: id
                                          value: string
                                    - name: publicIPAddress
                                      value:
                                        - name: sku
                                          value:
                                            - name: name
                                              value: string
                                            - name: tier
                                              value: string
                                        - name: properties
                                          value:
                                            - name: ipConfiguration
                                              value:
                                                - name: name
                                                  value: string
                                                - name: etag
                                                  value: string
                                                - name: id
                                                  value: string
                                            - name: dnsSettings
                                              value:
                                                - name: domainNameLabel
                                                  value: string
                                                - name: domainNameLabelScope
                                                  value: string
                                                - name: fqdn
                                                  value: string
                                                - name: reverseFqdn
                                                  value: string
                                            - name: ddosSettings
                                              value:
                                                - name: protectionMode
                                                  value: string
                                            - name: ipTags
                                              value:
                                                - - name: ipTagType
                                                    value: string
                                                  - name: tag
                                                    value: string
                                            - name: ipAddress
                                              value: string
                                            - name: idleTimeoutInMinutes
                                              value: integer
                                            - name: resourceGuid
                                              value: string
                                            - name: natGateway
                                              value:
                                                - name: sku
                                                  value: []
                                                - name: properties
                                                  value: []
                                                - name: zones
                                                  value:
                                                    - string
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
                                            - name: migrationPhase
                                              value: string
                                            - name: deleteOption
                                              value: string
                                        - name: etag
                                          value: string
                                        - name: zones
                                          value:
                                            - string
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
                                - name: name
                                  value: string
                                - name: etag
                                  value: string
                                - name: type
                                  value: string
                                - name: zones
                                  value:
                                    - string
                                - name: id
                                  value: string
                            - name: destinationPort
                              value: integer
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
                  - name: applicationGatewayBackendAddressPools
                    value:
                      - - name: properties
                          value:
                            - name: backendIPConfigurations
                              value:
                                - - name: name
                                    value: string
                                  - name: etag
                                    value: string
                                  - name: type
                                    value: string
                                  - name: id
                                    value: string
                            - name: backendAddresses
                              value:
                                - - name: fqdn
                                    value: string
                                  - name: ipAddress
                                    value: string
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: loadBalancerBackendAddressPools
                    value:
                      - - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: loadBalancerInboundNatRules
                    value:
                      - - name: properties
                          value:
                            - name: protocol
                              value: []
                            - name: frontendPort
                              value: integer
                            - name: backendPort
                              value: integer
                            - name: idleTimeoutInMinutes
                              value: integer
                            - name: enableFloatingIP
                              value: boolean
                            - name: enableTcpReset
                              value: boolean
                            - name: frontendPortRangeStart
                              value: integer
                            - name: frontendPortRangeEnd
                              value: integer
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: privateIPAddress
                    value: string
                  - name: privateIPAddressPrefixLength
                    value: integer
                  - name: primary
                    value: boolean
                  - name: applicationSecurityGroups
                    value:
                      - - name: properties
                          value:
                            - name: resourceGuid
                              value: string
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
                  - name: privateLinkConnectionProperties
                    value:
                      - name: groupId
                        value: string
                      - name: requiredMemberName
                        value: string
                      - name: fqdns
                        value:
                          - string
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: loadBalancingRules
          value:
            - - name: id
                value: string
        - name: outboundRules
          value:
            - - name: id
                value: string
        - name: inboundNatRules
          value:
            - - name: id
                value: string
        - name: drainPeriodInSeconds
          value: integer
        - name: syncMode
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

Deletes the specified <code>load_balancer_backend_address_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.load_balancer_backend_address_pools
WHERE backendAddressPoolName = '{{ backendAddressPoolName }}'
AND loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
