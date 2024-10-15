---
title: application_gateway_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateway_private_endpoint_connections
  - network
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

Creates, updates, deletes, gets or lists a <code>application_gateway_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateway_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateway_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateway_private_endpoint_connections', value: 'view', },
        { label: 'application_gateway_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of the private endpoint connection on an application gateway. |
| <CopyableCode code="applicationGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="link_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the private endpoint connection on an application gateway. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of Private Link Resource of an application gateway. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationGatewayName, connectionName, resourceGroupName, subscriptionId" /> | Gets the specified private endpoint connection on application gateway. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Lists all private endpoint connections on an application gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationGatewayName, connectionName, resourceGroupName, subscriptionId" /> | Deletes the specified private endpoint connection on application gateway. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="applicationGatewayName, connectionName, resourceGroupName, subscriptionId" /> | Updates the specified private endpoint connection on application gateway. |

## `SELECT` examples

Lists all private endpoint connections on an application gateway.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateway_private_endpoint_connections', value: 'view', },
        { label: 'application_gateway_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applicationGatewayName,
connectionName,
etag,
link_identifier,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.network.vw_application_gateway_private_endpoint_connections
WHERE applicationGatewayName = '{{ applicationGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.application_gateway_private_endpoint_connections
WHERE applicationGatewayName = '{{ applicationGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>application_gateway_private_endpoint_connections</code> resource.

```sql
/*+ update */
REPLACE azure.network.application_gateway_private_endpoint_connections
SET 
properties = '{{ properties }}',
name = '{{ name }}',
id = '{{ id }}'
WHERE 
applicationGatewayName = '{{ applicationGatewayName }}'
AND connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>application_gateway_private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.application_gateway_private_endpoint_connections
WHERE applicationGatewayName = '{{ applicationGatewayName }}'
AND connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
