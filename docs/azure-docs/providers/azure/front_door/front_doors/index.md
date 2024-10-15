---
title: front_doors
hide_title: false
hide_table_of_contents: false
keywords:
  - front_doors
  - front_door
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

Creates, updates, deletes, gets or lists a <code>front_doors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>front_doors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.front_doors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_front_doors', value: 'view', },
        { label: 'front_doors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="backend_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_pools_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="cname" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontDoorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontdoor_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_probe_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancing_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="rules_engines" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create an endpoint. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Gets a Front Door with the specified Front Door name under the specified subscription and resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the Front Doors within an Azure subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the Front Doors within a resource group under a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Creates a new Front Door with a Front Door name under the specified subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Deletes an existing Front Door with the specified parameters. |
| <CopyableCode code="validate_custom_domain" /> | `EXEC` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId, data__hostName" /> | Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS. |

## `SELECT` examples

Lists all of the Front Doors within an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_front_doors', value: 'view', },
        { label: 'front_doors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backend_pools,
backend_pools_settings,
cname,
enabled_state,
extended_properties,
friendly_name,
frontDoorName,
frontdoor_id,
frontend_endpoints,
health_probe_settings,
load_balancing_settings,
location,
provisioning_state,
resourceGroupName,
resource_state,
routing_rules,
rules_engines,
subscriptionId,
tags,
type
FROM azure.front_door.vw_front_doors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.front_door.front_doors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>front_doors</code> resource.

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
INSERT INTO azure.front_door.front_doors (
frontDoorName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ frontDoorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: friendlyName
          value: string
        - name: routingRules
          value:
            - - name: properties
                value:
                  - name: frontendEndpoints
                    value:
                      - - name: id
                          value: string
                  - name: acceptedProtocols
                    value:
                      - string
                  - name: patternsToMatch
                    value:
                      - string
                  - name: enabledState
                    value: string
                  - name: routeConfiguration
                    value:
                      - name: '@odata.type'
                        value: string
                  - name: rulesEngine
                    value:
                      - name: id
                        value: string
                  - name: webApplicationFirewallPolicyLink
                    value:
                      - name: id
                        value: string
                  - name: resourceState
                    value: []
              - name: name
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: loadBalancingSettings
          value:
            - - name: properties
                value:
                  - name: sampleSize
                    value: integer
                  - name: successfulSamplesRequired
                    value: integer
                  - name: additionalLatencyMilliseconds
                    value: integer
              - name: name
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: healthProbeSettings
          value:
            - - name: properties
                value:
                  - name: path
                    value: string
                  - name: protocol
                    value: string
                  - name: intervalInSeconds
                    value: integer
                  - name: healthProbeMethod
                    value: string
                  - name: enabledState
                    value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: backendPools
          value:
            - - name: properties
                value:
                  - name: backends
                    value:
                      - - name: address
                          value: string
                        - name: privateLinkAlias
                          value: string
                        - name: privateLinkResourceId
                          value: string
                        - name: privateLinkLocation
                          value: string
                        - name: privateEndpointStatus
                          value: string
                        - name: privateLinkApprovalMessage
                          value: string
                        - name: httpPort
                          value: integer
                        - name: httpsPort
                          value: integer
                        - name: enabledState
                          value: string
                        - name: priority
                          value: integer
                        - name: weight
                          value: integer
                        - name: backendHostHeader
                          value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: frontendEndpoints
          value:
            - - name: properties
                value:
                  - name: hostName
                    value: string
                  - name: sessionAffinityEnabledState
                    value: string
                  - name: sessionAffinityTtlSeconds
                    value: integer
                  - name: webApplicationFirewallPolicyLink
                    value:
                      - name: id
                        value: string
                  - name: customHttpsProvisioningState
                    value: string
                  - name: customHttpsProvisioningSubstate
                    value: string
                  - name: customHttpsConfiguration
                    value:
                      - name: certificateSource
                        value: string
                      - name: protocolType
                        value: string
                      - name: minimumTlsVersion
                        value: string
                      - name: keyVaultCertificateSourceParameters
                        value:
                          - name: vault
                            value:
                              - name: id
                                value: string
                          - name: secretName
                            value: string
                          - name: secretVersion
                            value: string
                      - name: frontDoorCertificateSourceParameters
                        value:
                          - name: certificateType
                            value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: backendPoolsSettings
          value:
            - name: enforceCertificateNameCheck
              value: string
            - name: sendRecvTimeoutSeconds
              value: integer
        - name: enabledState
          value: string
        - name: provisioningState
          value: string
        - name: cname
          value: string
        - name: frontdoorId
          value: string
        - name: rulesEngines
          value:
            - - name: properties
                value:
                  - name: rules
                    value:
                      - - name: name
                          value: string
                        - name: priority
                          value: integer
                        - name: action
                          value:
                            - name: requestHeaderActions
                              value:
                                - - name: headerActionType
                                    value: string
                                  - name: headerName
                                    value: string
                                  - name: value
                                    value: string
                            - name: responseHeaderActions
                              value:
                                - - name: headerActionType
                                    value: string
                                  - name: headerName
                                    value: string
                                  - name: value
                                    value: string
                        - name: matchConditions
                          value:
                            - - name: rulesEngineMatchVariable
                                value: string
                              - name: selector
                                value: string
                              - name: rulesEngineOperator
                                value: string
                              - name: negateCondition
                                value: boolean
                              - name: rulesEngineMatchValue
                                value:
                                  - string
                              - name: transforms
                                value:
                                  - []
                        - name: matchProcessingBehavior
                          value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: extendedProperties
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

Deletes the specified <code>front_doors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.front_door.front_doors
WHERE frontDoorName = '{{ frontDoorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
