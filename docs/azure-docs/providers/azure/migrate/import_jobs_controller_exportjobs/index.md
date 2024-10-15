---
title: import_jobs_controller_exportjobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs_controller_exportjobs
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

Creates, updates, deletes, gets or lists a <code>import_jobs_controller_exportjobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_jobs_controller_exportjobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.import_jobs_controller_exportjobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_import_jobs_controller_exportjobs', value: 'view', },
        { label: 'import_jobs_controller_exportjobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the relative ARM name to get job. |
| <CopyableCode code="name" /> | `text` | Gets or sets the Job ID. |
| <CopyableCode code="blob_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sas_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | Gets or sets the Job status. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type name for export job. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the relative ARM name to get job. |
| <CopyableCode code="name" /> | `string` | Gets or sets the Job ID. |
| <CopyableCode code="displayName" /> | `string` | Gets or sets the Display name. |
| <CopyableCode code="endTime" /> | `string` | Gets or sets the Job end time. |
| <CopyableCode code="properties" /> | `object` |  Export Imported Machines JobEntity Properties  |
| <CopyableCode code="startTime" /> | `string` | Gets or sets the Job start time. |
| <CopyableCode code="status" /> | `string` | Gets or sets the Job status. |
| <CopyableCode code="type" /> | `string` | Type name for export job. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, siteName, subscriptionId" /> | Gets the export imported machines job with the given job name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get all export import machines job for the given site. |

## `SELECT` examples

Method to get all export import machines job for the given site.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_import_jobs_controller_exportjobs', value: 'view', },
        { label: 'import_jobs_controller_exportjobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
blob_name,
display_name,
end_time,
jobName,
resourceGroupName,
sas_uri,
siteName,
start_time,
status,
subscriptionId,
type
FROM azure.migrate.vw_import_jobs_controller_exportjobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
displayName,
endTime,
properties,
startTime,
status,
type
FROM azure.migrate.import_jobs_controller_exportjobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

