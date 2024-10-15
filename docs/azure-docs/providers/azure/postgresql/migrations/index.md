---
title: migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - migrations
  - postgresql
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

Creates, updates, deletes, gets or lists a <code>migrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.migrations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_migrations', value: 'view', },
        { label: 'migrations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cancel" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="dbs_to_cancel_migration_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="dbs_to_migrate" /> | `text` | field from the `properties` object |
| <CopyableCode code="dbs_to_trigger_cutover_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="migrate_roles" /> | `text` | field from the `properties` object |
| <CopyableCode code="migrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_instance_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_option" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_window_end_time_in_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_window_start_time_in_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="overwrite_dbs_in_target" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="setup_logical_replication_on_source_db_if_needed" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_db_server_fully_qualified_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_db_server_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_db_server_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssl_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_data_migration" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="targetDbServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_db_server_fully_qualified_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_db_server_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_db_server_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="trigger_cutover" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Migration resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetDbServerName" /> | Gets details of a migration. |
| <CopyableCode code="list_by_target_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, targetDbServerName" /> | List all the migrations on a given target server. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetDbServerName" /> | Creates a new migration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetDbServerName" /> | Deletes a migration. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetDbServerName" /> | Updates an existing migration. The request body can contain one to many of the mutable properties present in the migration definition. Certain property updates initiate migration state transitions. |

## `SELECT` examples

List all the migrations on a given target server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_migrations', value: 'view', },
        { label: 'migrations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cancel,
current_status,
dbs_to_cancel_migration_on,
dbs_to_migrate,
dbs_to_trigger_cutover_on,
location,
migrate_roles,
migrationName,
migration_id,
migration_instance_resource_id,
migration_mode,
migration_option,
migration_window_end_time_in_utc,
migration_window_start_time_in_utc,
overwrite_dbs_in_target,
resourceGroupName,
secret_parameters,
setup_logical_replication_on_source_db_if_needed,
source_db_server_fully_qualified_domain_name,
source_db_server_metadata,
source_db_server_resource_id,
source_type,
ssl_mode,
start_data_migration,
subscriptionId,
tags,
targetDbServerName,
target_db_server_fully_qualified_domain_name,
target_db_server_metadata,
target_db_server_resource_id,
trigger_cutover
FROM azure.postgresql.vw_migrations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetDbServerName = '{{ targetDbServerName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.postgresql.migrations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetDbServerName = '{{ targetDbServerName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>migrations</code> resource.

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
INSERT INTO azure.postgresql.migrations (
migrationName,
resourceGroupName,
subscriptionId,
targetDbServerName,
properties,
tags,
location
)
SELECT 
'{{ migrationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ targetDbServerName }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: migrationId
          value: string
        - name: currentStatus
          value:
            - name: state
              value: []
            - name: error
              value: string
            - name: currentSubStateDetails
              value:
                - name: currentSubState
                  value: []
                - name: dbDetails
                  value: object
                - name: validationDetails
                  value:
                    - name: status
                      value: []
                    - name: validationStartTimeInUtc
                      value: string
                    - name: validationEndTimeInUtc
                      value: string
                    - name: serverLevelValidationDetails
                      value:
                        - - name: type
                            value: string
                          - name: messages
                            value:
                              - - name: message
                                  value: string
                    - name: dbLevelValidationDetails
                      value:
                        - - name: databaseName
                            value: string
                          - name: startedOn
                            value: string
                          - name: endedOn
                            value: string
                          - name: summary
                            value:
                              - - name: type
                                  value: string
                                - name: messages
                                  value:
                                    - - name: message
                                        value: string
        - name: migrationInstanceResourceId
          value: string
        - name: migrationMode
          value: []
        - name: migrationOption
          value: []
        - name: sourceType
          value: []
        - name: sslMode
          value: []
        - name: sourceDbServerMetadata
          value:
            - name: location
              value: string
            - name: version
              value: string
            - name: storageMb
              value: integer
            - name: sku
              value:
                - name: name
                  value: string
                - name: tier
                  value: string
        - name: sourceDbServerResourceId
          value: string
        - name: sourceDbServerFullyQualifiedDomainName
          value: string
        - name: targetDbServerResourceId
          value: string
        - name: targetDbServerFullyQualifiedDomainName
          value: string
        - name: secretParameters
          value:
            - name: adminCredentials
              value:
                - name: sourceServerPassword
                  value: string
                - name: targetServerPassword
                  value: string
            - name: sourceServerUsername
              value: string
            - name: targetServerUsername
              value: string
        - name: dbsToMigrate
          value:
            - string
        - name: setupLogicalReplicationOnSourceDbIfNeeded
          value: string
        - name: overwriteDbsInTarget
          value: string
        - name: migrationWindowStartTimeInUtc
          value: string
        - name: migrationWindowEndTimeInUtc
          value: string
        - name: migrateRoles
          value: string
        - name: startDataMigration
          value: string
        - name: triggerCutover
          value: string
        - name: dbsToTriggerCutoverOn
          value:
            - string
        - name: cancel
          value: string
        - name: dbsToCancelMigrationOn
          value:
            - string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>migrations</code> resource.

```sql
/*+ update */
UPDATE azure.postgresql.migrations
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
migrationName = '{{ migrationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetDbServerName = '{{ targetDbServerName }}';
```

## `DELETE` example

Deletes the specified <code>migrations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.postgresql.migrations
WHERE migrationName = '{{ migrationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetDbServerName = '{{ targetDbServerName }}';
```
