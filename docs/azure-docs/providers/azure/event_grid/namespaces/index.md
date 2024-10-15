---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.namespaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_namespaces', value: 'view', },
        { label: 'namespaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `text` | The identity information for the resource. |
| <CopyableCode code="inbound_ip_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_zone_redundant" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="minimum_tls_version_allowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Represents available Sku pricing tiers. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="topic_spaces_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="topics_configuration" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The identity information for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the namespace resource. |
| <CopyableCode code="sku" /> | `object` | Represents available Sku pricing tiers. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Get properties of a namespace. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the namespaces under a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the namespaces under an Azure subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Asynchronously creates or updates a new namespace with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Delete existing namespace. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Asynchronously updates a namespace with the specified parameters. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, data__keyName" /> | Regenerate a shared access key for a namespace. |
| <CopyableCode code="validate_custom_domain_ownership" /> | `EXEC` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Performs ownership validation via checking TXT records for all custom domains in a namespace. |

## `SELECT` examples

List all the namespaces under an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_namespaces', value: 'view', },
        { label: 'namespaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
identity,
inbound_ip_rules,
is_zone_redundant,
location,
minimum_tls_version_allowed,
namespaceName,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sku,
subscriptionId,
system_data,
tags,
topic_spaces_configuration,
topics_configuration
FROM azure.event_grid.vw_namespaces
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
systemData,
tags
FROM azure.event_grid.namespaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>namespaces</code> resource.

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
INSERT INTO azure.event_grid.namespaces (
namespaceName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
sku,
identity
)
SELECT 
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ sku }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: systemData
                value:
                  - name: createdBy
                    value: string
                  - name: createdByType
                    value: string
                  - name: createdAt
                    value: string
                  - name: lastModifiedBy
                    value: string
                  - name: lastModifiedByType
                    value: string
                  - name: lastModifiedAt
                    value: string
              - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: groupIds
                    value:
                      - string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: string
        - name: provisioningState
          value: string
        - name: topicsConfiguration
          value:
            - name: hostname
              value: string
            - name: customDomains
              value:
                - - name: fullyQualifiedDomainName
                    value: string
                  - name: validationState
                    value: string
                  - name: identity
                    value:
                      - name: type
                        value: string
                      - name: userAssignedIdentity
                        value: string
                  - name: certificateUrl
                    value: string
                  - name: expectedTxtRecordName
                    value: string
                  - name: expectedTxtRecordValue
                    value: string
        - name: topicSpacesConfiguration
          value:
            - name: state
              value: string
            - name: routeTopicResourceId
              value: string
            - name: hostname
              value: string
            - name: routingEnrichments
              value:
                - name: static
                  value:
                    - - name: key
                        value: string
                      - name: valueType
                        value: string
                - name: dynamic
                  value:
                    - - name: key
                        value: string
                      - name: value
                        value: string
            - name: clientAuthentication
              value:
                - name: alternativeAuthenticationNameSources
                  value:
                    - string
                - name: customJwtAuthentication
                  value:
                    - name: tokenIssuer
                      value: string
                    - name: issuerCertificates
                      value:
                        - - name: certificateUrl
                            value: string
                          - name: identity
                            value:
                              - name: type
                                value: string
                              - name: userAssignedIdentity
                                value: string
            - name: maximumSessionExpiryInHours
              value: integer
            - name: maximumClientSessionsPerAuthenticationName
              value: integer
            - name: routingIdentityInfo
              value:
                - name: type
                  value: string
                - name: userAssignedIdentity
                  value: string
            - name: customDomains
              value:
                - - name: fullyQualifiedDomainName
                    value: string
                  - name: validationState
                    value: string
                  - name: certificateUrl
                    value: string
                  - name: expectedTxtRecordName
                    value: string
                  - name: expectedTxtRecordValue
                    value: string
        - name: isZoneRedundant
          value: boolean
        - name: publicNetworkAccess
          value: string
        - name: inboundIpRules
          value:
            - - name: ipMask
                value: string
              - name: action
                value: string
        - name: minimumTlsVersionAllowed
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: capacity
          value: integer
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>namespaces</code> resource.

```sql
/*+ update */
UPDATE azure.event_grid.namespaces
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>namespaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.namespaces
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
