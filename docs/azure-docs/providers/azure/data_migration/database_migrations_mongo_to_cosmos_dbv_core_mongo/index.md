---
title: database_migrations_mongo_to_cosmos_dbv_core_mongo
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_mongo_to_cosmos_dbv_core_mongo
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>database_migrations_mongo_to_cosmos_dbv_core_mongo</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_migrations_mongo_to_cosmos_dbv_core_mongo</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.database_migrations_mongo_to_cosmos_dbv_core_mongo" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_migrations_mongo_to_cosmos_dbv_core_mongo', value: 'view', },
        { label: 'database_migrations_mongo_to_cosmos_dbv_core_mongo', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="collection_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="ended_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="migrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_failure_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_operation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_service" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_mongo_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="started_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="targetResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_mongo_connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Database Migration Resource properties for CosmosDb for Mongo. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetResourceName" /> | Get Database Migration resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetResourceName" /> | Create or Update Database Migration resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetResourceName" /> | Delete Database Migration resource. |

## `SELECT` examples

Get Database Migration resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_migrations_mongo_to_cosmos_dbv_core_mongo', value: 'view', },
        { label: 'database_migrations_mongo_to_cosmos_dbv_core_mongo', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
collection_list,
ended_on,
kind,
migrationName,
migration_failure_error,
migration_operation_id,
migration_service,
migration_status,
provisioning_error,
provisioning_state,
resourceGroupName,
scope,
source_mongo_connection,
started_on,
subscriptionId,
system_data,
targetResourceName,
target_mongo_connection,
type
FROM azure.data_migration.vw_database_migrations_mongo_to_cosmos_dbv_core_mongo
WHERE migrationName = '{{ migrationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetResourceName = '{{ targetResourceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_migration.database_migrations_mongo_to_cosmos_dbv_core_mongo
WHERE migrationName = '{{ migrationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetResourceName = '{{ targetResourceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>database_migrations_mongo_to_cosmos_dbv_core_mongo</code> resource.

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
INSERT INTO azure.data_migration.database_migrations_mongo_to_cosmos_dbv_core_mongo (
migrationName,
resourceGroupName,
subscriptionId,
targetResourceName,
properties
)
SELECT 
'{{ migrationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ targetResourceName }}',
'{{ properties }}'
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
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: kind
          value: string
        - name: scope
          value: string
        - name: provisioningState
          value: string
        - name: migrationStatus
          value: string
        - name: startedOn
          value: string
        - name: endedOn
          value: string
        - name: migrationService
          value: string
        - name: migrationOperationId
          value: string
        - name: migrationFailureError
          value:
            - name: code
              value: string
            - name: message
              value: string
        - name: provisioningError
          value: string
        - name: sourceMongoConnection
          value:
            - name: host
              value: string
            - name: port
              value: integer
            - name: userName
              value: string
            - name: password
              value: string
            - name: useSsl
              value: boolean
            - name: connectionString
              value: string
        - name: collectionList
          value:
            - - name: sourceDatabase
                value: string
              - name: sourceCollection
                value: string
              - name: targetDatabase
                value: string
              - name: targetCollection
                value: string
              - name: migrationProgressDetails
                value:
                  - name: migrationStatus
                    value: string
                  - name: migrationError
                    value: string
                  - name: sourceDocumentCount
                    value: integer
                  - name: processedDocumentCount
                    value: integer
                  - name: durationInSeconds
                    value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>database_migrations_mongo_to_cosmos_dbv_core_mongo</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_migration.database_migrations_mongo_to_cosmos_dbv_core_mongo
WHERE migrationName = '{{ migrationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetResourceName = '{{ targetResourceName }}';
```
