---
title: test_job_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - test_job_streams
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

Creates, updates, deletes, gets or lists a <code>test_job_streams</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_job_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.test_job_streams" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_test_job_streams', value: 'view', },
        { label: 'test_job_streams', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the id of the resource. |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobStreamId" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_stream_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runbookName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="id" /> | `string` | Gets or sets the id of the resource. |
| <CopyableCode code="properties" /> | `object` | Definition of the job stream. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, jobStreamId, resourceGroupName, runbookName, subscriptionId" /> | Retrieve a test job stream of the test job identified by runbook name and stream id. |
| <CopyableCode code="list_by_test_job" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Retrieve a list of test job streams identified by runbook name. |

## `SELECT` examples

Retrieve a list of test job streams identified by runbook name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_test_job_streams', value: 'view', },
        { label: 'test_job_streams', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
automationAccountName,
jobStreamId,
job_stream_id,
resourceGroupName,
runbookName,
stream_text,
stream_type,
subscriptionId,
summary,
time,
value
FROM azure.automation.vw_test_job_streams
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runbookName = '{{ runbookName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
properties
FROM azure.automation.test_job_streams
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runbookName = '{{ runbookName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

