---
title: schema_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_versions
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

Creates, updates, deletes, gets or lists a <code>schema_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.schema_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_schema_versions', value: 'view', },
        { label: 'schema_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="hash" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaRegistryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Defines the schema version properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaName, schemaRegistryName, schemaVersionName, subscriptionId" /> | Get a SchemaVersion |
| <CopyableCode code="list_by_schema" /> | `SELECT` | <CopyableCode code="resourceGroupName, schemaName, schemaRegistryName, subscriptionId" /> | List SchemaVersion resources by Schema |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="resourceGroupName, schemaName, schemaRegistryName, schemaVersionName, subscriptionId" /> | Create a SchemaVersion |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, schemaName, schemaRegistryName, schemaVersionName, subscriptionId" /> | Delete a SchemaVersion |

## `SELECT` examples

List SchemaVersion resources by Schema

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_schema_versions', value: 'view', },
        { label: 'schema_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
hash,
provisioning_state,
resourceGroupName,
schemaName,
schemaRegistryName,
schemaVersionName,
schema_content,
subscriptionId,
uuid
FROM azure.device_registry.vw_schema_versions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND schemaRegistryName = '{{ schemaRegistryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.device_registry.schema_versions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND schemaRegistryName = '{{ schemaRegistryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schema_versions</code> resource.

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
INSERT INTO azure.device_registry.schema_versions (
resourceGroupName,
schemaName,
schemaRegistryName,
schemaVersionName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ schemaName }}',
'{{ schemaRegistryName }}',
'{{ schemaVersionName }}',
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
        - name: description
          value: string
        - name: schemaContent
          value: string
        - name: hash
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>schema_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.device_registry.schema_versions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND schemaRegistryName = '{{ schemaRegistryName }}'
AND schemaVersionName = '{{ schemaVersionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
