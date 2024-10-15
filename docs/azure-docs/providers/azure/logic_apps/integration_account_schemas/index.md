---
title: integration_account_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_schemas
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_account_schemas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_account_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_account_schemas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_schemas', value: 'view', },
        { label: 'integration_account_schemas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="document_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="target_namespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration account schema properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, schemaName, subscriptionId" /> | Gets an integration account schema. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Gets a list of integration account schemas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="integrationAccountName, resourceGroupName, schemaName, subscriptionId, data__properties" /> | Creates or updates an integration account schema. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationAccountName, resourceGroupName, schemaName, subscriptionId" /> | Deletes an integration account schema. |

## `SELECT` examples

Gets a list of integration account schemas.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_schemas', value: 'view', },
        { label: 'integration_account_schemas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
changed_time,
content,
content_link,
content_type,
created_time,
document_name,
file_name,
integrationAccountName,
location,
metadata,
resourceGroupName,
schemaName,
schema_type,
subscriptionId,
tags,
target_namespace,
type
FROM azure.logic_apps.vw_integration_account_schemas
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.logic_apps.integration_account_schemas
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_account_schemas</code> resource.

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
INSERT INTO azure.logic_apps.integration_account_schemas (
integrationAccountName,
resourceGroupName,
schemaName,
subscriptionId,
data__properties,
properties,
location,
tags
)
SELECT 
'{{ integrationAccountName }}',
'{{ resourceGroupName }}',
'{{ schemaName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: schemaType
          value: []
        - name: targetNamespace
          value: string
        - name: documentName
          value: string
        - name: fileName
          value: string
        - name: createdTime
          value: string
        - name: changedTime
          value: string
        - name: metadata
          value: []
        - name: content
          value: string
        - name: contentType
          value: string
        - name: contentLink
          value:
            - name: uri
              value: string
            - name: contentVersion
              value: string
            - name: contentSize
              value: integer
            - name: contentHash
              value:
                - name: algorithm
                  value: string
                - name: value
                  value: string
            - name: metadata
              value: []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>integration_account_schemas</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_account_schemas
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND schemaName = '{{ schemaName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
