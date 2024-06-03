---
title: patch_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_deployments
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.osconfig.patch_deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Unique name for the patch deployment resource in a project. The patch deployment name is in the form: `projects/&#123;project_id&#125;/patchDeployments/&#123;patch_deployment_id&#125;`. This field is ignored when you create a new patch deployment. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the patch deployment. Length of the description is limited to 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="duration" /> | `string` | Optional. Duration of the patch. After the duration ends, the patch times out. |
| <CopyableCode code="instanceFilter" /> | `object` | A filter to target VM instances for patching. The targeted VMs must meet all criteria specified. So if both labels and zones are specified, the patch job targets only VMs with those labels and in those zones. |
| <CopyableCode code="lastExecuteTime" /> | `string` | Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="oneTimeSchedule" /> | `object` | Sets the time for a one time patch deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="patchConfig" /> | `object` | Patch configuration specifications. Contains details on how to apply the patch(es) to a VM instance. |
| <CopyableCode code="recurringSchedule" /> | `object` | Sets the time for recurring patch deployments. |
| <CopyableCode code="rollout" /> | `object` | Patch rollout configuration specifications. Contains details on the concurrency control when applying patch(es) to all targeted VMs. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the patch deployment. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Get an OS Config patch deployment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Get a page of OS Config patch deployments. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Create an OS Config patch deployment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Delete an OS Config patch deployment. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Update an OS Config patch deployment. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Get a page of OS Config patch deployments. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs. |
