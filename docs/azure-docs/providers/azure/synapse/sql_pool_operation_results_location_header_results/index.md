---
title: sql_pool_operation_results_location_header_results
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_operation_results_location_header_results
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

Creates, updates, deletes, gets or lists a <code>sql_pool_operation_results_location_header_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_operation_results_location_header_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_operation_results_location_header_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_operation_results_location_header_results', value: 'view', },
        { label: 'sql_pool_operation_results_location_header_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="collation" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="max_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoverable_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_point_in_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="source_database_deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a SQL Analytics pool |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get the status of a SQL pool operation |

## `SELECT` examples

Get the status of a SQL pool operation

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_pool_operation_results_location_header_results', value: 'view', },
        { label: 'sql_pool_operation_results_location_header_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
collation,
create_mode,
creation_date,
location,
max_size_bytes,
operationId,
provisioning_state,
recoverable_database_id,
resourceGroupName,
restore_point_in_time,
sku,
source_database_deletion_date,
source_database_id,
sqlPoolName,
status,
storage_account_type,
subscriptionId,
tags,
workspaceName
FROM azure.synapse.vw_sql_pool_operation_results_location_header_results
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.synapse.sql_pool_operation_results_location_header_results
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

