---
title: database_recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_recommended_actions
  - sql
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

Creates, updates, deletes, gets or lists a <code>database_recommended_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_recommended_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_recommended_actions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_recommended_actions', value: 'view', },
        { label: 'database_recommended_actions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="advisorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="estimated_impact" /> | `text` | field from the `properties` object |
| <CopyableCode code="execute_action_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="execute_action_initiated_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="execute_action_initiated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="execute_action_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="implementation_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_archived_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_executable_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_revertable_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Resource kind. |
| <CopyableCode code="last_refresh" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_objects" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="observed_impact" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendedActionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="revert_action_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="revert_action_initiated_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="revert_action_initiated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="revert_action_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="score" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_series" /> | `text` | field from the `properties` object |
| <CopyableCode code="valid_since" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Resource kind. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties for a Database, Server or Elastic Pool Recommended Action. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId" /> | Gets a database recommended action. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId" /> | Updates a database recommended action. |
| <CopyableCode code="list_by_database_advisor" /> | `EXEC` | <CopyableCode code="advisorName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets list of Database Recommended Actions. |

## `SELECT` examples

Gets a database recommended action.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_database_recommended_actions', value: 'view', },
        { label: 'database_recommended_actions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
advisorName,
databaseName,
details,
error_details,
estimated_impact,
execute_action_duration,
execute_action_initiated_by,
execute_action_initiated_time,
execute_action_start_time,
implementation_details,
is_archived_action,
is_executable_action,
is_revertable_action,
kind,
last_refresh,
linked_objects,
location,
observed_impact,
recommendation_reason,
recommendedActionName,
resourceGroupName,
revert_action_duration,
revert_action_initiated_by,
revert_action_initiated_time,
revert_action_start_time,
score,
serverName,
state,
subscriptionId,
time_series,
valid_since
FROM azure.sql.vw_database_recommended_actions
WHERE advisorName = '{{ advisorName }}'
AND databaseName = '{{ databaseName }}'
AND recommendedActionName = '{{ recommendedActionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.sql.database_recommended_actions
WHERE advisorName = '{{ advisorName }}'
AND databaseName = '{{ databaseName }}'
AND recommendedActionName = '{{ recommendedActionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>database_recommended_actions</code> resource.

```sql
/*+ update */
UPDATE azure.sql.database_recommended_actions
SET 
properties = '{{ properties }}'
WHERE 
advisorName = '{{ advisorName }}'
AND databaseName = '{{ databaseName }}'
AND recommendedActionName = '{{ recommendedActionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
