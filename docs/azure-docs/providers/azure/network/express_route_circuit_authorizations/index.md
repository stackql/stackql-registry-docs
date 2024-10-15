---
title: express_route_circuit_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_authorizations
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

Creates, updates, deletes, gets or lists a <code>express_route_circuit_authorizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_circuit_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuit_authorizations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_circuit_authorizations', value: 'view', },
        { label: 'express_route_circuit_authorizations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="authorizationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorization_use_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuitName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_resource_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of ExpressRouteCircuitAuthorization. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationName, circuitName, resourceGroupName, subscriptionId" /> | Gets the specified authorization from the specified express route circuit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="circuitName, resourceGroupName, subscriptionId" /> | Gets all authorizations in an express route circuit. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationName, circuitName, resourceGroupName, subscriptionId" /> | Creates or updates an authorization in the specified express route circuit. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationName, circuitName, resourceGroupName, subscriptionId" /> | Deletes the specified authorization from the specified express route circuit. |

## `SELECT` examples

Gets all authorizations in an express route circuit.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_circuit_authorizations', value: 'view', },
        { label: 'express_route_circuit_authorizations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
authorizationName,
authorization_key,
authorization_use_status,
circuitName,
connection_resource_uri,
etag,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.network.vw_express_route_circuit_authorizations
WHERE circuitName = '{{ circuitName }}'
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
FROM azure.network.express_route_circuit_authorizations
WHERE circuitName = '{{ circuitName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>express_route_circuit_authorizations</code> resource.

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
INSERT INTO azure.network.express_route_circuit_authorizations (
authorizationName,
circuitName,
resourceGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ authorizationName }}',
'{{ circuitName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: authorizationKey
          value: string
        - name: authorizationUseStatus
          value: string
        - name: connectionResourceUri
          value: string
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>express_route_circuit_authorizations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.express_route_circuit_authorizations
WHERE authorizationName = '{{ authorizationName }}'
AND circuitName = '{{ circuitName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
