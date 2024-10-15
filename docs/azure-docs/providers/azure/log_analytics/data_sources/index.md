---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>data_sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.data_sources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_sources', value: 'view', },
        { label: 'data_sources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="$filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataSourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag of the data source. |
| <CopyableCode code="kind" /> | `text` | The kind of the DataSource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag of the data source. |
| <CopyableCode code="kind" /> | `string` | The kind of the DataSource. |
| <CopyableCode code="properties" /> | `object` | JSON object |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataSourceName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a datasource instance. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="$filter, resourceGroupName, subscriptionId, workspaceName" /> | Gets the first page of data source instances in a workspace with the link to the next page. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataSourceName, resourceGroupName, subscriptionId, workspaceName, data__kind, data__properties" /> | Create or update a data source. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataSourceName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a data source instance. |

## `SELECT` examples

Gets the first page of data source instances in a workspace with the link to the next page.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_sources', value: 'view', },
        { label: 'data_sources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
$filter,
dataSourceName,
etag,
kind,
resourceGroupName,
subscriptionId,
tags,
workspaceName
FROM azure.log_analytics.vw_data_sources
WHERE $filter = '{{ $filter }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
kind,
properties,
tags
FROM azure.log_analytics.data_sources
WHERE $filter = '{{ $filter }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_sources</code> resource.

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
INSERT INTO azure.log_analytics.data_sources (
dataSourceName,
resourceGroupName,
subscriptionId,
workspaceName,
data__kind,
data__properties,
properties,
etag,
kind,
tags
)
SELECT 
'{{ dataSourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__kind }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ etag }}',
'{{ kind }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: []
    - name: etag
      value: string
    - name: kind
      value: []
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_sources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.data_sources
WHERE dataSourceName = '{{ dataSourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
