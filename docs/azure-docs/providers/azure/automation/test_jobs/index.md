---
title: test_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - test_jobs
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

Creates, updates, deletes, gets or lists a <code>test_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.test_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | Gets or sets the creation time of the test job. |
| <CopyableCode code="endTime" /> | `string` | Gets or sets the end time of the test job. |
| <CopyableCode code="exception" /> | `string` | Gets or sets the exception of the test job. |
| <CopyableCode code="lastModifiedTime" /> | `string` | Gets or sets the last modified time of the test job. |
| <CopyableCode code="lastStatusModifiedTime" /> | `string` | Gets or sets the last status modified time of the test job. |
| <CopyableCode code="logActivityTrace" /> | `integer` | The activity-level tracing options of the runbook. |
| <CopyableCode code="parameters" /> | `object` | Gets or sets the parameters of the test job. |
| <CopyableCode code="runOn" /> | `string` | Gets or sets the runOn which specifies the group name where the job is to be executed. |
| <CopyableCode code="startTime" /> | `string` | Gets or sets the start time of the test job. |
| <CopyableCode code="status" /> | `string` | Gets or sets the status of the test job. |
| <CopyableCode code="statusDetails" /> | `string` | Gets or sets the status details of the test job. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Retrieve the test job for the specified runbook. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Create a test job of the runbook. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Resume the test job. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Stop the test job. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Suspend the test job. |

## `SELECT` examples

Retrieve the test job for the specified runbook.


```sql
SELECT
creationTime,
endTime,
exception,
lastModifiedTime,
lastStatusModifiedTime,
logActivityTrace,
parameters,
runOn,
startTime,
status,
statusDetails
FROM azure.automation.test_jobs
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runbookName = '{{ runbookName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>test_jobs</code> resource.

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
INSERT INTO azure.automation.test_jobs (
automationAccountName,
resourceGroupName,
runbookName,
subscriptionId,
parameters,
runOn
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ runbookName }}',
'{{ subscriptionId }}',
'{{ parameters }}',
'{{ runOn }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: parameters
      value: object
    - name: runOn
      value: string

```
</TabItem>
</Tabs>
