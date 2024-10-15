---
title: managed_instance_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_private_endpoint_connections
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instance_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instance_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_private_endpoint_connections', value: 'view', },
        { label: 'managed_instance_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Properties of a private endpoint connection. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets a private endpoint connection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Approve or reject a private endpoint connection with a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes a private endpoint connection with a given name. |

## `SELECT` examples

Gets a private endpoint connection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_private_endpoint_connections', value: 'view', },
        { label: 'managed_instance_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
managedInstanceName,
privateEndpointConnectionName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.sql.vw_managed_instance_private_endpoint_connections
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_instance_private_endpoint_connections
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_instance_private_endpoint_connections</code> resource.

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
INSERT INTO azure.sql.managed_instance_private_endpoint_connections (
managedInstanceName,
privateEndpointConnectionName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ managedInstanceName }}',
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

## `DELETE` example

Deletes the specified <code>managed_instance_private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.managed_instance_private_endpoint_connections
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
