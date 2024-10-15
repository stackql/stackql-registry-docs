---
title: workbook_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - workbook_templates
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>workbook_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workbook_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.workbook_templates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workbook_templates', value: 'view', },
        { label: 'workbook_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name. |
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleries" /> | `text` | field from the `properties` object |
| <CopyableCode code="localized" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="template_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties that contain a workbook template. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get a single workbook template by its resourceName. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all Workbook templates defined within a specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a new workbook template. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Delete a workbook template. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a workbook template that has already been added. |

## `SELECT` examples

Get all Workbook templates defined within a specified resource group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workbook_templates', value: 'view', },
        { label: 'workbook_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
author,
galleries,
localized,
location,
priority,
resourceGroupName,
resourceName,
subscriptionId,
tags,
template_data,
type
FROM azure.application_insights.vw_workbook_templates
WHERE resourceGroupName = '{{ resourceGroupName }}'
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
FROM azure.application_insights.workbook_templates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workbook_templates</code> resource.

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
INSERT INTO azure.application_insights.workbook_templates (
resourceGroupName,
resourceName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: properties
      value:
        - name: priority
          value: integer
        - name: author
          value: string
        - name: templateData
          value: object
        - name: galleries
          value:
            - - name: name
                value: string
              - name: category
                value: string
              - name: type
                value: string
              - name: order
                value: integer
              - name: resourceType
                value: string
        - name: localized
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workbook_templates</code> resource.

```sql
/*+ update */
UPDATE azure.application_insights.workbook_templates
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>workbook_templates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.workbook_templates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
