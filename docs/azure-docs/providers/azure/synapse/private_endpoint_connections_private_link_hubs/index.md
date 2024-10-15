---
title: private_endpoint_connections_private_link_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections_private_link_hubs
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connections_private_link_hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoint_connections_private_link_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.private_endpoint_connections_private_link_hubs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoint_connections_private_link_hubs', value: 'view', },
        { label: 'private_endpoint_connections_private_link_hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | identifier |
| <CopyableCode code="privateEndpointConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateLinkHubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | identifier |
| <CopyableCode code="properties" /> | `object` | Properties of a private endpoint connection. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateEndpointConnectionName, privateLinkHubName, resourceGroupName, subscriptionId" /> | Get all PrivateEndpointConnection in the PrivateLinkHub by name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateLinkHubName, resourceGroupName, subscriptionId" /> | Get all PrivateEndpointConnections in the PrivateLinkHub |

## `SELECT` examples

Get all PrivateEndpointConnections in the PrivateLinkHub

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoint_connections_private_link_hubs', value: 'view', },
        { label: 'private_endpoint_connections_private_link_hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
privateEndpointConnectionName,
privateLinkHubName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.synapse.vw_private_endpoint_connections_private_link_hubs
WHERE privateLinkHubName = '{{ privateLinkHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
properties
FROM azure.synapse.private_endpoint_connections_private_link_hubs
WHERE privateLinkHubName = '{{ privateLinkHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

