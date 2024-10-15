---
title: sql_availability_groups_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_availability_groups_controllers
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

Creates, updates, deletes, gets or lists a <code>sql_availability_groups_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_availability_groups_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_availability_groups_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_availability_groups_controllers', value: 'view', },
        { label: 'sql_availability_groups_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availability_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_group_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_replicas" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_multi_sub_net" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_part_of_distributed_availability_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent_replica_overview_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlAvailabilityGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for SQL Server availability group properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlAvailabilityGroupName, sqlSiteName, subscriptionId" /> | Gets the sql availability group. |
| <CopyableCode code="list_by_sql_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Gets the sql availability groups. |

## `SELECT` examples

Gets the sql availability groups.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_availability_groups_controllers', value: 'view', },
        { label: 'sql_availability_groups_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availability_group_name,
availability_group_type,
availability_replicas,
cluster_name,
created_timestamp,
is_deleted,
is_multi_sub_net,
is_part_of_distributed_availability_group,
parent_replica_overview_list,
provisioning_state,
resourceGroupName,
siteName,
sqlAvailabilityGroupName,
sqlSiteName,
subscriptionId,
updated_timestamp
FROM azure.migrate.vw_sql_availability_groups_controllers
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
FROM azure.migrate.sql_availability_groups_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

