---
title: virtual_network_taps
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_taps
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

Creates, updates, deletes, gets or lists a <code>virtual_network_taps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_taps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_taps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_taps', value: 'view', },
        { label: 'virtual_network_taps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="destination_load_balancer_front_end_ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_network_interface_ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="network_interface_tap_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tapName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Virtual Network Tap properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, tapName" /> | Gets information about the specified virtual network tap. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the VirtualNetworkTaps in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the VirtualNetworkTaps in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, tapName" /> | Creates or updates a Virtual Network Tap. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, tapName" /> | Deletes the specified virtual network tap. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, tapName" /> | Updates an VirtualNetworkTap tags. |

## `SELECT` examples

Gets all the VirtualNetworkTaps in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_taps', value: 'view', },
        { label: 'virtual_network_taps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
destination_load_balancer_front_end_ip_configuration,
destination_network_interface_ip_configuration,
destination_port,
etag,
location,
network_interface_tap_configurations,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
tags,
tapName,
type
FROM azure.network.vw_virtual_network_taps
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
FROM azure.network.virtual_network_taps
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_network_taps</code> resource.

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
INSERT INTO azure.network.virtual_network_taps (
resourceGroupName,
subscriptionId,
tapName,
properties,
id,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tapName }}',
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
                                        value:
                                          - name: description
                                            value: string
                                          - name: protocol
                                            value: string
                                          - name: sourcePortRange
                                            value: string
                                          - name: destinationPortRange
                                            value: string
                                          - name: sourceAddressPrefix
                                            value: string
                                          - name: sourceAddressPrefixes
                                            value:
                                              - string
                                          - name: sourceApplicationSecurityGroups
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
                                          - name: destinationAddressPrefix
                                            value: string
                                          - name: destinationAddressPrefixes
                                            value:
                                              - string
                                          - name: destinationApplicationSecurityGroups
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
                                          - name: sourcePortRanges
                                            value:
                                              - string
                                          - name: destinationPortRanges
                                            value:
                                              - string
                                          - name: access
                                            value: []
                                          - name: priority
                                            value: integer
                                          - name: direction
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
                                        value:
                                          - name: name
                                            value: string
                                          - name: type
                                            value: []
                                      - name: properties
                                        value:
                                          - name: privateEndpoint
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
                                          - name: ipConfigurations
                                            value:
                                              - - name: name
                                                  value: string
                                                - name: etag
                                                  value: string
                                                - name: type
                                                  value: string
                                                - name: id
                                                  value: string
                                          - name: tapConfigurations
                                            value:
                                              - - name: name
                                                  value: string
                                                - name: etag
                                                  value: string
                                                - name: type
                                                  value: string
                                                - name: id
                                                  value: string
                                          - name: dnsSettings
                                            value:
                                              - name: dnsServers
                                                value:
                                                  - string
                                              - name: appliedDnsServers
                                                value:
                                                  - string
                                              - name: internalDnsNameLabel
                                                value: string
                                              - name: internalFqdn
                                                value: string
                                              - name: internalDomainNameSuffix
                                                value: string
                                          - name: macAddress
                                            value: string
                                          - name: primary
                                            value: boolean
                                          - name: vnetEncryptionSupported
                                            value: boolean
                                          - name: enableAcceleratedNetworking
                                            value: boolean
                                          - name: disableTcpStateTracking
                                            value: boolean
                                          - name: enableIPForwarding
                                            value: boolean
                                          - name: hostedWorkloads
                                            value:
                                              - string
                                          - name: resourceGuid
                                            value: string
                                          - name: workloadType
                                            value: string
                                          - name: nicType
                                            value: string
                                          - name: privateLinkService
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
                                          - name: migrationPhase
                                            value: string
                                          - name: auxiliaryMode
                                            value: string
                                          - name: auxiliarySku
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
                                        value:
                                          - name: targetResourceId
                                            value: string
                                          - name: targetResourceGuid
                                            value: string
                                          - name: storageId
                                            value: string
                                          - name: enabledFilteringCriteria
                                            value: string
                                          - name: enabled
                                            value: boolean
                                          - name: retentionPolicy
                                            value:
                                              - name: days
                                                value: integer
                                              - name: enabled
                                                value: boolean
                                          - name: format
                                            value:
                                              - name: type
                                                value: string
                                              - name: version
                                                value: integer
                                          - name: flowAnalyticsConfiguration
                                            value:
                                              - name: networkWatcherFlowAnalyticsConfiguration
                                                value: []
                                      - name: etag
                                        value: string
                                      - name: identity
                                        value:
                                          - name: principalId
                                            value: string
                                          - name: tenantId
                                            value: string
                                          - name: type
                                            value: string
                                          - name: userAssignedIdentities
                                            value: object
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
                                        value:
                                          - name: addressPrefix
                                            value: string
                                          - name: nextHopType
                                            value: []
                                          - name: nextHopIpAddress
                                            value: string
                                          - name: hasBgpOverride
                                            value: boolean
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
                                          value:
                                            - name: description
                                              value: string
                                            - name: service
                                              value: string
                                            - name: serviceResources
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
                        - name: ipConfigurations
                          value:
                            - - name: properties
                                value:
                                  - name: privateIPAddress
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_network_taps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_network_taps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tapName = '{{ tapName }}';
```
