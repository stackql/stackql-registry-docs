---
title: public_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_addresses
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

Creates, updates, deletes, gets or lists a <code>public_ip_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.public_ip_addresses" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_ip_addresses', value: 'view', },
        { label: 'public_ip_addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="ddos_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="delete_option" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="idle_timeout_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_public_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="migration_phase" /> | `text` | field from the `properties` object |
| <CopyableCode code="nat_gateway" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publicIpAddressName" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_address_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_allocation_method" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_public_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU of a public IP address. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Public IP address properties. |
| <CopyableCode code="sku" /> | `object` | SKU of a public IP address. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Gets the specified public IP address in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all public IP addresses in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the public IP addresses in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Creates or updates a static or dynamic public IP address. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Deletes the specified public IP address. |
| <CopyableCode code="ddos_protection_status" /> | `EXEC` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Gets the Ddos Protection Status of a Public IP Address |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Updates public IP address tags. |

## `SELECT` examples

Gets all the public IP addresses in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_ip_addresses', value: 'view', },
        { label: 'public_ip_addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ddos_settings,
delete_option,
dns_settings,
etag,
extended_location,
idle_timeout_in_minutes,
ip_address,
ip_configuration,
ip_tags,
linked_public_ip_address,
location,
migration_phase,
nat_gateway,
provisioning_state,
publicIpAddressName,
public_ip_address_version,
public_ip_allocation_method,
public_ip_prefix,
resourceGroupName,
resource_guid,
service_public_ip_address,
sku,
subscriptionId,
tags,
type,
zones
FROM azure.network.vw_public_ip_addresses
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
extendedLocation,
location,
properties,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>public_ip_addresses</code> resource.

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
INSERT INTO azure.network.public_ip_addresses (
publicIpAddressName,
resourceGroupName,
subscriptionId,
extendedLocation,
sku,
properties,
zones,
id,
location,
tags
)
SELECT 
'{{ publicIpAddressName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ extendedLocation }}',
'{{ sku }}',
'{{ properties }}',
'{{ zones }}',
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
        - name: publicIPAllocationMethod
          value: []
        - name: publicIPAddressVersion
          value: []
        - name: ipConfiguration
          value:
            - name: properties
              value:
                - name: privateIPAddress
                  value: string
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
                            - - name: name
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
                - name: publicIPAddress
                  value:
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
              value:
                - name: name
                  value: string
            - name: properties
              value:
                - name: idleTimeoutInMinutes
                  value: integer
                - name: publicIpAddresses
                  value:
                    - - name: id
                        value: string
                - name: publicIpPrefixes
                  value:
                    - - name: id
                        value: string
                - name: subnets
                  value:
                    - - name: id
                        value: string
                - name: resourceGuid
                  value: string
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>public_ip_addresses</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.public_ip_addresses
WHERE publicIpAddressName = '{{ publicIpAddressName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
