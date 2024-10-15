---
title: cassandra_views
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_views
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

Creates, updates, deletes, gets or lists a <code>cassandra_views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cassandra_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.cassandra_views" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cassandra_views', value: 'view', },
        { label: 'cassandra_views', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `text` | The name of the ARM resource. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="keyspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="options" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
| <CopyableCode code="viewName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="properties" /> | `object` | The properties of an Azure Cosmos DB Cassandra view |
| <CopyableCode code="tags" /> | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId, viewName" /> | Gets the Cassandra view under an existing Azure Cosmos DB database account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId" /> | Lists the Cassandra materialized views under an existing Azure Cosmos DB database account. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId, viewName, data__properties" /> | Create or update an Azure Cosmos DB Cassandra View |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId, viewName" /> | Deletes an existing Azure Cosmos DB Cassandra view. |

## `SELECT` examples

Lists the Cassandra materialized views under an existing Azure Cosmos DB database account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cassandra_views', value: 'view', },
        { label: 'cassandra_views', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
identity,
keyspaceName,
location,
options,
resource,
resourceGroupName,
subscriptionId,
tags,
type,
viewName
FROM azure.cosmos_db.vw_cassandra_views
WHERE accountName = '{{ accountName }}'
AND keyspaceName = '{{ keyspaceName }}'
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
FROM azure.cosmos_db.cassandra_views
WHERE accountName = '{{ accountName }}'
AND keyspaceName = '{{ keyspaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cassandra_views</code> resource.

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
INSERT INTO azure.cosmos_db.cassandra_views (
accountName,
keyspaceName,
resourceGroupName,
subscriptionId,
viewName,
data__properties,
properties,
location,
tags,
identity
)
SELECT 
'{{ accountName }}',
'{{ keyspaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ viewName }}',
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
            - name: viewDefinition
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

Deletes the specified <code>cassandra_views</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cosmos_db.cassandra_views
WHERE accountName = '{{ accountName }}'
AND keyspaceName = '{{ keyspaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND viewName = '{{ viewName }}';
```
