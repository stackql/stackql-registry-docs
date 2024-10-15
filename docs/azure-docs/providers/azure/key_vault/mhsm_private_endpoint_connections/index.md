---
title: mhsm_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - mhsm_private_endpoint_connections
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>mhsm_private_endpoint_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mhsm_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.mhsm_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mhsm_private_endpoint_connections', value: 'view', },
        { label: 'mhsm_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| <CopyableCode code="name" /> | `text` | The name of the managed HSM Pool. |
| <CopyableCode code="etag" /> | `text` | Modified whenever there is a change in the state of private endpoint connection. |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The supported Azure location where the managed HSM Pool should be created. |
| <CopyableCode code="privateEndpointConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU details |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | The resource type of the managed HSM Pool. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| <CopyableCode code="name" /> | `string` | The name of the managed HSM Pool. |
| <CopyableCode code="etag" /> | `string` | Modified whenever there is a change in the state of private endpoint connection. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The supported Azure location where the managed HSM Pool should be created. |
| <CopyableCode code="properties" /> | `object` | Properties of the private endpoint connection resource. |
| <CopyableCode code="sku" /> | `object` | SKU details |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | The resource type of the managed HSM Pool. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets the specified private endpoint connection associated with the managed HSM Pool. |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | The List operation gets information about the private endpoint connections associated with the managed HSM Pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes the specified private endpoint connection associated with the managed hsm pool. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Updates the specified private endpoint connection associated with the managed hsm pool. |

## `SELECT` examples

The List operation gets information about the private endpoint connections associated with the managed HSM Pool.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mhsm_private_endpoint_connections', value: 'view', },
        { label: 'mhsm_private_endpoint_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
identity,
location,
privateEndpointConnectionName,
private_endpoint,
private_link_service_connection_state,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
system_data,
tags,
type
FROM azure.key_vault.vw_mhsm_private_endpoint_connections
WHERE name = '{{ name }}'
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
identity,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.key_vault.mhsm_private_endpoint_connections
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>mhsm_private_endpoint_connections</code> resource.

```sql
/*+ update */
REPLACE azure.key_vault.mhsm_private_endpoint_connections
SET 
properties = '{{ properties }}',
etag = '{{ etag }}',
location = '{{ location }}',
sku = '{{ sku }}',
tags = '{{ tags }}',
systemData = '{{ systemData }}',
identity = '{{ identity }}'
WHERE 
name = '{{ name }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>mhsm_private_endpoint_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.key_vault.mhsm_private_endpoint_connections
WHERE name = '{{ name }}'
AND privateEndpointConnectionName = '{{ privateEndpointConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
