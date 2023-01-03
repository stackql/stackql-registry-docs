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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The fully qualified name of this Job. Format: projects/{project}/locations/{location}/jobs/{job} |
| `terminalCondition` | `object` | Defines a status condition for a resource. |
| `observedGeneration` | `string` | Output only. The generation of this Job. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
| `launchStage` | `string` | The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`. If no value is specified, GA is assumed. |
| `expireTime` | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. |
| `deleteTime` | `string` | Output only. The deletion time. |
| `generation` | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| `executionCount` | `integer` | Output only. Number of executions created for this job. |
| `annotations` | `object` | KRM-style annotations for the resource. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run will populate some annotations using 'run.googleapis.com' or 'serving.knative.dev' namespaces. This field follows Kubernetes annotations' namespacing, limits, and rules. More info: https://kubernetes.io/docs/user-guide/annotations |
| `template` | `object` | ExecutionTemplate describes the data an execution should have when created from a template. |
| `lastModifier` | `string` | Output only. Email address of the last authenticated modifier. |
| `createTime` | `string` | Output only. The creation time. |
| `binaryAuthorization` | `object` | Settings for Binary Authorization feature. |
| `latestCreatedExecution` | `object` | Reference to an Execution. Use /Executions.GetExecution with the given name to get full execution including the latest status. |
| `labels` | `object` | KRM-style labels for the resource. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels Cloud Run will populate some labels with 'run.googleapis.com' or 'serving.knative.dev' namespaces. Those labels are read-only, and user changes will not be preserved. |
| `etag` | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `creator` | `string` | Output only. Email address of the authenticated creator. |
| `uid` | `string` | Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| `reconciling` | `boolean` | Output only. Returns true if the Job is currently being acted upon by the system to bring it into the desired state. When a new Job is created, or an existing one is updated, Cloud Run will asynchronously perform all necessary steps to bring the Job to the desired state. This process is called reconciliation. While reconciliation is in process, `observed_generation` and `latest_succeeded_execution`, will have transient values that might mismatch the intended state: Once reconciliation is over (and this field is false), there are two possible outcomes: reconciliation succeeded and the state matches the Job, or there was an error, and reconciliation failed. This state can be found in `terminal_condition.state`. If reconciliation succeeded, the following fields will match: `observed_generation` and `generation`, `latest_succeeded_execution` and `latest_created_execution`. If reconciliation failed, `observed_generation` and `latest_succeeded_execution` will have the state of the last succeeded execution or empty for newly created Job. Additional information on the failure can be found in `terminal_condition` and `conditions`. |
| `clientVersion` | `string` | Arbitrary version identifier for the API client. |
| `client` | `string` | Arbitrary identifier for the API client. |
| `conditions` | `array` | Output only. The Conditions of all other associated sub-resources. They contain additional diagnostics information in case the Job does not reach its desired state. See comments in `reconciling` for additional information on reconciliation process in Cloud Run. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_get` | `SELECT` | `jobsId, locationsId, projectsId` | Gets information about a Job. |
| `projects_locations_jobs_list` | `SELECT` | `locationsId, projectsId` | List Jobs. |
| `projects_locations_jobs_create` | `INSERT` | `locationsId, projectsId` | Create a Job. |
| `projects_locations_jobs_delete` | `DELETE` | `jobsId, locationsId, projectsId` | Deletes a Job. |
| `projects_locations_jobs_patch` | `EXEC` | `jobsId, locationsId, projectsId` | Updates a Job. |
| `projects_locations_jobs_run` | `EXEC` | `jobsId, locationsId, projectsId` | Triggers creation of a new Execution of this Job. |
