---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - search
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auth_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="disabled_data_exfiltration_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_with_cmk" /> | `text` | field from the `properties` object |
| <CopyableCode code="hosting_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Details about the search service identity. A null value indicates that the search service has no identity assigned. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="network_rule_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="partition_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="replica_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="searchServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="semantic_search" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_private_link_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Defines the SKU of a search service, which determines billing rate and capacity limits. |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Details about the search service identity. A null value indicates that the search service has no identity assigned. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the search service. |
| <CopyableCode code="sku" /> | `object` | Defines the SKU of a search service, which determines billing rate and capacity limits. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Gets the search service with the given name in the given resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of all Search services in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all Search services in the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Creates or updates a search service in the given resource group. If the search service already exists, all properties will be updated with the given values. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Deletes a search service in the given resource group, along with its associated resources. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Updates an existing search service in the given resource group. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks whether or not the given search service name is available for use. Search service names must be globally unique since they are part of the service URI (https://name.search.windows.net). |

## `SELECT` examples

Gets a list of all Search services in the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auth_options,
disable_local_auth,
disabled_data_exfiltration_options,
e_tag,
encryption_with_cmk,
hosting_mode,
identity,
location,
network_rule_set,
partition_count,
private_endpoint_connections,
provisioning_state,
public_network_access,
replica_count,
resourceGroupName,
searchServiceName,
semantic_search,
shared_private_link_resources,
sku,
status,
status_details,
subscriptionId,
tags
FROM azure.search.vw_services
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
FROM azure.search.services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO azure.search.services (
resourceGroupName,
searchServiceName,
subscriptionId,
properties,
sku,
identity,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ searchServiceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}',
'{{ identity }}',
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
        - name: replicaCount
          value: integer
        - name: partitionCount
          value: integer
        - name: hostingMode
          value: string
        - name: publicNetworkAccess
          value: string
        - name: status
          value: string
        - name: statusDetails
          value: string
        - name: provisioningState
          value: string
        - name: networkRuleSet
          value:
            - name: ipRules
              value:
                - - name: value
                    value: string
            - name: bypass
              value: string
        - name: disabledDataExfiltrationOptions
          value:
            - []
        - name: encryptionWithCmk
          value:
            - name: enforcement
              value: string
            - name: encryptionComplianceStatus
              value: string
        - name: disableLocalAuth
          value: boolean
        - name: authOptions
          value:
            - name: apiKeyOnly
              value: []
            - name: aadOrApiKey
              value:
                - name: aadAuthFailureMode
                  value: string
        - name: semanticSearch
          value: []
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: privateEndpoint
                    value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: groupId
                    value: string
                  - name: provisioningState
                    value: string
              - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
        - name: sharedPrivateLinkResources
          value:
            - - name: properties
                value:
                  - name: privateLinkResourceId
                    value: string
                  - name: groupId
                    value: string
                  - name: requestMessage
                    value: string
                  - name: resourceRegion
                    value: string
                  - name: status
                    value: string
                  - name: provisioningState
                    value: string
              - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
        - name: eTag
          value: string
    - name: sku
      value:
        - name: name
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
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure.search.services
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.search.services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
