---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - healthdataaiservices
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.healthdataaiservices.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoint_connections', value: 'view', },
        { label: 'private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deidServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateEndpointConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the private endpoint connection. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deidServiceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Get a specific private connection |
| <CopyableCode code="list_by_deid_service" /> | `SELECT` | <CopyableCode code="deidServiceName, resourceGroupName, subscriptionId" /> | List private endpoint connections on the given resource |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deidServiceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Create a Private endpoint connection |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deidServiceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Delete the private endpoint connection |

## `SELECT` examples

List private endpoint connections on the given resource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoint_connections', value: 'view', },
        { label: 'private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
deidServiceName,
group_ids,
privateEndpointConnectionName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.healthdataaiservices.vw_private_endpoint_connections
WHERE deidServiceName = '{{ deidServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.healthdataaiservices.private_endpoint_connections
WHERE deidServiceName = '{{ deidServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_endpoint_connections</code> resource.

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
INSERT INTO azure.healthdataaiservices.private_endpoint_connections (
deidServiceName,
privateEndpointConnectionName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ deidServiceName }}',
'{{ privateEndpointConnectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: groupIds
          value:
            - string
        - name: privateEndpoint
          value:
            - name: id
              value: string
        - name: privateLinkServiceConnectionState
          value:
            - name: status
              value: []
            - name: description
              value: string
            - name: actionsRequired
              value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.healthdataaiservices.private_endpoint_connections
WHERE deidServiceName = '{{ deidServiceName }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
