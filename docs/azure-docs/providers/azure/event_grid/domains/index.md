---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_domains', value: 'view', },
        { label: 'domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_create_topic_with_first_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_delete_topic_with_last_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_residency_boundary" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_type_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The identity information for the resource. |
| <CopyableCode code="inbound_ip_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="input_schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="input_schema_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="metric_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimum_tls_version_allowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes an EventGrid Resource Sku. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The identity information for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the Event Grid Domain Resource. |
| <CopyableCode code="sku" /> | `object` | Describes an EventGrid Resource Sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Get properties of a domain. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the domains under a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the domains under an Azure subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Asynchronously creates or updates a new domain with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Delete existing domain. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Asynchronously updates a domain with the specified parameters. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId, data__keyName" /> | Regenerate a shared access key for a domain. |

## `SELECT` examples

List all the domains under an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_domains', value: 'view', },
        { label: 'domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_create_topic_with_first_subscription,
auto_delete_topic_with_last_subscription,
data_residency_boundary,
disable_local_auth,
domainName,
endpoint,
event_type_info,
identity,
inbound_ip_rules,
input_schema,
input_schema_mapping,
location,
metric_resource_id,
minimum_tls_version_allowed,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sku,
subscriptionId,
system_data,
tags
FROM azure.event_grid.vw_domains
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
FROM azure.event_grid.domains
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domains</code> resource.

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
INSERT INTO azure.event_grid.domains (
domainName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
sku,
identity
)
SELECT 
'{{ domainName }}',
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
        - name: minimumTlsVersionAllowed
          value: string
        - name: endpoint
          value: string
        - name: inputSchema
          value: string
        - name: eventTypeInfo
          value:
            - name: kind
              value: string
            - name: inlineEventTypes
              value: object
        - name: inputSchemaMapping
          value:
            - name: inputSchemaMappingType
              value: string
        - name: metricResourceId
          value: string
        - name: publicNetworkAccess
          value: string
        - name: inboundIpRules
          value:
            - - name: ipMask
                value: string
              - name: action
                value: string
        - name: disableLocalAuth
          value: boolean
        - name: autoCreateTopicWithFirstSubscription
          value: boolean
        - name: autoDeleteTopicWithLastSubscription
          value: boolean
        - name: dataResidencyBoundary
          value: string
    - name: sku
      value:
        - name: name
          value: string
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

Updates a <code>domains</code> resource.

```sql
/*+ update */
UPDATE azure.event_grid.domains
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}'
WHERE 
domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.domains
WHERE domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
