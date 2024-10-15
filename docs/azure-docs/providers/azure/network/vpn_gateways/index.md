---
title: vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways
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

Creates, updates, deletes, gets or lists a <code>vpn_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_gateways', value: 'view', },
        { label: 'vpn_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="bgp_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_bgp_route_translation_for_nat" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_routing_preference_internet" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_hub" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_gateway_scale_unit" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnGateway. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Retrieves the details of a virtual wan vpn gateway. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the VpnGateways in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the VpnGateways in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId, data__location" /> | Creates a virtual wan vpn gateway if it doesn't exist else updates the existing gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Deletes a virtual wan vpn gateway. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Resets the primary of the vpn gateway in the specified resource group. |
| <CopyableCode code="start_packet_capture" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Starts packet capture on vpn gateway in the specified resource group. |
| <CopyableCode code="stop_packet_capture" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Stops packet capture on vpn gateway in the specified resource group. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Updates virtual wan vpn gateway tags. |

## `SELECT` examples

Lists all the VpnGateways in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_gateways', value: 'view', },
        { label: 'vpn_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bgp_settings,
connections,
enable_bgp_route_translation_for_nat,
etag,
gatewayName,
ip_configurations,
is_routing_preference_internet,
location,
nat_rules,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type,
virtual_hub,
vpn_gateway_scale_unit
FROM azure.network.vw_vpn_gateways
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
FROM azure.network.vpn_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpn_gateways</code> resource.

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
INSERT INTO azure.network.vpn_gateways (
gatewayName,
resourceGroupName,
subscriptionId,
data__location,
properties,
id,
location,
tags
)
SELECT 
'{{ gatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
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
        - name: virtualHub
          value:
            - name: id
              value: string
        - name: connections
          value:
            - - name: properties
                value:
                  - name: routingWeight
                    value: integer
                  - name: dpdTimeoutSeconds
                    value: integer
                  - name: connectionStatus
                    value: []
                  - name: vpnConnectionProtocolType
                    value: []
                  - name: ingressBytesTransferred
                    value: integer
                  - name: egressBytesTransferred
                    value: integer
                  - name: connectionBandwidth
                    value: integer
                  - name: sharedKey
                    value: string
                  - name: enableBgp
                    value: boolean
                  - name: usePolicyBasedTrafficSelectors
                    value: boolean
                  - name: ipsecPolicies
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
                  - name: trafficSelectorPolicies
                    value:
                      - - name: localAddressRanges
                          value:
                            - string
                        - name: remoteAddressRanges
                          value:
                            - string
                  - name: enableRateLimiting
                    value: boolean
                  - name: enableInternetSecurity
                    value: boolean
                  - name: useLocalAzureIpAddress
                    value: boolean
                  - name: provisioningState
                    value: []
                  - name: vpnLinkConnections
                    value:
                      - - name: properties
                          value:
                            - name: routingWeight
                              value: integer
                            - name: vpnLinkConnectionMode
                              value: string
                            - name: ingressBytesTransferred
                              value: integer
                            - name: egressBytesTransferred
                              value: integer
                            - name: connectionBandwidth
                              value: integer
                            - name: sharedKey
                              value: string
                            - name: enableBgp
                              value: boolean
                            - name: vpnGatewayCustomBgpAddresses
                              value:
                                - - name: ipConfigurationId
                                    value: string
                                  - name: customBgpIpAddress
                                    value: string
                            - name: usePolicyBasedTrafficSelectors
                              value: boolean
                            - name: ipsecPolicies
                              value:
                                - - name: saLifeTimeSeconds
                                    value: integer
                                  - name: saDataSizeKilobytes
                                    value: integer
                            - name: enableRateLimiting
                              value: boolean
                            - name: useLocalAzureIpAddress
                              value: boolean
                            - name: ingressNatRules
                              value:
                                - - name: id
                                    value: string
                            - name: egressNatRules
                              value:
                                - - name: id
                                    value: string
                            - name: dpdTimeoutSeconds
                              value: integer
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: routingConfiguration
                    value:
                      - name: propagatedRouteTables
                        value:
                          - name: labels
                            value:
                              - string
                          - name: ids
                            value:
                              - - name: id
                                  value: string
                      - name: vnetRoutes
                        value:
                          - name: staticRoutesConfig
                            value:
                              - name: propagateStaticRoutes
                                value: boolean
                              - name: vnetLocalRouteOverrideCriteria
                                value: []
                          - name: staticRoutes
                            value:
                              - - name: name
                                  value: string
                                - name: addressPrefixes
                                  value:
                                    - string
                                - name: nextHopIpAddress
                                  value: string
                          - name: bgpConnections
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
        - name: vpnGatewayScaleUnit
          value: integer
        - name: ipConfigurations
          value:
            - - name: id
                value: string
              - name: publicIpAddress
                value: string
              - name: privateIpAddress
                value: string
        - name: enableBgpRouteTranslationForNat
          value: boolean
        - name: isRoutingPreferenceInternet
          value: boolean
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
                  - name: egressVpnSiteLinkConnections
                    value:
                      - - name: id
                          value: string
                  - name: ingressVpnSiteLinkConnections
                    value:
                      - - name: id
                          value: string
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>vpn_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.vpn_gateways
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
