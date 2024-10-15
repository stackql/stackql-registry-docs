---
title: notebook_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_workspaces
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>notebook_workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebook_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.notebook_workspaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_notebook_workspaces', value: 'view', },
        { label: 'notebook_workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `text` | The name of the database account. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="notebookWorkspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="notebook_server_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Properties of a notebook workspace resource. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Gets the notebook workspace for a Cosmos DB account. |
| <CopyableCode code="list_by_database_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the notebook workspace resources of an existing Cosmos DB account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Creates the notebook workspace for a Cosmos DB account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Deletes the notebook workspace for a Cosmos DB account. |
| <CopyableCode code="regenerate_auth_token" /> | `EXEC` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Regenerates the auth token for the notebook workspace |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Starts the notebook workspace |

## `SELECT` examples

Gets the notebook workspace resources of an existing Cosmos DB account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_notebook_workspaces', value: 'view', },
        { label: 'notebook_workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
notebookWorkspaceName,
notebook_server_endpoint,
resourceGroupName,
status,
subscriptionId,
type
FROM azure.cosmos_db.vw_notebook_workspaces
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.cosmos_db.notebook_workspaces
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notebook_workspaces</code> resource.

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
INSERT INTO azure.cosmos_db.notebook_workspaces (
accountName,
notebookWorkspaceName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ accountName }}',
'{{ notebookWorkspaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}'
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notebook_workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.notebook_workspaces
WHERE accountName = '{{ accountName }}'
AND notebookWorkspaceName = '{{ notebookWorkspaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
