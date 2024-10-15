---
title: vpn_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connections
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

Creates, updates, deletes, gets or lists a <code>vpn_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_connections', value: 'view', },
        { label: 'vpn_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_bandwidth" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="dpd_timeout_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="egress_bytes_transferred" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_bgp" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_internet_security" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_rate_limiting" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_bytes_transferred" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipsec_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_vpn_site" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_weight" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="traffic_selector_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_local_azure_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_policy_based_traffic_selectors" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_connection_protocol_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_link_connections" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnConnection. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, gatewayName, resourceGroupName, subscriptionId" /> | Retrieves the details of a vpn connection. |
| <CopyableCode code="list_by_vpn_gateway" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Retrieves all vpn connections for a particular virtual wan vpn gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, gatewayName, resourceGroupName, subscriptionId" /> | Creates a vpn connection to a scalable vpn gateway if it doesn't exist else updates the existing connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, gatewayName, resourceGroupName, subscriptionId" /> | Deletes a vpn connection. |
| <CopyableCode code="start_packet_capture" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId, vpnConnectionName" /> | Starts packet capture on Vpn connection in the specified resource group. |
| <CopyableCode code="stop_packet_capture" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId, vpnConnectionName" /> | Stops packet capture on Vpn connection in the specified resource group. |

## `SELECT` examples

Retrieves all vpn connections for a particular virtual wan vpn gateway.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_connections', value: 'view', },
        { label: 'vpn_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connectionName,
connection_bandwidth,
connection_status,
dpd_timeout_seconds,
egress_bytes_transferred,
enable_bgp,
enable_internet_security,
enable_rate_limiting,
etag,
gatewayName,
ingress_bytes_transferred,
ipsec_policies,
provisioning_state,
remote_vpn_site,
resourceGroupName,
routing_configuration,
routing_weight,
shared_key,
subscriptionId,
traffic_selector_policies,
use_local_azure_ip_address,
use_policy_based_traffic_selectors,
vpn_connection_protocol_type,
vpn_link_connections
FROM azure.network.vw_vpn_connections
WHERE gatewayName = '{{ gatewayName }}'
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
properties
FROM azure.network.vpn_connections
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpn_connections</code> resource.

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
INSERT INTO azure.network.vpn_connections (
connectionName,
gatewayName,
resourceGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ connectionName }}',
'{{ gatewayName }}',
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
        - name: remoteVpnSite
          value:
            - name: id
              value: string
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>vpn_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.vpn_connections
WHERE connectionName = '{{ connectionName }}'
AND gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
