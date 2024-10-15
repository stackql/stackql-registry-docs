---
title: gremlin_database_throughputs
hide_title: false
hide_table_of_contents: false
keywords:
  - gremlin_database_throughputs
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

Creates, updates, deletes, gets or lists a <code>gremlin_database_throughputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gremlin_database_throughputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.gremlin_database_throughputs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gremlin_database_throughputs', value: 'view', },
        { label: 'gremlin_database_throughputs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `text` | The name of the ARM resource. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="location" /> | `text` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | The properties of an Azure Cosmos DB resource throughput |
| <CopyableCode code="tags" /> | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Gets the RUs per second of the Gremlin database under an existing Azure Cosmos DB database account with the provided name. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Update RUs per second of an Azure Cosmos DB Gremlin database |

## `SELECT` examples

Gets the RUs per second of the Gremlin database under an existing Azure Cosmos DB database account with the provided name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gremlin_database_throughputs', value: 'view', },
        { label: 'gremlin_database_throughputs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
databaseName,
identity,
location,
resource,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.cosmos_db.vw_gremlin_database_throughputs
WHERE accountName = '{{ accountName }}'
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
FROM azure.cosmos_db.gremlin_database_throughputs
WHERE accountName = '{{ accountName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>gremlin_database_throughputs</code> resource.

```sql
/*+ update */
REPLACE azure.cosmos_db.gremlin_database_throughputs
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
accountName = '{{ accountName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}';
```
