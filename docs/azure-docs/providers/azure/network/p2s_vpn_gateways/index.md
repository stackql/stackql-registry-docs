---
title: p2s_vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - p2s_vpn_gateways
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

Creates, updates, deletes, gets or lists a <code>p2s_vpn_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>p2s_vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.p2s_vpn_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_p2s_vpn_gateways', value: 'view', },
        { label: 'p2s_vpn_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="custom_dns_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_routing_preference_internet" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="p2_s_connection_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_hub" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_client_connection_health" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_gateway_scale_unit" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_server_configuration" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Parameters for P2SVpnGateway. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Retrieves the details of a virtual wan p2s vpn gateway. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the P2SVpnGateways in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the P2SVpnGateways in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId, data__location" /> | Creates a virtual wan p2s vpn gateway if it doesn't exist else updates the existing gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Deletes a virtual wan p2s vpn gateway. |
| <CopyableCode code="disconnect_p2s_vpn_connections" /> | `EXEC` | <CopyableCode code="p2sVpnGatewayName, resourceGroupName, subscriptionId" /> | Disconnect P2S vpn connections of the virtual wan P2SVpnGateway in the specified resource group. |
| <CopyableCode code="generate_vpn_profile" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Resets the primary of the p2s vpn gateway in the specified resource group. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Updates virtual wan p2s vpn gateway tags. |

## `SELECT` examples

Lists all the P2SVpnGateways in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_p2s_vpn_gateways', value: 'view', },
        { label: 'p2s_vpn_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_dns_servers,
etag,
gatewayName,
is_routing_preference_internet,
location,
p2_s_connection_configurations,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type,
virtual_hub,
vpn_client_connection_health,
vpn_gateway_scale_unit,
vpn_server_configuration
FROM azure.network.vw_p2s_vpn_gateways
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
FROM azure.network.p2s_vpn_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>p2s_vpn_gateways</code> resource.

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
INSERT INTO azure.network.p2s_vpn_gateways (
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
        - name: p2SConnectionConfigurations
          value:
            - - name: properties
                value:
                  - name: vpnClientAddressPool
                    value:
                      - name: addressPrefixes
                        value:
                          - string
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
                  - name: enableInternetSecurity
                    value: boolean
                  - name: configurationPolicyGroupAssociations
                    value:
                      - - name: id
                          value: string
                  - name: previousConfigurationPolicyGroupAssociations
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
                            - name: p2SConnectionConfigurations
                              value:
                                - - name: id
                                    value: string
                            - name: provisioningState
                              value: []
                        - name: etag
                          value: string
                        - name: name
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
              - name: name
                value: string
              - name: etag
                value: string
              - name: id
                value: string
        - name: vpnGatewayScaleUnit
          value: integer
        - name: vpnClientConnectionHealth
          value:
            - name: totalIngressBytesTransferred
              value: integer
            - name: totalEgressBytesTransferred
              value: integer
            - name: vpnClientConnectionsCount
              value: integer
            - name: allocatedIpAddresses
              value:
                - string
        - name: customDnsServers
          value:
            - string
        - name: isRoutingPreferenceInternet
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

Deletes the specified <code>p2s_vpn_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.p2s_vpn_gateways
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
