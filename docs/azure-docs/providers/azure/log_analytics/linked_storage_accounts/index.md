---
title: linked_storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_storage_accounts
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

Creates, updates, deletes, gets or lists a <code>linked_storage_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>linked_storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.linked_storage_accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linked_storage_accounts', value: 'view', },
        { label: 'linked_storage_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataSourceType" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Linked storage accounts properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataSourceType, resourceGroupName, subscriptionId, workspaceName" /> | Gets all linked storage account of a specific data source type associated with the specified workspace. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all linked storage accounts associated with the specified workspace, storage accounts will be sorted by their data source type. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataSourceType, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Create or Update a link relation between current workspace and a group of storage accounts of a specific data source type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataSourceType, resourceGroupName, subscriptionId, workspaceName" /> | Deletes all linked storage accounts of a specific data source type associated with the specified workspace. |

## `SELECT` examples

Gets all linked storage accounts associated with the specified workspace, storage accounts will be sorted by their data source type.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linked_storage_accounts', value: 'view', },
        { label: 'linked_storage_accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dataSourceType,
data_source_type,
resourceGroupName,
storage_account_ids,
subscriptionId,
workspaceName
FROM azure.log_analytics.vw_linked_storage_accounts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.log_analytics.linked_storage_accounts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>linked_storage_accounts</code> resource.

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
INSERT INTO azure.log_analytics.linked_storage_accounts (
dataSourceType,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ dataSourceType }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
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
        - name: dataSourceType
          value: string
        - name: storageAccountIds
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>linked_storage_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.linked_storage_accounts
WHERE dataSourceType = '{{ dataSourceType }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
