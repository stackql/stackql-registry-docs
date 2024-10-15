---
title: private_link_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_hubs
  - synapse
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

Creates, updates, deletes, gets or lists a <code>private_link_hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.private_link_hubs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_hubs', value: 'view', },
        { label: 'private_link_hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="privateLinkHubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | PrivateLinkHub properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateLinkHubName, resourceGroupName, subscriptionId" /> | Gets a privateLinkHub |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of privateLinkHubs in a subscription |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns a list of privateLinkHubs in a resource group |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateLinkHubName, resourceGroupName, subscriptionId" /> | Creates or updates a privateLinkHub |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateLinkHubName, resourceGroupName, subscriptionId" /> | Deletes a privateLinkHub |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="privateLinkHubName, resourceGroupName, subscriptionId" /> | Updates a privateLinkHub |

## `SELECT` examples

Returns a list of privateLinkHubs in a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_hubs', value: 'view', },
        { label: 'private_link_hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
privateLinkHubName,
private_endpoint_connections,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.synapse.vw_private_link_hubs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.synapse.private_link_hubs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_link_hubs</code> resource.

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
INSERT INTO azure.synapse.private_link_hubs (
privateLinkHubName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ privateLinkHubName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
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
        - name: provisioningState
          value: string
        - name: privateEndpointConnections
          value:
            - - name: id
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
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>private_link_hubs</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.private_link_hubs
SET 
tags = '{{ tags }}'
WHERE 
privateLinkHubName = '{{ privateLinkHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>private_link_hubs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.private_link_hubs
WHERE privateLinkHubName = '{{ privateLinkHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
