---
title: saved_searches
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_searches
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

Creates, updates, deletes, gets or lists a <code>saved_searches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saved_searches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.saved_searches" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_saved_searches', value: 'view', },
        { label: 'saved_searches', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag |
| <CopyableCode code="function_alias" /> | `text` | field from the `properties` object |
| <CopyableCode code="function_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="query" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="savedSearchId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag |
| <CopyableCode code="properties" /> | `object` | Value object for saved search results. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, savedSearchId, subscriptionId, workspaceName" /> | Gets the specified saved search for a given workspace. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the saved searches for a given Log Analytics Workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, savedSearchId, subscriptionId, workspaceName, data__properties" /> | Creates or updates a saved search for a given workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, savedSearchId, subscriptionId, workspaceName" /> | Deletes the specified saved search in a given workspace. |

## `SELECT` examples

Gets the saved searches for a given Log Analytics Workspace

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_saved_searches', value: 'view', },
        { label: 'saved_searches', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
category,
display_name,
etag,
function_alias,
function_parameters,
query,
resourceGroupName,
savedSearchId,
subscriptionId,
tags,
version,
workspaceName
FROM azure.log_analytics.vw_saved_searches
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.log_analytics.saved_searches
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>saved_searches</code> resource.

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
INSERT INTO azure.log_analytics.saved_searches (
resourceGroupName,
savedSearchId,
subscriptionId,
workspaceName,
data__properties,
etag,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ savedSearchId }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: category
          value: string
        - name: displayName
          value: string
        - name: query
          value: string
        - name: functionAlias
          value: string
        - name: functionParameters
          value: string
        - name: version
          value: integer
        - name: tags
          value:
            - - name: name
                value: string
              - name: value
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>saved_searches</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.saved_searches
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND savedSearchId = '{{ savedSearchId }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
