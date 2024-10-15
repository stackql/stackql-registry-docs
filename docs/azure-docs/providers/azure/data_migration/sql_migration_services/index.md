---
title: sql_migration_services
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_migration_services
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

Creates, updates, deletes, gets or lists a <code>sql_migration_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_migration_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.sql_migration_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_migration_services', value: 'view', },
        { label: 'sql_migration_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="integration_runtime_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlMigrationServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | The SQL Migration Service properties. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlMigrationServiceName, subscriptionId" /> | Retrieve the Database Migration Service |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve all SQL migration services in the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve all SQL migration services in the subscriptions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlMigrationServiceName, subscriptionId" /> | Create or Update Database Migration Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlMigrationServiceName, subscriptionId" /> | Delete Database Migration Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlMigrationServiceName, subscriptionId" /> | Update Database Migration Service. |
| <CopyableCode code="delete_node" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlMigrationServiceName, subscriptionId" /> | Delete the integration runtime node. |
| <CopyableCode code="regenerate_auth_keys" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlMigrationServiceName, subscriptionId" /> | Regenerate a new set of Authentication Keys for Self Hosted Integration Runtime. |

## `SELECT` examples

Retrieve all SQL migration services in the subscriptions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_migration_services', value: 'view', },
        { label: 'sql_migration_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
integration_runtime_state,
location,
provisioning_state,
resourceGroupName,
sqlMigrationServiceName,
subscriptionId,
system_data,
tags,
type
FROM azure.data_migration.vw_sql_migration_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
tags,
type
FROM azure.data_migration.sql_migration_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_migration_services</code> resource.

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
INSERT INTO azure.data_migration.sql_migration_services (
resourceGroupName,
sqlMigrationServiceName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlMigrationServiceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
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
        - name: provisioningState
          value: string
        - name: integrationRuntimeState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_migration_services</code> resource.

```sql
/*+ update */
UPDATE azure.data_migration.sql_migration_services
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlMigrationServiceName = '{{ sqlMigrationServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sql_migration_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_migration.sql_migration_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlMigrationServiceName = '{{ sqlMigrationServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
