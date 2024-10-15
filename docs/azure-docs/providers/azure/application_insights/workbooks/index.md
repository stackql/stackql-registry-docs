---
title: workbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - workbooks
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

Creates, updates, deletes, gets or lists a <code>workbooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workbooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.workbooks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workbooks', value: 'view', },
        { label: 'workbooks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource etag |
| <CopyableCode code="identity" /> | `text` | Identity used for BYOS |
| <CopyableCode code="kind" /> | `text` | The kind of workbook. Only valid value is shared. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="revision" /> | `text` | field from the `properties` object |
| <CopyableCode code="serialized_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="identity" /> | `object` | Identity used for BYOS |
| <CopyableCode code="kind" /> | `string` | The kind of workbook. Only valid value is shared. |
| <CopyableCode code="properties" /> | `object` | Properties that contain a workbook. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get a single workbook by its resourceName. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all Workbooks defined within a specified resource group and category. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all Workbooks defined within a specified subscription and category. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a new workbook. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Delete a workbook. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a workbook that has already been added. |
| <CopyableCode code="revision_get" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, revisionId, subscriptionId" /> | Get a single workbook revision defined by its revisionId. |
| <CopyableCode code="revisions_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the revisions for the workbook defined by its resourceName. |

## `SELECT` examples

Get all Workbooks defined within a specified subscription and category.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workbooks', value: 'view', },
        { label: 'workbooks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
category,
display_name,
etag,
identity,
kind,
resourceGroupName,
resourceName,
revision,
serialized_data,
source_id,
storage_uri,
subscriptionId,
system_data,
tags,
time_modified,
user_id,
version
FROM azure.application_insights.vw_workbooks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
identity,
kind,
properties,
systemData
FROM azure.application_insights.workbooks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workbooks</code> resource.

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
INSERT INTO azure.application_insights.workbooks (
resourceGroupName,
resourceName,
subscriptionId,
identity,
kind,
etag,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ kind }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value: string
    - name: kind
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: displayName
          value: string
        - name: serializedData
          value: string
        - name: version
          value: string
        - name: timeModified
          value: string
        - name: category
          value: string
        - name: tags
          value:
            - string
        - name: userId
          value: string
        - name: sourceId
          value: string
        - name: storageUri
          value: string
        - name: description
          value: string
        - name: revision
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workbooks</code> resource.

```sql
/*+ update */
UPDATE azure.application_insights.workbooks
SET 
kind = '{{ kind }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>workbooks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.workbooks
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
