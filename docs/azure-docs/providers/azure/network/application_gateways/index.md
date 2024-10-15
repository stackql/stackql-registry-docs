---
title: application_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways
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

Creates, updates, deletes, gets or lists a <code>application_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateways', value: 'view', },
        { label: 'application_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="applicationGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="authentication_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="autoscale_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_address_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_http_settings_collection" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_settings_collection" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_error_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_predefined_ssl_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_fips" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_http2" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="firewall_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="force_firewall_policy_association" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend_ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend_ports" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="global_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_listeners" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="listeners" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_distribution_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="operational_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="probes" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="redirect_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_routing_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="rewrite_rule_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssl_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssl_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssl_profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="trusted_client_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="trusted_root_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="url_path_maps" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_application_firewall_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting where the resource needs to come from. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the application gateway. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Gets the specified application gateway. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all application gateways in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the application gateways in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Creates or updates the specified application gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Deletes the specified application gateway. |
| <CopyableCode code="backend_health" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Gets the backend health of the specified application gateway in a resource group. |
| <CopyableCode code="backend_health_on_demand" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Gets the backend health for given combination of backend pool and http setting of the specified application gateway in a resource group. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Starts the specified application gateway. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Stops the specified application gateway in a resource group. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Updates the specified application gateway tags. |

## `SELECT` examples

Gets all the application gateways in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateways', value: 'view', },
        { label: 'application_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applicationGatewayName,
authentication_certificates,
autoscale_configuration,
backend_address_pools,
backend_http_settings_collection,
backend_settings_collection,
custom_error_configurations,
default_predefined_ssl_policy,
enable_fips,
enable_http2,
etag,
firewall_policy,
force_firewall_policy_association,
frontend_ip_configurations,
frontend_ports,
gateway_ip_configurations,
global_configuration,
http_listeners,
identity,
listeners,
load_distribution_policies,
location,
operational_state,
private_endpoint_connections,
private_link_configurations,
probes,
provisioning_state,
redirect_configurations,
request_routing_rules,
resourceGroupName,
resource_guid,
rewrite_rule_sets,
routing_rules,
sku,
ssl_certificates,
ssl_policy,
ssl_profiles,
subscriptionId,
tags,
trusted_client_certificates,
trusted_root_certificates,
type,
url_path_maps,
web_application_firewall_configuration,
zones
FROM azure.network.vw_application_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
location,
properties,
tags,
type,
zones
FROM azure.network.application_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_gateways</code> resource.

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
INSERT INTO azure.network.application_gateways (
applicationGatewayName,
resourceGroupName,
subscriptionId,
properties,
zones,
identity,
id,
location,
tags
)
SELECT 
'{{ applicationGatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ zones }}',
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
                                              - name: privateIPAddressVersion
                                                value: []
                                              - name: subnet
                                                value:
                                                  - name: properties
                                                    value: []
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
                                                  - name: extendedLocation
                                                    value: []
                                                  - name: sku
                                                    value: []
                                                  - name: properties
                                                    value: []
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
                      - name: properties
                        value:
                          - name: networkInterfaces
                            value:
                              - - name: properties
                                  value:
                                    - name: networkSecurityGroup
                                      value:
                                        - name: properties
                                          value:
                                            - name: flushConnection
                                              value: boolean
                                            - name: securityRules
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
                                                    value: []
                                                  - name: etag
                                                    value: string
                                                  - name: identity
                                                    value: []
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
                                    - name: ipConfigurations
                                      value:
                                        - - name: name
                                            value: string
                                          - name: etag
                                            value: string
                                          - name: type
                                            value: string
                                          - name: id
                                            value: string
                                    - name: tapConfigurations
                                      value:
                                        - - name: name
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
                                          value:
                                            - name: loadBalancerFrontendIpConfigurations
                                              value:
                                                - - name: name
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
                                            - name: destinationIPAddress
                                              value: string
                                            - name: networkInterfaces
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
                                            - name: privateEndpointConnections
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
                                            - name: visibility
                                              value: string
                                            - name: autoApproval
                                              value: string
                                            - name: fqdns
                                              value:
                                                - string
                                            - name: alias
                                              value: string
                                            - name: enableProxyProtocol
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
                          - name: privateLinkServiceConnections
                            value:
                              - - name: properties
                                  value:
                                    - name: privateLinkServiceId
                                      value: string
                                    - name: groupIds
                                      value:
                                        - string
                                    - name: requestMessage
                                      value: string
                                    - name: privateLinkServiceConnectionState
                                      value:
                                        - name: status
                                          value: string
                                        - name: description
                                          value: string
                                        - name: actionsRequired
                                          value: string
                                - name: name
                                  value: string
                                - name: type
                                  value: string
                                - name: etag
                                  value: string
                                - name: id
                                  value: string
                          - name: manualPrivateLinkServiceConnections
                            value:
                              - - name: name
                                  value: string
                                - name: type
                                  value: string
                                - name: etag
                                  value: string
                                - name: id
                                  value: string
                          - name: customDnsConfigs
                            value:
                              - - name: fqdn
                                  value: string
                                - name: ipAddresses
                                  value:
                                    - string
                          - name: applicationSecurityGroups
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
                              - - name: properties
                                  value:
                                    - name: groupId
                                      value: string
                                    - name: memberName
                                      value: string
                                    - name: privateIPAddress
                                      value: string
                                - name: name
                                  value: string
                                - name: type
                                  value: string
                                - name: etag
                                  value: string
                          - name: customNetworkInterfaceName
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

Deletes the specified <code>application_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.application_gateways
WHERE applicationGatewayName = '{{ applicationGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
