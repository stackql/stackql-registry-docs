---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
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

Creates, updates, deletes, gets or lists a <code>schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.schemas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_schemas', value: 'view', },
        { label: 'schemas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="format" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaRegistryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Defines the schema properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaName, schemaRegistryName, subscriptionId" /> | Get a Schema |
| <CopyableCode code="list_by_schema_registry" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaRegistryName, subscriptionId" /> | List Schema resources by SchemaRegistry |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="resourceGroupName, schemaName, schemaRegistryName, subscriptionId" /> | Create a Schema |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, schemaName, schemaRegistryName, subscriptionId" /> | Delete a Schema |

## `SELECT` examples

List Schema resources by SchemaRegistry

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_schemas', value: 'view', },
        { label: 'schemas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
display_name,
format,
provisioning_state,
resourceGroupName,
schemaName,
schemaRegistryName,
schema_type,
subscriptionId,
tags,
uuid
FROM azure.device_registry.vw_schemas
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaRegistryName = '{{ schemaRegistryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.device_registry.schemas
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaRegistryName = '{{ schemaRegistryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schemas</code> resource.

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
INSERT INTO azure.device_registry.schemas (
resourceGroupName,
schemaName,
schemaRegistryName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ schemaName }}',
'{{ schemaRegistryName }}',
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
        - name: uuid
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: format
          value: []
        - name: schemaType
          value: []
        - name: provisioningState
          value: []
        - name: tags
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>schemas</code> resource.

```sql
/*+ delete */
DELETE FROM azure.device_registry.schemas
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND schemaRegistryName = '{{ schemaRegistryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
