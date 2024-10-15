---
title: sql_role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_role_definitions
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

Creates, updates, deletes, gets or lists a <code>sql_role_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_role_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.sql_role_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_role_definitions', value: 'view', },
        { label: 'sql_role_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `text` | The name of the database account. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignable_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="permissions" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Azure Cosmos DB SQL Role Definition resource object. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, roleDefinitionId, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB SQL Role Definition with the given Id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves the list of all Azure Cosmos DB SQL Role Definitions. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, roleDefinitionId, subscriptionId" /> | Creates or updates an Azure Cosmos DB SQL Role Definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, roleDefinitionId, subscriptionId" /> | Deletes an existing Azure Cosmos DB SQL Role Definition. |

## `SELECT` examples

Retrieves the list of all Azure Cosmos DB SQL Role Definitions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_role_definitions', value: 'view', },
        { label: 'sql_role_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
assignable_scopes,
permissions,
resourceGroupName,
roleDefinitionId,
role_name,
subscriptionId,
type
FROM azure.cosmos_db.vw_sql_role_definitions
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
FROM azure.cosmos_db.sql_role_definitions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_role_definitions</code> resource.

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
INSERT INTO azure.cosmos_db.sql_role_definitions (
accountName,
resourceGroupName,
roleDefinitionId,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ roleDefinitionId }}',
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
        - name: roleName
          value: string
        - name: type
          value: string
        - name: assignableScopes
          value:
            - string
        - name: permissions
          value:
            - - name: dataActions
                value:
                  - string
              - name: notDataActions
                value:
                  - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sql_role_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.sql_role_definitions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND roleDefinitionId = '{{ roleDefinitionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
