---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - run
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.run.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The fully qualified name of this Job. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/jobs/&#123;job&#125; |
| <CopyableCode code="annotations" /> | `object` | Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run API v2 does not support annotations with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected on new resources. All system annotations in v1 now have a corresponding field in v2 Job. This field follows Kubernetes annotations' namespacing, limits, and rules. |
| <CopyableCode code="binaryAuthorization" /> | `object` | Settings for Binary Authorization feature. |
| <CopyableCode code="client" /> | `string` | Arbitrary identifier for the API client. |
| <CopyableCode code="clientVersion" /> | `string` | Arbitrary version identifier for the API client. |
| <CopyableCode code="conditions" /> | `array` | Output only. The Conditions of all other associated sub-resources. They contain additional diagnostics information in case the Job does not reach its desired state. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time. |
| <CopyableCode code="creator" /> | `string` | Output only. Email address of the authenticated creator. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The deletion time. |
| <CopyableCode code="etag" /> | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| <CopyableCode code="executionCount" /> | `integer` | Output only. Number of executions created for this job. |
| <CopyableCode code="expireTime" /> | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. |
| <CopyableCode code="generation" /> | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| <CopyableCode code="labels" /> | `object` | Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels. Cloud Run API v2 does not support labels with `run.googleapis.com`, `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev` namespaces, and they will be rejected. All system labels in v1 now have a corresponding field in v2 Job. |
| <CopyableCode code="lastModifier" /> | `string` | Output only. Email address of the last authenticated modifier. |
| <CopyableCode code="latestCreatedExecution" /> | `object` | Reference to an Execution. Use /Executions.GetExecution with the given name to get full execution including the latest status. |
| <CopyableCode code="launchStage" /> | `string` | The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, GA is assumed. Set the launch stage to a preview stage on input to allow use of preview features in that stage. On read (or output), describes whether the resource uses preview features. For example, if ALPHA is provided as input, but only BETA and GA-level features are used, this field will be BETA on output. |
| <CopyableCode code="observedGeneration" /> | `string` | Output only. The generation of this Job. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Returns true if the Job is currently being acted upon by the system to bring it into the desired state. When a new Job is created, or an existing one is updated, Cloud Run will asynchronously perform all necessary steps to bring the Job to the desired state. This process is called reconciliation. While reconciliation is in process, `observed_generation` and `latest_succeeded_execution`, will have transient values that might mismatch the intended state: Once reconciliation is over (and this field is false), there are two possible outcomes: reconciliation succeeded and the state matches the Job, or there was an error, and reconciliation failed. This state can be found in `terminal_condition.state`. If reconciliation succeeded, the following fields will match: `observed_generation` and `generation`, `latest_succeeded_execution` and `latest_created_execution`. If reconciliation failed, `observed_generation` and `latest_succeeded_execution` will have the state of the last succeeded execution or empty for newly created Job. Additional information on the failure can be found in `terminal_condition` and `conditions`. |
| <CopyableCode code="runExecutionToken" /> | `string` | A unique string used as a suffix for creating a new execution. The Job will become ready when the execution is successfully completed. The sum of job name and token length must be fewer than 63 characters. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="startExecutionToken" /> | `string` | A unique string used as a suffix creating a new execution. The Job will become ready when the execution is successfully started. The sum of job name and token length must be fewer than 63 characters. |
| <CopyableCode code="template" /> | `object` | ExecutionTemplate describes the data an execution should have when created from a template. |
| <CopyableCode code="terminalCondition" /> | `object` | Defines a status condition for a resource. |
| <CopyableCode code="uid" /> | `string` | Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last-modified time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Gets information about a Job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Jobs. Results are sorted by creation time, descending. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Deletes a Job. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Updates a Job. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Jobs. Results are sorted by creation time, descending. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Triggers creation of a new Execution of this Job. |
