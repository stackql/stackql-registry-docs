
---
title: clone_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - clone_jobs
  - vmmigration
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

Creates, updates, deletes or gets an <code>clone_job</code> resource or lists <code>clone_jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clone_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.clone_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the clone. |
| <CopyableCode code="computeEngineDisksTargetDetails" /> | `object` | ComputeEngineDisksTargetDetails is a collection of created Persistent Disks details. |
| <CopyableCode code="computeEngineTargetDetails" /> | `object` | ComputeEngineTargetDetails is a collection of details for creating a VM in a target Compute Engine project. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the clone job was created (as an API call, not when it was actually created in the target). |
| <CopyableCode code="endTime" /> | `string` | Output only. The time the clone job was ended. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="state" /> | `string` | Output only. State of the clone job. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The time the state was last updated. |
| <CopyableCode code="steps" /> | `array` | Output only. The clone steps list representing its progress. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloneJobsId, locationsId, migratingVmsId, projectsId, sourcesId" /> | Gets details of a single CloneJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Lists the CloneJobs of a migrating VM. Only 25 most recent CloneJobs are listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Initiates a Clone of a specific migrating VM. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="cloneJobsId, locationsId, migratingVmsId, projectsId, sourcesId" /> | Initiates the cancellation of a running clone job. |

## `SELECT` examples

Lists the CloneJobs of a migrating VM. Only 25 most recent CloneJobs are listed.

```sql
SELECT
name,
computeEngineDisksTargetDetails,
computeEngineTargetDetails,
createTime,
endTime,
error,
state,
stateTime,
steps
FROM google.vmmigration.clone_jobs
WHERE locationsId = '{{ locationsId }}'
AND migratingVmsId = '{{ migratingVmsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clone_jobs</code> resource.

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
INSERT INTO google.vmmigration.clone_jobs (
locationsId,
migratingVmsId,
projectsId,
sourcesId,
computeEngineTargetDetails,
computeEngineDisksTargetDetails,
createTime,
endTime,
name,
state,
stateTime,
error,
steps
)
SELECT 
'{{ locationsId }}',
'{{ migratingVmsId }}',
'{{ projectsId }}',
'{{ sourcesId }}',
'{{ computeEngineTargetDetails }}',
'{{ computeEngineDisksTargetDetails }}',
'{{ createTime }}',
'{{ endTime }}',
'{{ name }}',
'{{ state }}',
'{{ stateTime }}',
'{{ error }}',
'{{ steps }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: computeEngineTargetDetails
        value: '{{ computeEngineTargetDetails }}'
      - name: computeEngineDisksTargetDetails
        value: '{{ computeEngineDisksTargetDetails }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: endTime
        value: '{{ endTime }}'
      - name: name
        value: '{{ name }}'
      - name: state
        value: '{{ state }}'
      - name: stateTime
        value: '{{ stateTime }}'
      - name: error
        value: '{{ error }}'
      - name: steps
        value: '{{ steps }}'

```
</TabItem>
</Tabs>
