---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - dataflow
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
<tr><td><b>Id</b></td><td><code>google.dataflow.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of this job. This field is set by the Cloud Dataflow service when the Job is created, and is immutable for the life of the job. |
| `name` | `string` | The user-specified Cloud Dataflow job name. Only one Job with a given name can exist in a project within one region at any given time. Jobs in different regions can have the same name. If a caller attempts to create a Job with the same name as an already-existing Job, the attempt returns the existing Job. The name must match the regular expression `[a-z]([-a-z0-9]{0,1022}[a-z0-9])?` |
| `labels` | `object` | User-defined labels for this job. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \p{Ll}\p{Lo}{0,62} * Values must conform to regexp: [\p{Ll}\p{Lo}\p{N}_-]{0,63} * Both keys and values are additionally constrained to be &lt;= 128 bytes in size. |
| `replaceJobId` | `string` | If this job is an update of an existing job, this field is the job ID of the job it replaced. When sending a `CreateJobRequest`, you can update a job by specifying it here. The job named here is stopped, and its intermediate state is transferred to this job. |
| `currentState` | `string` | The current state of the job. Jobs are created in the `JOB_STATE_STOPPED` state unless otherwise specified. A job in the `JOB_STATE_RUNNING` state may asynchronously enter a terminal state. After a job has reached a terminal state, no further state updates may be made. This field may be mutated by the Cloud Dataflow service; callers cannot mutate it. |
| `pipelineDescription` | `object` | A descriptive representation of submitted pipeline as well as the executed form. This data is provided by the Dataflow service for ease of visualizing the pipeline and interpreting Dataflow provided metrics. |
| `tempFiles` | `array` | A set of files the system should be aware of that are used for temporary storage. These temporary files will be removed on job completion. No duplicates are allowed. No file patterns are supported. The supported files are: Google Cloud Storage: storage.googleapis.com/{bucket}/{object} bucket.storage.googleapis.com/{object} |
| `currentStateTime` | `string` | The timestamp associated with the current state. |
| `environment` | `object` | Describes the environment in which a Dataflow Job runs. |
| `satisfiesPzs` | `boolean` | Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests. |
| `projectId` | `string` | The ID of the Cloud Platform project that the job belongs to. |
| `location` | `string` | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job. |
| `type` | `string` | The type of Cloud Dataflow job. |
| `jobMetadata` | `object` | Metadata available primarily for filtering jobs. Will be included in the ListJob response and Job SUMMARY view. |
| `replacedByJobId` | `string` | If another job is an update of this job (and thus, this job is in `JOB_STATE_UPDATED`), this field contains the ID of that job. |
| `stageStates` | `array` | This field may be mutated by the Cloud Dataflow service; callers cannot mutate it. |
| `steps` | `array` | Exactly one of step or steps_location should be specified. The top-level steps that constitute the entire job. Only retrieved with JOB_VIEW_ALL. |
| `stepsLocation` | `string` | The Cloud Storage location where the steps are stored. |
| `createdFromSnapshotId` | `string` | If this is specified, the job's initial state is populated from the given snapshot. |
| `startTime` | `string` | The timestamp when the job was started (transitioned to JOB_STATE_PENDING). Flexible resource scheduling jobs are started with some delay after job creation, so start_time is unset before start and is updated when the job is started by the Cloud Dataflow service. For other jobs, start_time always equals to create_time and is immutable and set by the Cloud Dataflow service. |
| `transformNameMapping` | `object` | The map of transform name prefixes of the job to be replaced to the corresponding name prefixes of the new job. |
| `createTime` | `string` | The timestamp when the job was initially created. Immutable and set by the Cloud Dataflow service. |
| `requestedState` | `string` | The job's requested state. `UpdateJob` may be used to switch between the `JOB_STATE_STOPPED` and `JOB_STATE_RUNNING` states, by setting requested_state. `UpdateJob` may also be used to directly set a job's requested state to `JOB_STATE_CANCELLED` or `JOB_STATE_DONE`, irrevocably terminating the job if it has not already reached a terminal state. |
| `clientRequestId` | `string` | The client's unique identifier of the job, re-used across retried attempts. If this field is set, the service will ensure its uniqueness. The request to create a job will fail if the service has knowledge of a previously submitted job with the same client's ID and job name. The caller may use this field to ensure idempotence of job creation across retried attempts to create a job. By default, the field is empty and, in that case, the service ignores it. |
| `executionInfo` | `object` | Additional information about how a Cloud Dataflow job will be executed that isn't contained in the submitted job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_jobs_get` | `SELECT` | `jobId, projectId` | Gets the state of the specified Cloud Dataflow job. To get the state of a job, we recommend using `projects.locations.jobs.get` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.get` is not recommended, as you can only get the state of jobs that are running in `us-central1`. |
| `projects_jobs_list` | `SELECT` | `projectId` | List the jobs of a project. To list the jobs of a project in a region, we recommend using `projects.locations.jobs.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use `projects.jobs.aggregated`. Using `projects.jobs.list` is not recommended, as you can only get the list of jobs that are running in `us-central1`. |
| `projects_locations_jobs_get` | `SELECT` | `jobId, location, projectId` | Gets the state of the specified Cloud Dataflow job. To get the state of a job, we recommend using `projects.locations.jobs.get` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.get` is not recommended, as you can only get the state of jobs that are running in `us-central1`. |
| `projects_locations_jobs_list` | `SELECT` | `location, projectId` | List the jobs of a project. To list the jobs of a project in a region, we recommend using `projects.locations.jobs.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use `projects.jobs.aggregated`. Using `projects.jobs.list` is not recommended, as you can only get the list of jobs that are running in `us-central1`. |
| `projects_jobs_create` | `INSERT` | `projectId` | Creates a Cloud Dataflow job. To create a job, we recommend using `projects.locations.jobs.create` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.create` is not recommended, as your job will always start in `us-central1`. Do not enter confidential information when you supply string values using the API. |
| `projects_locations_jobs_create` | `INSERT` | `location, projectId` | Creates a Cloud Dataflow job. To create a job, we recommend using `projects.locations.jobs.create` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.create` is not recommended, as your job will always start in `us-central1`. Do not enter confidential information when you supply string values using the API. |
| `projects_jobs_snapshot` | `EXEC` | `jobId, projectId` | Snapshot the state of a streaming job. |
| `projects_jobs_update` | `EXEC` | `jobId, projectId` | Updates the state of an existing Cloud Dataflow job. To update the state of an existing job, we recommend using `projects.locations.jobs.update` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.update` is not recommended, as you can only update the state of jobs that are running in `us-central1`. |
| `projects_locations_jobs_snapshot` | `EXEC` | `jobId, location, projectId` | Snapshot the state of a streaming job. |
| `projects_locations_jobs_update` | `EXEC` | `jobId, location, projectId` | Updates the state of an existing Cloud Dataflow job. To update the state of an existing job, we recommend using `projects.locations.jobs.update` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.update` is not recommended, as you can only update the state of jobs that are running in `us-central1`. |
