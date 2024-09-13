---
title: patch_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_jobs
  - osconfig
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

Creates, updates, deletes or gets an <code>patch_job</code> resource or lists <code>patch_jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.osconfig.patch_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Unique identifier for this patch job in the form `projects/*/patchJobs/*` |
| <CopyableCode code="description" /> | `string` | Description of the patch job. Length of the description is limited to 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Time this patch job was created. |
| <CopyableCode code="displayName" /> | `string` | Display name for this patch job. This is not a unique identifier. |
| <CopyableCode code="dryRun" /> | `boolean` | If this patch job is a dry run, the agent reports that it has finished without running any updates on the VM instance. |
| <CopyableCode code="duration" /> | `string` | Duration of the patch job. After the duration ends, the patch job times out. |
| <CopyableCode code="errorMessage" /> | `string` | If this patch job failed, this message provides information about the failure. |
| <CopyableCode code="instanceDetailsSummary" /> | `object` | A summary of the current patch state across all instances that this patch job affects. Contains counts of instances in different states. These states map to `InstancePatchState`. List patch job instance details to see the specific states of each instance. |
| <CopyableCode code="instanceFilter" /> | `object` | A filter to target VM instances for patching. The targeted VMs must meet all criteria specified. So if both labels and zones are specified, the patch job targets only VMs with those labels and in those zones. |
| <CopyableCode code="patchConfig" /> | `object` | Patch configuration specifications. Contains details on how to apply the patch(es) to a VM instance. |
| <CopyableCode code="patchDeployment" /> | `string` | Output only. Name of the patch deployment that created this patch job. |
| <CopyableCode code="percentComplete" /> | `number` | Reflects the overall progress of the patch job in the range of 0.0 being no progress to 100.0 being complete. |
| <CopyableCode code="rollout" /> | `object` | Patch rollout configuration specifications. Contains details on the concurrency control when applying patch(es) to all targeted VMs. |
| <CopyableCode code="state" /> | `string` | The current state of the PatchJob. |
| <CopyableCode code="updateTime" /> | `string` | Last time this patch job was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="patchJobsId, projectsId" /> | Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Get a list of patch jobs. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="patchJobsId, projectsId" /> | Cancel a patch job. The patch job must be active. Canceled patch jobs cannot be restarted. |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="projectsId" /> | Patch VM instances by creating and running a patch job. |

## `SELECT` examples

Get a list of patch jobs.

```sql
SELECT
name,
description,
createTime,
displayName,
dryRun,
duration,
errorMessage,
instanceDetailsSummary,
instanceFilter,
patchConfig,
patchDeployment,
percentComplete,
rollout,
state,
updateTime
FROM google.osconfig.patch_jobs
WHERE projectsId = '{{ projectsId }}'; 
```
