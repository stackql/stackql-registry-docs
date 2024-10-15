---
title: sql_stored_procedures
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_stored_procedures
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

Creates, updates, deletes, gets or lists a <code>sql_stored_procedures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_stored_procedures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.sql_stored_procedures" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_stored_procedures', value: 'view', },
        { label: 'sql_stored_procedures', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `text` | The name of the ARM resource. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="containerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="location" /> | `text` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storedProcedureName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="properties" /> | `object` | The properties of an Azure Cosmos DB StoredProcedure |
| <CopyableCode code="tags" /> | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, storedProcedureName, subscriptionId" /> | Gets the SQL storedProcedure under an existing Azure Cosmos DB database account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, subscriptionId" /> | Lists the SQL storedProcedure under an existing Azure Cosmos DB database account. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, storedProcedureName, subscriptionId, data__properties" /> | Create or update an Azure Cosmos DB SQL storedProcedure |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, storedProcedureName, subscriptionId" /> | Deletes an existing Azure Cosmos DB SQL storedProcedure. |

## `SELECT` examples

Lists the SQL storedProcedure under an existing Azure Cosmos DB database account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_stored_procedures', value: 'view', },
        { label: 'sql_stored_procedures', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
containerName,
databaseName,
identity,
location,
resource,
resourceGroupName,
storedProcedureName,
subscriptionId,
tags,
type
FROM azure.cosmos_db.vw_sql_stored_procedures
WHERE accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
tags,
type
FROM azure.cosmos_db.sql_stored_procedures
WHERE accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_stored_procedures</code> resource.

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
INSERT INTO azure.cosmos_db.sql_stored_procedures (
accountName,
containerName,
databaseName,
resourceGroupName,
storedProcedureName,
subscriptionId,
data__properties,
properties,
location,
tags,
identity
)
SELECT 
'{{ accountName }}',
'{{ containerName }}',
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ storedProcedureName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: resource
          value:
            - name: id
              value: string
            - name: body
              value: string
        - name: options
          value:
            - name: throughput
              value: integer
            - name: autoscaleSettings
              value:
                - name: maxThroughput
                  value: integer
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sql_stored_procedures</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.sql_stored_procedures
WHERE accountName = '{{ accountName }}'
AND containerName = '{{ containerName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storedProcedureName = '{{ storedProcedureName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
