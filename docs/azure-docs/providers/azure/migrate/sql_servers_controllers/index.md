---
title: sql_servers_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_servers_controllers
  - migrate
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

Creates, updates, deletes, gets or lists a <code>sql_servers_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_servers_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_servers_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_servers_controllers', value: 'view', },
        { label: 'sql_servers_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="engine_edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hydrated_run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyperthread_ratio" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_clustered" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_high_availability_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="logical_cpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_arm_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_overview_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_server_memory_in_use_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="num_of_logins" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_ag_databases" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_user_databases" /> | `text` | field from the `properties` object |
| <CopyableCode code="physical_cpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="port_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_support_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_fci_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_server_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sum_of_user_databases_size_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="temp_db_size_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="visible_online_core_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for SQL Server properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlServerName, sqlSiteName, subscriptionId" /> | Gets the sql server. |
| <CopyableCode code="list_by_sql_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Gets the sql servers. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, siteName, sqlServerName, sqlSiteName, subscriptionId" /> | Updates the sql server tags. |

## `SELECT` examples

Gets the sql servers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_servers_controllers', value: 'view', },
        { label: 'sql_servers_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_timestamp,
edition,
engine_edition,
errors,
host_name,
hydrated_run_as_account_id,
hyperthread_ratio,
is_clustered,
is_deleted,
is_high_availability_enabled,
logical_cpu_count,
machine_arm_ids,
machine_overview_list,
max_server_memory_in_use_in_mb,
num_of_logins,
number_of_ag_databases,
number_of_user_databases,
physical_cpu_count,
port_number,
product_support_status,
provisioning_state,
resourceGroupName,
run_as_account_id,
siteName,
sqlServerName,
sqlSiteName,
sql_fci_properties,
sql_server_name,
sql_start_time,
status,
subscriptionId,
sum_of_user_databases_size_in_mb,
tags,
temp_db_size_in_mb,
updated_timestamp,
version,
visible_online_core_count
FROM azure.migrate.vw_sql_servers_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.sql_servers_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>sql_servers_controllers</code> resource.

```sql
/*+ update */
UPDATE azure.migrate.sql_servers_controllers
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlServerName = '{{ sqlServerName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
