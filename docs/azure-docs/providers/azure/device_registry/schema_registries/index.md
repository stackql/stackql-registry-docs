---
title: schema_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_registries
  - device_registry
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

Creates, updates, deletes, gets or lists a <code>schema_registries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.schema_registries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_schema_registries', value: 'view', },
        { label: 'schema_registries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="namespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaRegistryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_container_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the schema registry properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaRegistryName, subscriptionId" /> | Get a SchemaRegistry |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List SchemaRegistry resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List SchemaRegistry resources by subscription ID |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="resourceGroupName, schemaRegistryName, subscriptionId" /> | Create a SchemaRegistry |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, schemaRegistryName, subscriptionId" /> | Delete a SchemaRegistry |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, schemaRegistryName, subscriptionId" /> | Update a SchemaRegistry |

## `SELECT` examples

List SchemaRegistry resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_schema_registries', value: 'view', },
        { label: 'schema_registries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
display_name,
identity,
location,
namespace,
provisioning_state,
resourceGroupName,
schemaRegistryName,
storage_account_container_url,
subscriptionId,
tags,
uuid
FROM azure.device_registry.vw_schema_registries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.device_registry.schema_registries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schema_registries</code> resource.

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
INSERT INTO azure.device_registry.schema_registries (
resourceGroupName,
schemaRegistryName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ schemaRegistryName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: uuid
          value: string
        - name: namespace
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: storageAccountContainerUrl
          value: string
        - name: provisioningState
          value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>schema_registries</code> resource.

```sql
/*+ update */
UPDATE azure.device_registry.schema_registries
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND schemaRegistryName = '{{ schemaRegistryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>schema_registries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.device_registry.schema_registries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaRegistryName = '{{ schemaRegistryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
