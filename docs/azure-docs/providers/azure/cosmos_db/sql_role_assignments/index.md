---
title: sql_role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_role_assignments
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

Creates, updates, deletes, gets or lists a <code>sql_role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.sql_role_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_role_assignments', value: 'view', },
        { label: 'sql_role_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `text` | The name of the database account. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleAssignmentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Azure Cosmos DB SQL Role Assignment resource object. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, roleAssignmentId, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB SQL Role Assignment with the given Id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves the list of all Azure Cosmos DB SQL Role Assignments. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, roleAssignmentId, subscriptionId" /> | Creates or updates an Azure Cosmos DB SQL Role Assignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, roleAssignmentId, subscriptionId" /> | Deletes an existing Azure Cosmos DB SQL Role Assignment. |

## `SELECT` examples

Retrieves the list of all Azure Cosmos DB SQL Role Assignments.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_role_assignments', value: 'view', },
        { label: 'sql_role_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
principal_id,
resourceGroupName,
roleAssignmentId,
role_definition_id,
scope,
subscriptionId,
type
FROM azure.cosmos_db.vw_sql_role_assignments
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
FROM azure.cosmos_db.sql_role_assignments
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_role_assignments</code> resource.

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
INSERT INTO azure.cosmos_db.sql_role_assignments (
accountName,
resourceGroupName,
roleAssignmentId,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ roleAssignmentId }}',
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
        - name: roleDefinitionId
          value: string
        - name: scope
          value: string
        - name: principalId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sql_role_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.sql_role_assignments
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND roleAssignmentId = '{{ roleAssignmentId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
