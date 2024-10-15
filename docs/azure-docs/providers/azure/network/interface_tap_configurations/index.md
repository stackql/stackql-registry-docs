---
title: interface_tap_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - interface_tap_configurations
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

Creates, updates, deletes, gets or lists a <code>interface_tap_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interface_tap_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.interface_tap_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_interface_tap_configurations', value: 'view', },
        { label: 'interface_tap_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="networkInterfaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tapConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Sub Resource type. |
| <CopyableCode code="virtual_network_tap" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of Virtual Network Tap configuration. |
| <CopyableCode code="type" /> | `string` | Sub Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId, tapConfigurationName" /> | Get the specified tap configuration on a network interface. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | Get all Tap configurations in a network interface. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId, tapConfigurationName" /> | Creates or updates a Tap configuration in the specified NetworkInterface. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId, tapConfigurationName" /> | Deletes the specified tap configuration from the NetworkInterface. |

## `SELECT` examples

Get all Tap configurations in a network interface.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_interface_tap_configurations', value: 'view', },
        { label: 'interface_tap_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
networkInterfaceName,
provisioning_state,
resourceGroupName,
subscriptionId,
tapConfigurationName,
type,
virtual_network_tap
FROM azure.network.vw_interface_tap_configurations
WHERE networkInterfaceName = '{{ networkInterfaceName }}'
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
FROM azure.network.interface_tap_configurations
WHERE networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>interface_tap_configurations</code> resource.

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
INSERT INTO azure.network.interface_tap_configurations (
networkInterfaceName,
resourceGroupName,
subscriptionId,
tapConfigurationName,
properties,
name,
id
)
SELECT 
'{{ networkInterfaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tapConfigurationName }}',
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
        - name: virtualNetworkTap
          value:
            - name: properties
              value:
                - name: networkInterfaceTapConfigurations
                  value:
                    - - name: name
                        value: string
                      - name: etag
                        value: string
                      - name: type
                        value: string
                      - name: id
                        value: string
                - name: resourceGuid
                  value: string
                - name: provisioningState
                  value: []
                - name: destinationNetworkInterfaceIPConfiguration
                  value:
                    - name: properties
                      value:
                        - name: gatewayLoadBalancer
                          value:
                            - name: id
                              value: string
                        - name: virtualNetworkTaps
                          value:
                            - - name: etag
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
                            - - name: properties
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
                                      - - name: name
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
                                      value:
                                        - name: flushConnection
                                          value: boolean
                                        - name: securityRules
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
                                        - name: defaultSecurityRules
                                          value:
                                            - - name: name
                                                value: string
                                              - name: etag
                                                value: string
                                              - name: type
                                                value: string
                                              - name: id
                                                value: string
                                        - name: networkInterfaces
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
                                        - name: subnets
                                          value:
                                            - - name: name
                                                value: string
                                              - name: etag
                                                value: string
                                              - name: type
                                                value: string
                                              - name: id
                                                value: string
                                        - name: flowLogs
                                          value:
                                            - - name: properties
                                                value: []
                                              - name: etag
                                                value: string
                                              - name: identity
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
                                - name: routeTable
                                  value:
                                    - name: properties
                                      value:
                                        - name: routes
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
                                        - name: subnets
                                          value:
                                            - - name: name
                                                value: string
                                              - name: etag
                                                value: string
                                              - name: type
                                                value: string
                                              - name: id
                                                value: string
                                        - name: disableBgpRoutePropagation
                                          value: boolean
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
                                        value:
                                          - name: serviceEndpointPolicyDefinitions
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
                                          - name: subnets
                                            value:
                                              - - name: name
                                                  value: string
                                                - name: etag
                                                  value: string
                                                - name: type
                                                  value: string
                                                - name: id
                                                  value: string
                                          - name: resourceGuid
                                            value: string
                                          - name: serviceAlias
                                            value: string
                                          - name: contextualServiceEndpointPolicies
                                            value:
                                              - string
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
                                    - - name: properties
                                        value:
                                          - name: networkInterfaces
                                            value:
                                              - - name: etag
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
                                          - name: privateLinkServiceConnections
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
                                          - name: manualPrivateLinkServiceConnections
                                            value:
                                              - - name: name
                                                  value: string
                                                - name: type
                                                  value: string
                                                - name: etag
                                                  value: string
                                                - name: id
                                                  value: string
                                          - name: customDnsConfigs
                                            value:
                                              - - name: fqdn
                                                  value: string
                                                - name: ipAddresses
                                                  value:
                                                    - string
                                          - name: applicationSecurityGroups
                                            value:
                                              - - name: properties
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
                                                - name: type
                                                  value: string
                                                - name: etag
                                                  value: string
                                          - name: customNetworkInterfaceName
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
                                - name: ipConfigurations
                                  value:
                                    - - name: properties
                                        value:
                                          - name: privateIPAddress
                                            value: string
                                          - name: publicIPAddress
                                            value:
                                              - name: sku
                                                value: []
                                              - name: properties
                                                value: []
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
                                        value:
                                          - name: linkedResourceType
                                            value: string
                                          - name: link
                                            value: string
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
                                        value:
                                          - name: linkedResourceType
                                            value: string
                                          - name: link
                                            value: string
                                          - name: allowDelete
                                            value: boolean
                                          - name: locations
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
                                - name: delegations
                                  value:
                                    - - name: properties
                                        value:
                                          - name: serviceName
                                            value: string
                                          - name: actions
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
                        - name: primary
                          value: boolean
                        - name: applicationSecurityGroups
                          value:
                            - - name: etag
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

Deletes the specified <code>interface_tap_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.interface_tap_configurations
WHERE networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tapConfigurationName = '{{ tapConfigurationName }}';
```
