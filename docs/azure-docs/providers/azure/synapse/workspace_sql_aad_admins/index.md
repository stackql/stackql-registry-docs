---
title: workspace_sql_aad_admins
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_sql_aad_admins
  - synapse
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

Creates, updates, deletes, gets or lists a <code>workspace_sql_aad_admins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_sql_aad_admins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspace_sql_aad_admins" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_sql_aad_admins', value: 'view', },
        { label: 'workspace_sql_aad_admins', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrator_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="login" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Workspace active directory administrator properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets a workspace SQL active directory admin |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a workspace SQL active directory admin |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Deletes a workspace SQL active directory admin |

## `SELECT` examples

Gets a workspace SQL active directory admin

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_sql_aad_admins', value: 'view', },
        { label: 'workspace_sql_aad_admins', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrator_type,
login,
resourceGroupName,
sid,
subscriptionId,
tenant_id,
workspaceName
FROM azure.synapse.vw_workspace_sql_aad_admins
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.workspace_sql_aad_admins
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_sql_aad_admins</code> resource.

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
INSERT INTO azure.synapse.workspace_sql_aad_admins (
resourceGroupName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
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
        - name: tenantId
          value: string
        - name: login
          value: string
        - name: administratorType
          value: string
        - name: sid
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workspace_sql_aad_admins</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.workspace_sql_aad_admins
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
