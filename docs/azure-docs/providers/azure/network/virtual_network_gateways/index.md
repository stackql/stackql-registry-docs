---
title: virtual_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways
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

Creates, updates, deletes, gets or lists a <code>virtual_network_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_gateways', value: 'view', },
        { label: 'virtual_network_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="active_active" /> | `text` | field from the `properties` object |
| <CopyableCode code="admin_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_remote_vnet_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_virtual_wan_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_scale_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="bgp_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_routes" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_ip_sec_replay_protection" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_bgp" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_bgp_route_translation_for_nat" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_dns_forwarding" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_private_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_default_site" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="inbound_dns_forwarding_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resiliency_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtualNetworkGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_gateway_policy_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_extended_location_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_client_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_gateway_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | VirtualNetworkGateway properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Gets the specified virtual network gateway by resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all virtual network gateways by resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName, data__properties" /> | Creates or updates a virtual network gateway in the specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Deletes the specified virtual network gateway. |
| <CopyableCode code="disconnect_virtual_network_gateway_vpn_connections" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Disconnect vpn connections of virtual network gateway in the specified resource group. |
| <CopyableCode code="generate_vpn_profile" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Generates VPN profile for P2S client of the virtual network gateway in the specified resource group. Used for IKEV2 and radius based authentication. |
| <CopyableCode code="generatevpnclientpackage" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Generates VPN client package for P2S client of the virtual network gateway in the specified resource group. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Resets the primary of the virtual network gateway in the specified resource group. |
| <CopyableCode code="reset_vpn_client_shared_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Resets the VPN client shared key of the virtual network gateway in the specified resource group. |
| <CopyableCode code="set_vpnclient_ipsec_parameters" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName, data__dhGroup, data__ikeEncryption, data__ikeIntegrity, data__ipsecEncryption, data__ipsecIntegrity, data__pfsGroup, data__saDataSizeKilobytes, data__saLifeTimeSeconds" /> | The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider. |
| <CopyableCode code="start_packet_capture" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Starts packet capture on virtual network gateway in the specified resource group. |
| <CopyableCode code="stop_packet_capture" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Stops packet capture on virtual network gateway in the specified resource group. |
| <CopyableCode code="supported_vpn_devices" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Gets a xml format representation for supported vpn devices. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Updates a virtual network gateway tags. |
| <CopyableCode code="vpn_device_configuration_script" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Gets a xml format representation for vpn device configuration script. |

## `SELECT` examples

Gets all virtual network gateways by resource group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_gateways', value: 'view', },
        { label: 'virtual_network_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
active_active,
admin_state,
allow_remote_vnet_traffic,
allow_virtual_wan_traffic,
auto_scale_configuration,
bgp_settings,
custom_routes,
disable_ip_sec_replay_protection,
enable_bgp,
enable_bgp_route_translation_for_nat,
enable_dns_forwarding,
enable_private_ip_address,
etag,
extended_location,
gateway_default_site,
gateway_type,
identity,
inbound_dns_forwarding_endpoint,
ip_configurations,
location,
nat_rules,
provisioning_state,
resiliency_model,
resourceGroupName,
resource_guid,
sku,
subscriptionId,
tags,
type,
virtualNetworkGatewayName,
virtual_network_gateway_policy_groups,
vnet_extended_location_resource_id,
vpn_client_configuration,
vpn_gateway_generation,
vpn_type
FROM azure.network.vw_virtual_network_gateways
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
extendedLocation,
identity,
location,
properties,
tags,
type
FROM azure.network.virtual_network_gateways
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_network_gateways</code> resource.

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
INSERT INTO azure.network.virtual_network_gateways (
resourceGroupName,
subscriptionId,
virtualNetworkGatewayName,
data__properties,
properties,
extendedLocation,
identity,
id,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualNetworkGatewayName }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ identity }}',
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_network_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_network_gateways
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkGatewayName = '{{ virtualNetworkGatewayName }}';
```
