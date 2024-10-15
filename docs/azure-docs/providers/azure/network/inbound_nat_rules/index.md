---
title: inbound_nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_nat_rules
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

Creates, updates, deletes, gets or lists a <code>inbound_nat_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inbound_nat_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.inbound_nat_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_inbound_nat_rules', value: 'view', },
        { label: 'inbound_nat_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within the set of inbound NAT rules used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="backend_address_pool" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_floating_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_tcp_reset" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="frontend_ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend_port_range_end" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend_port_range_start" /> | `text` | field from the `properties` object |
| <CopyableCode code="idle_timeout_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="inboundNatRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="loadBalancerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within the set of inbound NAT rules used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the inbound NAT rule. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId" /> | Gets the specified load balancer inbound NAT rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets all the inbound NAT rules in a load balancer. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId" /> | Creates or updates a load balancer inbound NAT rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="inboundNatRuleName, loadBalancerName, resourceGroupName, subscriptionId" /> | Deletes the specified load balancer inbound NAT rule. |

## `SELECT` examples

Gets all the inbound NAT rules in a load balancer.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_inbound_nat_rules', value: 'view', },
        { label: 'inbound_nat_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backend_address_pool,
backend_ip_configuration,
backend_port,
enable_floating_ip,
enable_tcp_reset,
etag,
frontend_ip_configuration,
frontend_port,
frontend_port_range_end,
frontend_port_range_start,
idle_timeout_in_minutes,
inboundNatRuleName,
loadBalancerName,
protocol,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.network.vw_inbound_nat_rules
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
FROM azure.network.inbound_nat_rules
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>inbound_nat_rules</code> resource.

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
INSERT INTO azure.network.inbound_nat_rules (
inboundNatRuleName,
loadBalancerName,
resourceGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ inboundNatRuleName }}',
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
        - name: frontendIPConfiguration
          value:
            - name: id
              value: string
        - name: backendIPConfiguration
          value:
            - name: properties
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
                    - - name: name
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>inbound_nat_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.inbound_nat_rules
WHERE inboundNatRuleName = '{{ inboundNatRuleName }}'
AND loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
