---
title: workspace_managed_sql_server_recoverable_sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_recoverable_sql_pools
  - synapse
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

Creates, updates, deletes, gets or lists a <code>workspace_managed_sql_server_recoverable_sql_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_recoverable_sql_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspace_managed_sql_server_recoverable_sql_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_managed_sql_server_recoverable_sql_pools', value: 'view', },
        { label: 'workspace_managed_sql_server_recoverable_sql_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="elastic_pool_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_available_backup_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_level_objective" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a recoverable sql pool |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get recoverable sql pools for workspace managed sql server. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Get list of recoverable sql pools for workspace managed sql server. |

## `SELECT` examples

Get list of recoverable sql pools for workspace managed sql server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_managed_sql_server_recoverable_sql_pools', value: 'view', },
        { label: 'workspace_managed_sql_server_recoverable_sql_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
edition,
elastic_pool_name,
last_available_backup_date,
resourceGroupName,
service_level_objective,
sqlPoolName,
subscriptionId,
workspaceName
FROM azure.synapse.vw_workspace_managed_sql_server_recoverable_sql_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.workspace_managed_sql_server_recoverable_sql_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

