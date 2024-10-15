---
title: web_application_firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - web_application_firewall_policies
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

Creates, updates, deletes, gets or lists a <code>web_application_firewall_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_application_firewall_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.web_application_firewall_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_application_firewall_policies', value: 'view', },
        { label: 'web_application_firewall_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="application_gateway_for_containers" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_gateways" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="http_listeners" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="managed_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="path_based_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Defines web application firewall policy properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Retrieve protection policy with specified name within a resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the protection policies within a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the WAF policies in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Creates or update policy with specified rule set name within a resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Deletes Policy. |

## `SELECT` examples

Gets all the WAF policies in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_web_application_firewall_policies', value: 'view', },
        { label: 'web_application_firewall_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
application_gateway_for_containers,
application_gateways,
custom_rules,
etag,
http_listeners,
location,
managed_rules,
path_based_rules,
policyName,
policy_settings,
provisioning_state,
resourceGroupName,
resource_state,
subscriptionId,
tags,
type
FROM azure.network.vw_web_application_firewall_policies
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
FROM azure.network.web_application_firewall_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>web_application_firewall_policies</code> resource.

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
INSERT INTO azure.network.web_application_firewall_policies (
policyName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ policyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: policySettings
          value:
            - name: state
              value: string
            - name: mode
              value: string
            - name: requestBodyCheck
              value: boolean
            - name: requestBodyInspectLimitInKB
              value: integer
            - name: requestBodyEnforcement
              value: boolean
            - name: maxRequestBodySizeInKb
              value: integer
            - name: fileUploadEnforcement
              value: boolean
            - name: fileUploadLimitInMb
              value: integer
            - name: customBlockResponseStatusCode
              value: integer
            - name: customBlockResponseBody
              value: string
            - name: logScrubbing
              value:
                - name: state
                  value: string
                - name: scrubbingRules
                  value:
                    - - name: matchVariable
                        value: string
                      - name: selectorMatchOperator
                        value: string
                      - name: selector
                        value: string
                      - name: state
                        value: string
            - name: jsChallengeCookieExpirationInMins
              value: integer
        - name: customRules
          value:
            - - name: name
                value: string
              - name: etag
                value: string
              - name: priority
                value: integer
              - name: state
                value: string
              - name: rateLimitDuration
                value: string
              - name: rateLimitThreshold
                value: integer
              - name: ruleType
                value: string
              - name: matchConditions
                value:
                  - - name: matchVariables
                      value:
                        - - name: variableName
                            value: string
                          - name: selector
                            value: string
                    - name: operator
                      value: string
                    - name: negationConditon
                      value: boolean
                    - name: matchValues
                      value:
                        - string
                    - name: transforms
                      value:
                        - []
              - name: groupByUserSession
                value:
                  - - name: groupByVariables
                      value:
                        - - name: variableName
                            value: string
              - name: action
                value: string
        - name: applicationGateways
          value:
            - - name: properties
                value:
                  - name: sku
                    value:
                      - name: name
                        value: string
                      - name: tier
                        value: string
                      - name: capacity
                        value: integer
                      - name: family
                        value: string
                  - name: sslPolicy
                    value:
                      - name: disabledSslProtocols
                        value:
                          - []
                      - name: policyType
                        value: string
                      - name: policyName
                        value: []
                      - name: cipherSuites
                        value:
                          - []
                      - name: minProtocolVersion
                        value: []
                  - name: operationalState
                    value: string
                  - name: gatewayIPConfigurations
                    value:
                      - - name: properties
                          value:
                            - name: subnet
                              value:
                                - name: id
                                  value: string
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
                  - name: authenticationCertificates
                    value:
                      - - name: properties
                          value:
                            - name: data
                              value: string
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: trustedRootCertificates
                    value:
                      - - name: properties
                          value:
                            - name: data
                              value: string
                            - name: keyVaultSecretId
                              value: string
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: trustedClientCertificates
                    value:
                      - - name: properties
                          value:
                            - name: data
                              value: string
                            - name: validatedCertData
                              value: string
                            - name: clientCertIssuerDN
                              value: string
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: sslCertificates
                    value:
                      - - name: properties
                          value:
                            - name: data
                              value: string
                            - name: password
                              value: string
                            - name: publicCertData
                              value: string
                            - name: keyVaultSecretId
                              value: string
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: frontendIPConfigurations
                    value:
                      - - name: properties
                          value:
                            - name: privateIPAddress
                              value: string
                            - name: privateIPAllocationMethod
                              value: []
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: frontendPorts
                    value:
                      - - name: properties
                          value:
                            - name: port
                              value: integer
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
                            - name: protocol
                              value: []
                            - name: host
                              value: string
                            - name: path
                              value: string
                            - name: interval
                              value: integer
                            - name: timeout
                              value: integer
                            - name: unhealthyThreshold
                              value: integer
                            - name: pickHostNameFromBackendHttpSettings
                              value: boolean
                            - name: pickHostNameFromBackendSettings
                              value: boolean
                            - name: minServers
                              value: integer
                            - name: match
                              value:
                                - name: body
                                  value: string
                                - name: statusCodes
                                  value:
                                    - string
                            - name: port
                              value: integer
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: backendAddressPools
                    value:
                      - - name: properties
                          value:
                            - name: backendIPConfigurations
                              value:
                                - - name: properties
                                    value:
                                      - name: virtualNetworkTaps
                                        value:
                                          - - name: properties
                                              value:
                                                - name: networkInterfaceTapConfigurations
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
                                                - name: resourceGuid
                                                  value: string
                                                - name: destinationNetworkInterfaceIPConfiguration
                                                  value:
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
                                                      value: []
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
                                          - - name: name
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
                                                        value: []
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
                                                  - - name: name
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
                  - name: backendHttpSettingsCollection
                    value:
                      - - name: properties
                          value:
                            - name: port
                              value: integer
                            - name: cookieBasedAffinity
                              value: string
                            - name: requestTimeout
                              value: integer
                            - name: authenticationCertificates
                              value:
                                - - name: id
                                    value: string
                            - name: trustedRootCertificates
                              value:
                                - - name: id
                                    value: string
                            - name: connectionDraining
                              value:
                                - name: enabled
                                  value: boolean
                                - name: drainTimeoutInSec
                                  value: integer
                            - name: hostName
                              value: string
                            - name: pickHostNameFromBackendAddress
                              value: boolean
                            - name: affinityCookieName
                              value: string
                            - name: probeEnabled
                              value: boolean
                            - name: path
                              value: string
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: backendSettingsCollection
                    value:
                      - - name: properties
                          value:
                            - name: port
                              value: integer
                            - name: timeout
                              value: integer
                            - name: trustedRootCertificates
                              value:
                                - - name: id
                                    value: string
                            - name: hostName
                              value: string
                            - name: pickHostNameFromBackendAddress
                              value: boolean
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: httpListeners
                    value:
                      - - name: properties
                          value:
                            - name: hostName
                              value: string
                            - name: requireServerNameIndication
                              value: boolean
                            - name: customErrorConfigurations
                              value:
                                - - name: statusCode
                                    value: string
                                  - name: customErrorPageUrl
                                    value: string
                            - name: hostNames
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
                  - name: listeners
                    value:
                      - - name: properties
                          value:
                            - name: hostNames
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
                  - name: sslProfiles
                    value:
                      - - name: properties
                          value:
                            - name: trustedClientCertificates
                              value:
                                - - name: id
                                    value: string
                            - name: clientAuthConfiguration
                              value:
                                - name: verifyClientCertIssuerDN
                                  value: boolean
                                - name: verifyClientRevocation
                                  value: string
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: urlPathMaps
                    value:
                      - - name: properties
                          value:
                            - name: pathRules
                              value:
                                - - name: properties
                                    value:
                                      - name: paths
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
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: requestRoutingRules
                    value:
                      - - name: properties
                          value:
                            - name: ruleType
                              value: string
                            - name: priority
                              value: integer
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: routingRules
                    value:
                      - - name: properties
                          value:
                            - name: ruleType
                              value: string
                            - name: priority
                              value: integer
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: rewriteRuleSets
                    value:
                      - - name: properties
                          value:
                            - name: rewriteRules
                              value:
                                - - name: name
                                    value: string
                                  - name: ruleSequence
                                    value: integer
                                  - name: conditions
                                    value:
                                      - - name: variable
                                          value: string
                                        - name: pattern
                                          value: string
                                        - name: ignoreCase
                                          value: boolean
                                        - name: negate
                                          value: boolean
                                  - name: actionSet
                                    value:
                                      - name: requestHeaderConfigurations
                                        value:
                                          - - name: headerName
                                              value: string
                                            - name: headerValueMatcher
                                              value:
                                                - name: pattern
                                                  value: string
                                                - name: ignoreCase
                                                  value: boolean
                                                - name: negate
                                                  value: boolean
                                            - name: headerValue
                                              value: string
                                      - name: responseHeaderConfigurations
                                        value:
                                          - - name: headerName
                                              value: string
                                            - name: headerValue
                                              value: string
                                      - name: urlConfiguration
                                        value:
                                          - name: modifiedPath
                                            value: string
                                          - name: modifiedQueryString
                                            value: string
                                          - name: reroute
                                            value: boolean
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: id
                          value: string
                  - name: redirectConfigurations
                    value:
                      - - name: properties
                          value:
                            - name: redirectType
                              value: []
                            - name: targetUrl
                              value: string
                            - name: includePath
                              value: boolean
                            - name: includeQueryString
                              value: boolean
                            - name: requestRoutingRules
                              value:
                                - - name: id
                                    value: string
                            - name: urlPathMaps
                              value:
                                - - name: id
                                    value: string
                            - name: pathRules
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
                  - name: webApplicationFirewallConfiguration
                    value:
                      - name: enabled
                        value: boolean
                      - name: firewallMode
                        value: string
                      - name: ruleSetType
                        value: string
                      - name: ruleSetVersion
                        value: string
                      - name: disabledRuleGroups
                        value:
                          - - name: ruleGroupName
                              value: string
                            - name: rules
                              value:
                                - integer
                      - name: requestBodyCheck
                        value: boolean
                      - name: maxRequestBodySize
                        value: integer
                      - name: maxRequestBodySizeInKb
                        value: integer
                      - name: fileUploadLimitInMb
                        value: integer
                      - name: exclusions
                        value:
                          - - name: matchVariable
                              value: string
                            - name: selectorMatchOperator
                              value: string
                            - name: selector
                              value: string
                  - name: enableHttp2
                    value: boolean
                  - name: enableFips
                    value: boolean
                  - name: autoscaleConfiguration
                    value:
                      - name: minCapacity
                        value: integer
                      - name: maxCapacity
                        value: integer
                  - name: privateLinkConfigurations
                    value:
                      - - name: properties
                          value:
                            - name: ipConfigurations
                              value:
                                - - name: properties
                                    value:
                                      - name: privateIPAddress
                                        value: string
                                      - name: primary
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
                        - name: id
                          value: string
                  - name: privateEndpointConnections
                    value:
                      - - name: properties
                          value:
                            - name: privateEndpoint
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
                            - name: privateLinkServiceConnectionState
                              value:
                                - name: status
                                  value: string
                                - name: description
                                  value: string
                                - name: actionsRequired
                                  value: string
                            - name: linkIdentifier
                              value: string
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
                  - name: customErrorConfigurations
                    value:
                      - - name: statusCode
                          value: string
                        - name: customErrorPageUrl
                          value: string
                  - name: forceFirewallPolicyAssociation
                    value: boolean
                  - name: loadDistributionPolicies
                    value:
                      - - name: properties
                          value:
                            - name: loadDistributionTargets
                              value:
                                - - name: properties
                                    value:
                                      - name: weightPerServer
                                        value: integer
                                  - name: name
                                    value: string
                                  - name: etag
                                    value: string
                                  - name: type
                                    value: string
                                  - name: id
                                    value: string
                            - name: loadDistributionAlgorithm
                              value: []
                        - name: name
                          value: string
                        - name: etag
                          value: string
                        - name: type
                          value: string
                        - name: id
                          value: string
                  - name: globalConfiguration
                    value:
                      - name: enableRequestBuffering
                        value: boolean
                      - name: enableResponseBuffering
                        value: boolean
              - name: etag
                value: string
              - name: zones
                value:
                  - string
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
        - name: resourceState
          value: string
        - name: managedRules
          value:
            - name: exceptions
              value:
                - - name: matchVariable
                    value: string
                  - name: values
                    value:
                      - string
                  - name: valueMatchOperator
                    value: string
                  - name: selectorMatchOperator
                    value: string
                  - name: selector
                    value: string
                  - name: exceptionManagedRuleSets
                    value:
                      - - name: ruleSetType
                          value: string
                        - name: ruleSetVersion
                          value: string
                        - name: ruleGroups
                          value:
                            - - name: ruleGroupName
                                value: string
                              - name: rules
                                value:
                                  - - name: ruleId
                                      value: string
            - name: exclusions
              value:
                - - name: matchVariable
                    value: string
                  - name: selectorMatchOperator
                    value: string
                  - name: selector
                    value: string
                  - name: exclusionManagedRuleSets
                    value:
                      - - name: ruleSetType
                          value: string
                        - name: ruleSetVersion
                          value: string
                        - name: ruleGroups
                          value:
                            - - name: ruleGroupName
                                value: string
                              - name: rules
                                value:
                                  - - name: ruleId
                                      value: string
            - name: managedRuleSets
              value:
                - - name: ruleSetType
                    value: string
                  - name: ruleSetVersion
                    value: string
                  - name: ruleGroupOverrides
                    value:
                      - - name: ruleGroupName
                          value: string
                        - name: rules
                          value:
                            - - name: ruleId
                                value: string
                              - name: state
                                value: string
                              - name: action
                                value: []
                              - name: sensitivity
                                value: []
        - name: httpListeners
          value:
            - - name: id
                value: string
        - name: pathBasedRules
          value:
            - - name: id
                value: string
        - name: applicationGatewayForContainers
          value:
            - - name: id
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

Deletes the specified <code>web_application_firewall_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.web_application_firewall_policies
WHERE policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
