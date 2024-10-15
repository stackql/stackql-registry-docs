---
title: source_control_sync_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_sync_jobs
  - automation
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

Creates, updates, deletes, gets or lists a <code>source_control_sync_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_control_sync_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.source_control_sync_jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_source_control_sync_jobs', value: 'view', },
        { label: 'source_control_sync_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The id of the job. |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="exception" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sourceControlName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sourceControlSyncJobId" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_control_sync_job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the job. |
| <CopyableCode code="properties" /> | `object` | Definition of source control sync job properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, subscriptionId" /> | Retrieve the source control sync job identified by job id. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Retrieve a list of source control sync jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, subscriptionId, data__properties" /> | Creates the sync job for a source control. |

## `SELECT` examples

Retrieve a list of source control sync jobs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_source_control_sync_jobs', value: 'view', },
        { label: 'source_control_sync_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
automationAccountName,
creation_time,
end_time,
exception,
provisioning_state,
resourceGroupName,
sourceControlName,
sourceControlSyncJobId,
source_control_sync_job_id,
start_time,
subscriptionId,
sync_type
FROM azure.automation.vw_source_control_sync_jobs
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlName = '{{ sourceControlName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
properties
FROM azure.automation.source_control_sync_jobs
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlName = '{{ sourceControlName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>source_control_sync_jobs</code> resource.

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
INSERT INTO azure.automation.source_control_sync_jobs (
automationAccountName,
resourceGroupName,
sourceControlName,
sourceControlSyncJobId,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ sourceControlName }}',
'{{ sourceControlSyncJobId }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: commitId
          value: string

```
</TabItem>
</Tabs>
