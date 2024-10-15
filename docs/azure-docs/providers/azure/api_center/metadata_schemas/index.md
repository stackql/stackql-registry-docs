---
title: metadata_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_schemas
  - api_center
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

Creates, updates, deletes, gets or lists a <code>metadata_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.metadata_schemas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_metadata_schemas', value: 'view', },
        { label: 'metadata_schemas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assigned_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadataSchemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Metadata schema properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="metadataSchemaName, resourceGroupName, serviceName, subscriptionId" /> | Returns details of the metadata schema. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Returns a collection of metadata schemas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="metadataSchemaName, resourceGroupName, serviceName, subscriptionId" /> | Creates new or updates existing metadata schema. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="metadataSchemaName, resourceGroupName, serviceName, subscriptionId" /> | Deletes specified metadata schema. |

## `SELECT` examples

Returns a collection of metadata schemas.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_metadata_schemas', value: 'view', },
        { label: 'metadata_schemas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
assigned_to,
metadataSchemaName,
resourceGroupName,
schema,
serviceName,
subscriptionId
FROM azure.api_center.vw_metadata_schemas
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_center.metadata_schemas
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metadata_schemas</code> resource.

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
INSERT INTO azure.api_center.metadata_schemas (
metadataSchemaName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ metadataSchemaName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: schema
          value: string
        - name: assignedTo
          value:
            - - name: entity
                value: []
              - name: required
                value: boolean
              - name: deprecated
                value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>metadata_schemas</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_center.metadata_schemas
WHERE metadataSchemaName = '{{ metadataSchemaName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
