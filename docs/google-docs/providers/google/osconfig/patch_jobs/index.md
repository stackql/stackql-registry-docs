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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.patch_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Unique identifier for this patch job in the form `projects/*/patchJobs/*` |
| `description` | `string` | Description of the patch job. Length of the description is limited to 1024 characters. |
| `patchDeployment` | `string` | Output only. Name of the patch deployment that created this patch job. |
| `createTime` | `string` | Time this patch job was created. |
| `percentComplete` | `number` | Reflects the overall progress of the patch job in the range of 0.0 being no progress to 100.0 being complete. |
| `displayName` | `string` | Display name for this patch job. This is not a unique identifier. |
| `dryRun` | `boolean` | If this patch job is a dry run, the agent reports that it has finished without running any updates on the VM instance. |
| `duration` | `string` | Duration of the patch job. After the duration ends, the patch job times out. |
| `updateTime` | `string` | Last time this patch job was updated. |
| `instanceFilter` | `object` | A filter to target VM instances for patching. The targeted VMs must meet all criteria specified. So if both labels and zones are specified, the patch job targets only VMs with those labels and in those zones. |
| `errorMessage` | `string` | If this patch job failed, this message provides information about the failure. |
| `instanceDetailsSummary` | `object` | A summary of the current patch state across all instances that this patch job affects. Contains counts of instances in different states. These states map to `InstancePatchState`. List patch job instance details to see the specific states of each instance. |
| `rollout` | `object` | Patch rollout configuration specifications. Contains details on the concurrency control when applying patch(es) to all targeted VMs. |
| `state` | `string` | The current state of the PatchJob. |
| `patchConfig` | `object` | Patch configuration specifications. Contains details on how to apply the patch(es) to a VM instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `patchJobsId, projectsId` | Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs. |
| `list` | `SELECT` | `projectsId` | Get a list of patch jobs. |
| `_list` | `EXEC` | `projectsId` | Get a list of patch jobs. |
| `cancel` | `EXEC` | `patchJobsId, projectsId` | Cancel a patch job. The patch job must be active. Canceled patch jobs cannot be restarted. |
| `execute` | `EXEC` | `projectsId` | Patch VM instances by creating and running a patch job. |
