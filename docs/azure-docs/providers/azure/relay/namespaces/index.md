---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - relay
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.relay.namespaces" /></td></tr>
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
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="metric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_bus_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU of the namespace. |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="updated_at" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the namespace. |
| <CopyableCode code="sku" /> | `object` | SKU of the namespace. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Returns the description for the specified namespace. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the available namespaces within the subscription regardless of the resourceGroups. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the available namespaces within the ResourceGroup. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Create Azure Relay namespace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Deletes an existing namespace. This operation also removes all associated resources under the namespace. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Check the specified namespace name availability. |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the primary or secondary connection strings to the namespace. |

## `SELECT` examples

Lists all the available namespaces within the subscription regardless of the resourceGroups.

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
created_at,
location,
metric_id,
namespaceName,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
service_bus_endpoint,
sku,
status,
subscriptionId,
system_data,
tags,
updated_at
FROM azure.relay.vw_namespaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
systemData,
tags
FROM azure.relay.namespaces
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
INSERT INTO azure.relay.namespaces (
namespaceName,
resourceGroupName,
subscriptionId,
sku,
properties,
location,
tags
)
SELECT 
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ sku }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
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
        - name: provisioningState
          value: string
        - name: status
          value: string
        - name: createdAt
          value: string
        - name: updatedAt
          value: string
        - name: serviceBusEndpoint
          value: string
        - name: metricId
          value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: location
                value: string
              - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                  - name: provisioningState
                    value: string
        - name: publicNetworkAccess
          value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>namespaces</code> resource.

```sql
/*+ update */
UPDATE azure.relay.namespaces
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>namespaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.relay.namespaces
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
