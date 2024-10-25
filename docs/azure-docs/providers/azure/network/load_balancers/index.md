---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - network
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>load_balancers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="properties" /> | `object` | Properties of the load balancer. |
| <CopyableCode code="sku" /> | `object` | SKU of a load balancer. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets the specified load balancer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the load balancers in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the load balancers in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Creates or updates a load balancer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Deletes the specified load balancer. |
| <CopyableCode code="migrate_to_ip_based" /> | `EXEC` | <CopyableCode code="groupName, loadBalancerName, subscriptionId" /> | Migrate load balancer to IP Based |
| <CopyableCode code="swap_public_ip_addresses" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Swaps VIPs between two load balancers. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Updates a load balancer tags. |

## `SELECT` examples

Gets all the load balancers in a subscription.


```sql
SELECT
id,
name,
etag,
extendedLocation,
properties,
sku,
systemData,
type
FROM azure.network.load_balancers
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>load_balancers</code> resource.

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
INSERT INTO azure.network.load_balancers (
loadBalancerName,
resourceGroupName,
subscriptionId,
extendedLocation,
sku,
properties
)
SELECT 
'{{ loadBalancerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ extendedLocation }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: properties
      value:
        - name: frontendIPConfigurations
          value:
            - - name: properties
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
                                                  - name: systemData
                                                    value: []
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
                                      - - name: properties
                                          value:
                                            - name: virtualMachine
                                              value:
                                                - name: id
                                                  value: string
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
                                            - name: ipConfigurations
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
                                            - name: tapConfigurations
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
        - name: backendAddressPools
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
        - name: loadBalancingRules
          value:
            - - name: properties
                value:
                  - name: backendAddressPools
                    value:
                      - - name: id
                          value: string
                  - name: protocol
                    value: []
                  - name: loadDistribution
                    value: string
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
                  - name: disableOutboundSnat
                    value: boolean
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: probes
          value:
            - - name: properties
                value:
                  - name: loadBalancingRules
                    value:
                      - - name: id
                          value: string
                  - name: protocol
                    value: string
                  - name: port
                    value: integer
                  - name: intervalInSeconds
                    value: integer
                  - name: noHealthyBackendsBehavior
                    value: string
                  - name: numberOfProbes
                    value: integer
                  - name: probeThreshold
                    value: integer
                  - name: requestPath
                    value: string
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: inboundNatRules
          value:
            - - name: properties
                value:
                  - name: backendIPConfiguration
                    value:
                      - name: name
                        value: string
                      - name: etag
                        value: string
                      - name: type
                        value: string
                      - name: id
                        value: string
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
        - name: inboundNatPools
          value:
            - - name: properties
                value:
                  - name: frontendPortRangeStart
                    value: integer
                  - name: frontendPortRangeEnd
                    value: integer
                  - name: backendPort
                    value: integer
                  - name: idleTimeoutInMinutes
                    value: integer
                  - name: enableFloatingIP
                    value: boolean
                  - name: enableTcpReset
                    value: boolean
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: outboundRules
          value:
            - - name: properties
                value:
                  - name: allocatedOutboundPorts
                    value: integer
                  - name: frontendIPConfigurations
                    value:
                      - - name: id
                          value: string
                  - name: protocol
                    value: string
                  - name: enableTcpReset
                    value: boolean
                  - name: idleTimeoutInMinutes
                    value: integer
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
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>load_balancers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.load_balancers
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
