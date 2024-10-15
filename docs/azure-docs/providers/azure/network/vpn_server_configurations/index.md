---
title: vpn_server_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_server_configurations
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

Creates, updates, deletes, gets or lists a <code>vpn_server_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_server_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_server_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_server_configurations', value: 'view', },
        { label: 'vpn_server_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="aad_authentication_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_policy_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="p2_s_vpn_gateways" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="radius_client_root_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="radius_server_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="radius_server_root_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="radius_server_secret" /> | `text` | field from the `properties` object |
| <CopyableCode code="radius_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="vpnServerConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_authentication_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_client_ipsec_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_client_revoked_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_client_root_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_protocols" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnServerConfiguration. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vpnServerConfigurationName" /> | Retrieves the details of a VpnServerConfiguration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the VpnServerConfigurations in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the vpnServerConfigurations in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vpnServerConfigurationName" /> | Creates a VpnServerConfiguration resource if it doesn't exist else updates the existing VpnServerConfiguration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vpnServerConfigurationName" /> | Deletes a VpnServerConfiguration. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vpnServerConfigurationName" /> | Updates VpnServerConfiguration tags. |

## `SELECT` examples

Lists all the VpnServerConfigurations in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_server_configurations', value: 'view', },
        { label: 'vpn_server_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
aad_authentication_parameters,
configuration_policy_groups,
etag,
location,
p2_s_vpn_gateways,
provisioning_state,
radius_client_root_certificates,
radius_server_address,
radius_server_root_certificates,
radius_server_secret,
radius_servers,
resourceGroupName,
subscriptionId,
tags,
type,
vpnServerConfigurationName,
vpn_authentication_types,
vpn_client_ipsec_policies,
vpn_client_revoked_certificates,
vpn_client_root_certificates,
vpn_protocols
FROM azure.network.vw_vpn_server_configurations
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
FROM azure.network.vpn_server_configurations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpn_server_configurations</code> resource.

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
INSERT INTO azure.network.vpn_server_configurations (
resourceGroupName,
subscriptionId,
vpnServerConfigurationName,
properties,
id,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vpnServerConfigurationName }}',
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
        - name: name
          value: string
        - name: vpnProtocols
          value:
            - string
        - name: vpnAuthenticationTypes
          value:
            - string
        - name: vpnClientRootCertificates
          value:
            - - name: name
                value: string
              - name: publicCertData
                value: string
        - name: vpnClientRevokedCertificates
          value:
            - - name: name
                value: string
              - name: thumbprint
                value: string
        - name: radiusServerRootCertificates
          value:
            - - name: name
                value: string
              - name: publicCertData
                value: string
        - name: radiusClientRootCertificates
          value:
            - - name: name
                value: string
              - name: thumbprint
                value: string
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
        - name: aadAuthenticationParameters
          value:
            - name: aadTenant
              value: string
            - name: aadAudience
              value: string
            - name: aadIssuer
              value: string
        - name: provisioningState
          value: string
        - name: p2SVpnGateways
          value:
            - - name: properties
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
        - name: configurationPolicyGroups
          value:
            - - name: etag
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: etag
          value: string
    - name: name
      value: string
    - name: etag
      value: string
    - name: id
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

Deletes the specified <code>vpn_server_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.vpn_server_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vpnServerConfigurationName = '{{ vpnServerConfigurationName }}';
```
