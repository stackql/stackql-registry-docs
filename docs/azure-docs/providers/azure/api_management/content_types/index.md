---
title: content_types
hide_title: false
hide_table_of_contents: false
keywords:
  - content_types
  - api_management
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

Creates, updates, deletes, gets or lists a <code>content_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>content_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.content_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_content_types', value: 'view', },
        { label: 'content_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="contentTypeId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the developer portal's content type. Content types describe content items' properties, validation rules, and constraints. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists the developer portal's content types. Content types describe content items' properties, validation rules, and constraints. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates the developer portal's content type. Content types describe content items' properties, validation rules, and constraints. Custom content types' identifiers need to start with the `c-` prefix. Built-in content types can't be modified. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Removes the specified developer portal's content type. Content types describe content items' properties, validation rules, and constraints. Built-in content types (with identifiers starting with the `c-` prefix) can't be removed. |

## `SELECT` examples

Lists the developer portal's content types. Content types describe content items' properties, validation rules, and constraints.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_content_types', value: 'view', },
        { label: 'content_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
contentTypeId,
resourceGroupName,
schema,
serviceName,
subscriptionId,
version
FROM azure.api_management.vw_content_types
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.content_types
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>content_types</code> resource.

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
INSERT INTO azure.api_management.content_types (
contentTypeId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ contentTypeId }}',
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
        - name: id
          value: string
        - name: name
          value: string
        - name: description
          value: string
        - name: schema
          value: object
        - name: version
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>content_types</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.content_types
WHERE If-Match = '{{ If-Match }}'
AND contentTypeId = '{{ contentTypeId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
