---
title: communications_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - communications_gateways
  - voice_services
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

Creates, updates, deletes, gets or lists a <code>communications_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>communications_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.voice_services.communications_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_communications_gateways', value: 'view', },
        { label: 'communications_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allocated_media_address_prefixes" /> | `text` | field from the `properties` object |
| <CopyableCode code="allocated_signaling_address_prefixes" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_bridge" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_generated_domain_name_label" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_generated_domain_name_label_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="codecs" /> | `text` | field from the `properties` object |
| <CopyableCode code="communicationsGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectivity" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_sip_headers" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_delegations" /> | `text` | field from the `properties` object |
| <CopyableCode code="e911_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="emergency_dial_strings" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="integrated_mcp_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="on_prem_mcp_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="platforms" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="teams_voicemail_pilot_number" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the CommunicationsGateway resource. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId" /> | Get a CommunicationsGateway |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List CommunicationsGateway resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List CommunicationsGateway resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId" /> | Create a CommunicationsGateway |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId" /> | Delete a CommunicationsGateway |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId" /> | Update a CommunicationsGateway |

## `SELECT` examples

List CommunicationsGateway resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_communications_gateways', value: 'view', },
        { label: 'communications_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allocated_media_address_prefixes,
allocated_signaling_address_prefixes,
api_bridge,
auto_generated_domain_name_label,
auto_generated_domain_name_label_scope,
codecs,
communicationsGatewayName,
connectivity,
custom_sip_headers,
dns_delegations,
e911_type,
emergency_dial_strings,
identity,
integrated_mcp_enabled,
location,
on_prem_mcp_enabled,
platforms,
provisioning_state,
resourceGroupName,
service_locations,
sku,
status,
subscriptionId,
tags,
teams_voicemail_pilot_number
FROM azure.voice_services.vw_communications_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
sku,
tags
FROM azure.voice_services.communications_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>communications_gateways</code> resource.

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
INSERT INTO azure.voice_services.communications_gateways (
communicationsGatewayName,
resourceGroupName,
subscriptionId,
properties,
identity,
sku,
tags,
location
)
SELECT 
'{{ communicationsGatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ sku }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: status
          value: []
        - name: serviceLocations
          value:
            - - name: name
                value: string
              - name: primaryRegionProperties
                value:
                  - name: operatorAddresses
                    value:
                      - string
                  - name: esrpAddresses
                    value:
                      - string
                  - name: allowedSignalingSourceAddressPrefixes
                    value:
                      - string
                  - name: allowedMediaSourceAddressPrefixes
                    value:
                      - string
        - name: connectivity
          value: []
        - name: codecs
          value:
            - []
        - name: e911Type
          value: []
        - name: platforms
          value:
            - []
        - name: apiBridge
          value:
            - name: configureApiBridge
              value: []
            - name: endpointFqdns
              value:
                - string
            - name: allowedAddressPrefixes
              value:
                - string
        - name: autoGeneratedDomainNameLabelScope
          value: []
        - name: autoGeneratedDomainNameLabel
          value: string
        - name: teamsVoicemailPilotNumber
          value: string
        - name: onPremMcpEnabled
          value: boolean
        - name: integratedMcpEnabled
          value: boolean
        - name: emergencyDialStrings
          value:
            - string
        - name: dnsDelegations
          value:
            - name: delegations
              value:
                - - name: domain
                    value: string
                  - name: nameServers
                    value:
                      - string
        - name: customSipHeaders
          value:
            - name: headers
              value:
                - - name: name
                    value: string
        - name: allocatedSignalingAddressPrefixes
          value:
            - string
        - name: allocatedMediaAddressPrefixes
          value:
            - string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>communications_gateways</code> resource.

```sql
/*+ update */
UPDATE azure.voice_services.communications_gateways
SET 
identity = '{{ identity }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
communicationsGatewayName = '{{ communicationsGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>communications_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.voice_services.communications_gateways
WHERE communicationsGatewayName = '{{ communicationsGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
