---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - web_pubsub
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.private_endpoint_connections" /></td></tr>
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
| <CopyableCode code="group_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateEndpointConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Private endpoint connection properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Get the specified private endpoint connection |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List private endpoint connections |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Delete the specified private endpoint connection |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Update the state of specified private endpoint connection |

## `SELECT` examples

List private endpoint connections

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
group_ids,
privateEndpointConnectionName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
resourceName,
subscriptionId
FROM azure.web_pubsub.vw_private_endpoint_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.web_pubsub.private_endpoint_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>private_endpoint_connections</code> resource.

```sql
/*+ update */
REPLACE azure.web_pubsub.private_endpoint_connections
SET 
properties = '{{ properties }}'
WHERE 
privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.web_pubsub.private_endpoint_connections
WHERE privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
