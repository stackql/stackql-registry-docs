---
title: mongo_user_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_user_definitions
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

Creates, updates, deletes, gets or lists a <code>mongo_user_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mongo_user_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.mongo_user_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mongo_user_definitions', value: 'view', },
        { label: 'mongo_user_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `text` | The name of the database account. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="mechanisms" /> | `text` | field from the `properties` object |
| <CopyableCode code="mongoUserDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="password" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="roles" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
| <CopyableCode code="user_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Azure Cosmos DB Mongo User Definition resource object. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB Mongo User Definition with the given Id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves the list of all Azure Cosmos DB Mongo User Definition. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId" /> | Creates or updates an Azure Cosmos DB Mongo User Definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, mongoUserDefinitionId, resourceGroupName, subscriptionId" /> | Deletes an existing Azure Cosmos DB Mongo User Definition. |

## `SELECT` examples

Retrieves the list of all Azure Cosmos DB Mongo User Definition.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mongo_user_definitions', value: 'view', },
        { label: 'mongo_user_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
custom_data,
database_name,
mechanisms,
mongoUserDefinitionId,
password,
resourceGroupName,
roles,
subscriptionId,
type,
user_name
FROM azure.cosmos_db.vw_mongo_user_definitions
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
FROM azure.cosmos_db.mongo_user_definitions
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mongo_user_definitions</code> resource.

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
INSERT INTO azure.cosmos_db.mongo_user_definitions (
accountName,
mongoUserDefinitionId,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ mongoUserDefinitionId }}',
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
        - name: userName
          value: string
        - name: password
          value: string
        - name: databaseName
          value: string
        - name: customData
          value: string
        - name: roles
          value:
            - - name: db
                value: string
              - name: role
                value: string
        - name: mechanisms
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>mongo_user_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.mongo_user_definitions
WHERE accountName = '{{ accountName }}'
AND mongoUserDefinitionId = '{{ mongoUserDefinitionId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
