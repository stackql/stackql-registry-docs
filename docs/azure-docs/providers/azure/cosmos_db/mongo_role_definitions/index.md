---
title: mongo_role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_role_definitions
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

Creates, updates, deletes, gets or lists a <code>mongo_role_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mongo_role_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.mongo_role_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mongo_role_definitions', value: 'view', },
        { label: 'mongo_role_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `text` | The name of the database account. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="mongoRoleDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="privileges" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="roles" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Azure Cosmos DB Mongo Role Definition resource object. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB Mongo Role Definition with the given Id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves the list of all Azure Cosmos DB Mongo Role Definitions. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId" /> | Creates or updates an Azure Cosmos DB Mongo Role Definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId" /> | Deletes an existing Azure Cosmos DB Mongo Role Definition. |

## `SELECT` examples

Retrieves the list of all Azure Cosmos DB Mongo Role Definitions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mongo_role_definitions', value: 'view', },
        { label: 'mongo_role_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
database_name,
mongoRoleDefinitionId,
privileges,
resourceGroupName,
role_name,
roles,
subscriptionId,
type
FROM azure.cosmos_db.vw_mongo_role_definitions
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
FROM azure.cosmos_db.mongo_role_definitions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mongo_role_definitions</code> resource.

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
INSERT INTO azure.cosmos_db.mongo_role_definitions (
accountName,
mongoRoleDefinitionId,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ mongoRoleDefinitionId }}',
'{{ resourceGroupName }}',
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
        - name: databaseName
          value: string
        - name: privileges
          value:
            - - name: resource
                value:
                  - name: db
                    value: string
                  - name: collection
                    value: string
              - name: actions
                value:
                  - string
        - name: roles
          value:
            - - name: db
                value: string
              - name: role
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>mongo_role_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.mongo_role_definitions
WHERE accountName = '{{ accountName }}'
AND mongoRoleDefinitionId = '{{ mongoRoleDefinitionId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
