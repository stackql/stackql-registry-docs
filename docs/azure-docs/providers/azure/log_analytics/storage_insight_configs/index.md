---
title: storage_insight_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_insight_configs
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

Creates, updates, deletes, gets or lists a <code>storage_insight_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_insight_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.storage_insight_configs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_insight_configs', value: 'view', },
        { label: 'storage_insight_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="containers" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageInsightName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tables" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | The ETag of the storage insight. |
| <CopyableCode code="properties" /> | `object` | Storage insight properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageInsightName, subscriptionId, workspaceName" /> | Gets a storage insight instance. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists the storage insight instances within a workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, storageInsightName, subscriptionId, workspaceName" /> | Create or update a storage insight. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, storageInsightName, subscriptionId, workspaceName" /> | Deletes a storageInsightsConfigs resource |

## `SELECT` examples

Lists the storage insight instances within a workspace

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_insight_configs', value: 'view', },
        { label: 'storage_insight_configs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
containers,
e_tag,
resourceGroupName,
status,
storageInsightName,
storage_account,
subscriptionId,
tables,
tags,
workspaceName
FROM azure.log_analytics.vw_storage_insight_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
properties,
tags
FROM azure.log_analytics.storage_insight_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_insight_configs</code> resource.

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
INSERT INTO azure.log_analytics.storage_insight_configs (
resourceGroupName,
storageInsightName,
subscriptionId,
workspaceName,
properties,
eTag,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ storageInsightName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}',
'{{ eTag }}',
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
        - name: containers
          value:
            - string
        - name: tables
          value:
            - string
        - name: storageAccount
          value:
            - name: id
              value: string
            - name: key
              value: string
        - name: status
          value:
            - name: state
              value: string
            - name: description
              value: string
    - name: eTag
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>storage_insight_configs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.storage_insight_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageInsightName = '{{ storageInsightName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
