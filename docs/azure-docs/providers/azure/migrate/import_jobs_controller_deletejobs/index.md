---
title: import_jobs_controller_deletejobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs_controller_deletejobs
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

Creates, updates, deletes, gets or lists a <code>import_jobs_controller_deletejobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_jobs_controller_deletejobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.import_jobs_controller_deletejobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_import_jobs_controller_deletejobs', value: 'view', },
        { label: 'import_jobs_controller_deletejobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blob_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_confirmation" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_sas_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_machines_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Delete Imported Machines Job Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, siteName, subscriptionId" /> | Gets the delete imported machines job with the given job name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get all delete import machines job for the given site. |

## `SELECT` examples

Method to get all delete import machines job for the given site.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_import_jobs_controller_deletejobs', value: 'view', },
        { label: 'import_jobs_controller_deletejobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
blob_name,
deletion_confirmation,
display_name,
end_time,
error_sas_uri,
errors,
jobName,
job_state,
number_of_machines_deleted,
provisioning_state,
resourceGroupName,
siteName,
start_time,
status,
subscriptionId
FROM azure.migrate.vw_import_jobs_controller_deletejobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.import_jobs_controller_deletejobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

