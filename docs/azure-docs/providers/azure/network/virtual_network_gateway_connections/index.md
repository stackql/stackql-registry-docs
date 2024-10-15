---
title: virtual_network_gateway_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_connections
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

Creates, updates, deletes, gets or lists a <code>virtual_network_gateway_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_gateway_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateway_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_gateway_connections', value: 'view', },
        { label: 'virtual_network_gateway_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="authorization_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="dpd_timeout_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="egress_bytes_transferred" /> | `text` | field from the `properties` object |
| <CopyableCode code="egress_nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_bgp" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_private_link_fast_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="express_route_gateway_bypass" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_custom_bgp_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_bytes_transferred" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipsec_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_network_gateway2" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="peer" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_weight" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="traffic_selector_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="tunnel_connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="use_local_azure_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_policy_based_traffic_selectors" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualNetworkGatewayConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_gateway1" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_gateway2" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | VirtualNetworkGatewayConnection properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Gets the specified virtual network gateway connection by resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__properties" /> | Creates or updates a virtual network gateway connection in the specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Deletes the specified virtual network Gateway connection. |
| <CopyableCode code="reset_connection" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Resets the virtual network gateway connection specified. |
| <CopyableCode code="reset_shared_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__keyLength" /> | The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
| <CopyableCode code="set_shared_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__value" /> | The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
| <CopyableCode code="start_packet_capture" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Starts packet capture on virtual network gateway connection in the specified resource group. |
| <CopyableCode code="stop_packet_capture" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Stops packet capture on virtual network gateway connection in the specified resource group. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Updates a virtual network gateway connection tags. |

## `SELECT` examples

The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_gateway_connections', value: 'view', },
        { label: 'virtual_network_gateway_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
authorization_key,
connection_mode,
connection_protocol,
connection_status,
connection_type,
dpd_timeout_seconds,
egress_bytes_transferred,
egress_nat_rules,
enable_bgp,
enable_private_link_fast_path,
etag,
express_route_gateway_bypass,
gateway_custom_bgp_ip_addresses,
ingress_bytes_transferred,
ingress_nat_rules,
ipsec_policies,
local_network_gateway2,
location,
peer,
provisioning_state,
resourceGroupName,
resource_guid,
routing_weight,
shared_key,
subscriptionId,
tags,
traffic_selector_policies,
tunnel_connection_status,
type,
use_local_azure_ip_address,
use_policy_based_traffic_selectors,
virtualNetworkGatewayConnectionName,
virtual_network_gateway1,
virtual_network_gateway2
FROM azure.network.vw_virtual_network_gateway_connections
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
FROM azure.network.virtual_network_gateway_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_network_gateway_connections</code> resource.

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
INSERT INTO azure.network.virtual_network_gateway_connections (
resourceGroupName,
subscriptionId,
virtualNetworkGatewayConnectionName,
data__properties,
properties,
id,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualNetworkGatewayConnectionName }}',
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
        - name: authorizationKey
          value: string
        - name: virtualNetworkGateway1
          value:
            - name: properties
              value:
                - name: autoScaleConfiguration
                  value:
                    - name: bounds
                      value:
                        - name: min
                          value: integer
                        - name: max
                          value: integer
                - name: ipConfigurations
                  value:
                    - - name: properties
                        value:
                          - name: privateIPAllocationMethod
                            value: []
                          - name: subnet
                            value:
                              - name: id
                                value: string
                          - name: privateIPAddress
                            value: string
                          - name: provisioningState
                            value: []
                      - name: name
                        value: string
                      - name: etag
                        value: string
                      - name: id
                        value: string
                - name: gatewayType
                  value: string
                - name: vpnType
                  value: string
                - name: vpnGatewayGeneration
                  value: string
                - name: enableBgp
                  value: boolean
                - name: enablePrivateIpAddress
                  value: boolean
                - name: activeActive
                  value: boolean
                - name: disableIPSecReplayProtection
                  value: boolean
                - name: sku
                  value:
                    - name: name
                      value: string
                    - name: tier
                      value: string
                    - name: capacity
                      value: integer
                - name: vpnClientConfiguration
                  value:
                    - name: vpnClientAddressPool
                      value:
                        - name: addressPrefixes
                          value:
                            - string
                    - name: vpnClientRootCertificates
                      value:
                        - - name: properties
                            value:
                              - name: publicCertData
                                value: string
                          - name: name
                            value: string
                          - name: etag
                            value: string
                          - name: id
                            value: string
                    - name: vpnClientRevokedCertificates
                      value:
                        - - name: properties
                            value:
                              - name: thumbprint
                                value: string
                          - name: name
                            value: string
                          - name: etag
                            value: string
                          - name: id
                            value: string
                    - name: vpnClientProtocols
                      value:
                        - string
                    - name: vpnAuthenticationTypes
                      value:
                        - string
                    - name: vpnClientIpsecPolicies
                      value:
                        - - name: saLifeTimeSeconds
                            value: integer
                          - name: saDataSizeKilobytes
                            value: integer
                          - name: ipsecEncryption
                            value: []
                          - name: ipsecIntegrity
                            value: []
                          - name: ikeEncryption
                            value: []
                          - name: ikeIntegrity
                            value: []
                          - name: dhGroup
                            value: []
                          - name: pfsGroup
                            value: []
                    - name: radiusServerAddress
                      value: string
                    - name: radiusServerSecret
                      value: string
                    - name: radiusServers
                      value:
                        - - name: radiusServerAddress
                            value: string
                          - name: radiusServerScore
                            value: integer
                          - name: radiusServerSecret
                            value: string
                    - name: aadTenant
                      value: string
                    - name: aadAudience
                      value: string
                    - name: aadIssuer
                      value: string
                    - name: vngClientConnectionConfigurations
                      value:
                        - - name: properties
                            value:
                              - name: virtualNetworkGatewayPolicyGroups
                                value:
                                  - - name: id
                                      value: string
                          - name: name
                            value: string
                          - name: etag
                            value: string
                          - name: id
                            value: string
                - name: virtualNetworkGatewayPolicyGroups
                  value:
                    - - name: properties
                        value:
                          - name: isDefault
                            value: boolean
                          - name: priority
                            value: integer
                          - name: policyMembers
                            value:
                              - - name: name
                                  value: string
                                - name: attributeType
                                  value: string
                                - name: attributeValue
                                  value: string
                          - name: vngClientConnectionConfigurations
                            value:
                              - - name: id
                                  value: string
                      - name: name
                        value: string
                      - name: etag
                        value: string
                      - name: id
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
                - name: enableDnsForwarding
                  value: boolean
                - name: inboundDnsForwardingEndpoint
                  value: string
                - name: vNetExtendedLocationResourceId
                  value: string
                - name: natRules
                  value:
                    - - name: properties
                        value:
                          - name: type
                            value: string
                          - name: mode
                            value: string
                          - name: internalMappings
                            value:
                              - - name: addressSpace
                                  value: string
                                - name: portRange
                                  value: string
                          - name: externalMappings
                            value:
                              - - name: addressSpace
                                  value: string
                                - name: portRange
                                  value: string
                          - name: ipConfigurationId
                            value: string
                      - name: name
                        value: string
                      - name: etag
                        value: string
                      - name: type
                        value: string
                      - name: id
                        value: string
                - name: enableBgpRouteTranslationForNat
                  value: boolean
                - name: allowVirtualWanTraffic
                  value: boolean
                - name: allowRemoteVnetTraffic
                  value: boolean
                - name: adminState
                  value: string
                - name: resiliencyModel
                  value: string
            - name: extendedLocation
              value:
                - name: name
                  value: string
                - name: type
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
        - name: localNetworkGateway2
          value:
            - name: properties
              value:
                - name: gatewayIpAddress
                  value: string
                - name: fqdn
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
            - name: location
              value: string
            - name: tags
              value: object
        - name: ingressNatRules
          value:
            - - name: id
                value: string
        - name: egressNatRules
          value:
            - - name: id
                value: string
        - name: connectionType
          value: []
        - name: connectionProtocol
          value: []
        - name: routingWeight
          value: integer
        - name: dpdTimeoutSeconds
          value: integer
        - name: connectionMode
          value: []
        - name: sharedKey
          value: string
        - name: connectionStatus
          value: []
        - name: tunnelConnectionStatus
          value:
            - - name: tunnel
                value: string
              - name: ingressBytesTransferred
                value: integer
              - name: egressBytesTransferred
                value: integer
              - name: lastConnectionEstablishedUtcTime
                value: string
        - name: egressBytesTransferred
          value: integer
        - name: ingressBytesTransferred
          value: integer
        - name: enableBgp
          value: boolean
        - name: gatewayCustomBgpIpAddresses
          value:
            - - name: ipConfigurationId
                value: string
              - name: customBgpIpAddress
                value: string
        - name: useLocalAzureIpAddress
          value: boolean
        - name: usePolicyBasedTrafficSelectors
          value: boolean
        - name: ipsecPolicies
          value:
            - - name: saLifeTimeSeconds
                value: integer
              - name: saDataSizeKilobytes
                value: integer
        - name: trafficSelectorPolicies
          value:
            - - name: localAddressRanges
                value:
                  - string
              - name: remoteAddressRanges
                value:
                  - string
        - name: resourceGuid
          value: string
        - name: expressRouteGatewayBypass
          value: boolean
        - name: enablePrivateLinkFastPath
          value: boolean
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

Deletes the specified <code>virtual_network_gateway_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_network_gateway_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkGatewayConnectionName = '{{ virtualNetworkGatewayConnectionName }}';
```
