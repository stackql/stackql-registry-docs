---
title: source_control_sync_job_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_sync_job_streams
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

Creates, updates, deletes, gets or lists a <code>source_control_sync_job_streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_control_sync_job_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.source_control_sync_job_streams" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_source_control_sync_job_streams', value: 'view', },
        { label: 'source_control_sync_job_streams', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource id. |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sourceControlName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sourceControlSyncJobId" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_control_sync_job_stream_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="streamId" /> | `text` | field from the `properties` object |
| <CopyableCode code="stream_text" /> | `text` | field from the `properties` object |
| <CopyableCode code="stream_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="time" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource id. |
| <CopyableCode code="properties" /> | `object` | Definition of source control sync job stream by id properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, streamId, subscriptionId" /> | Retrieve a sync job stream identified by stream id. |
| <CopyableCode code="list_by_sync_job" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, subscriptionId" /> | Retrieve a list of sync job streams identified by sync job id. |

## `SELECT` examples

Retrieve a list of sync job streams identified by sync job id.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_source_control_sync_job_streams', value: 'view', },
        { label: 'source_control_sync_job_streams', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
automationAccountName,
resourceGroupName,
sourceControlName,
sourceControlSyncJobId,
source_control_sync_job_stream_id,
streamId,
stream_text,
stream_type,
subscriptionId,
summary,
time,
value
FROM azure.automation.vw_source_control_sync_job_streams
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlName = '{{ sourceControlName }}'
AND sourceControlSyncJobId = '{{ sourceControlSyncJobId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
properties
FROM azure.automation.source_control_sync_job_streams
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlName = '{{ sourceControlName }}'
AND sourceControlSyncJobId = '{{ sourceControlSyncJobId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

