---
title: sql_jobs_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_jobs_controllers
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

Creates, updates, deletes, gets or lists a <code>sql_jobs_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_jobs_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_jobs_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_jobs_controllers', value: 'view', },
        { label: 'sql_jobs_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activity_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_request_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Job REST Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Get a SqlJob |
| <CopyableCode code="list_by_sql_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | List SqlJob resources by SqlSite |

## `SELECT` examples

List SqlJob resources by SqlSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sql_jobs_controllers', value: 'view', },
        { label: 'sql_jobs_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
activity_id,
client_request_id,
display_name,
end_time,
errors,
jobName,
provisioning_state,
resourceGroupName,
siteName,
sqlSiteName,
start_time,
status,
subscriptionId
FROM azure.migrate.vw_sql_jobs_controllers
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
FROM azure.migrate.sql_jobs_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND sqlSiteName = '{{ sqlSiteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

