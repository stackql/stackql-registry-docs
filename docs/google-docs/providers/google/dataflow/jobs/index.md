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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID of this job. This field is set by the Dataflow service when the job is created, and is immutable for the life of the job. |
| <CopyableCode code="name" /> | `string` | Optional. The user-specified Dataflow job name. Only one active job with a given name can exist in a project within one region at any given time. Jobs in different regions can have the same name. If a caller attempts to create a job with the same name as an active job that already exists, the attempt returns the existing job. The name must match the regular expression `[a-z]([-a-z0-9]&#123;0,1022&#125;[a-z0-9])?` |
| <CopyableCode code="clientRequestId" /> | `string` | The client's unique identifier of the job, re-used across retried attempts. If this field is set, the service will ensure its uniqueness. The request to create a job will fail if the service has knowledge of a previously submitted job with the same client's ID and job name. The caller may use this field to ensure idempotence of job creation across retried attempts to create a job. By default, the field is empty and, in that case, the service ignores it. |
| <CopyableCode code="createTime" /> | `string` | The timestamp when the job was initially created. Immutable and set by the Cloud Dataflow service. |
| <CopyableCode code="createdFromSnapshotId" /> | `string` | If this is specified, the job's initial state is populated from the given snapshot. |
| <CopyableCode code="currentState" /> | `string` | The current state of the job. Jobs are created in the `JOB_STATE_STOPPED` state unless otherwise specified. A job in the `JOB_STATE_RUNNING` state may asynchronously enter a terminal state. After a job has reached a terminal state, no further state updates may be made. This field might be mutated by the Dataflow service; callers cannot mutate it. |
| <CopyableCode code="currentStateTime" /> | `string` | The timestamp associated with the current state. |
| <CopyableCode code="environment" /> | `object` | Describes the environment in which a Dataflow Job runs. |
| <CopyableCode code="executionInfo" /> | `object` | Additional information about how a Cloud Dataflow job will be executed that isn't contained in the submitted job. |
| <CopyableCode code="jobMetadata" /> | `object` | Metadata available primarily for filtering jobs. Will be included in the ListJob response and Job SUMMARY view. |
| <CopyableCode code="labels" /> | `object` | User-defined labels for this job. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \p&#123;Ll&#125;\p&#123;Lo&#125;&#123;0,62&#125; * Values must conform to regexp: [\p&#123;Ll&#125;\p&#123;Lo&#125;\p&#123;N&#125;_-]&#123;0,63&#125; * Both keys and values are additionally constrained to be &lt;= 128 bytes in size. |
| <CopyableCode code="location" /> | `string` | The [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that contains this job. |
| <CopyableCode code="pipelineDescription" /> | `object` | A descriptive representation of submitted pipeline as well as the executed form. This data is provided by the Dataflow service for ease of visualizing the pipeline and interpreting Dataflow provided metrics. |
| <CopyableCode code="projectId" /> | `string` | The ID of the Google Cloud project that the job belongs to. |
| <CopyableCode code="replaceJobId" /> | `string` | If this job is an update of an existing job, this field is the job ID of the job it replaced. When sending a `CreateJobRequest`, you can update a job by specifying it here. The job named here is stopped, and its intermediate state is transferred to this job. |
| <CopyableCode code="replacedByJobId" /> | `string` | If another job is an update of this job (and thus, this job is in `JOB_STATE_UPDATED`), this field contains the ID of that job. |
| <CopyableCode code="requestedState" /> | `string` | The job's requested state. Applies to `UpdateJob` requests. Set `requested_state` with `UpdateJob` requests to switch between the states `JOB_STATE_STOPPED` and `JOB_STATE_RUNNING`. You can also use `UpdateJob` requests to change a job's state from `JOB_STATE_RUNNING` to `JOB_STATE_CANCELLED`, `JOB_STATE_DONE`, or `JOB_STATE_DRAINED`. These states irrevocably terminate the job if it hasn't already reached a terminal state. This field has no effect on `CreateJob` requests. |
| <CopyableCode code="runtimeUpdatableParams" /> | `object` | Additional job parameters that can only be updated during runtime using the projects.jobs.update method. These fields have no effect when specified during job creation. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Reserved for future use. This field is set only in responses from the server; it is ignored if it is set in any requests. |
| <CopyableCode code="stageStates" /> | `array` | This field may be mutated by the Cloud Dataflow service; callers cannot mutate it. |
| <CopyableCode code="startTime" /> | `string` | The timestamp when the job was started (transitioned to JOB_STATE_PENDING). Flexible resource scheduling jobs are started with some delay after job creation, so start_time is unset before start and is updated when the job is started by the Cloud Dataflow service. For other jobs, start_time always equals to create_time and is immutable and set by the Cloud Dataflow service. |
| <CopyableCode code="steps" /> | `array` | Exactly one of step or steps_location should be specified. The top-level steps that constitute the entire job. Only retrieved with JOB_VIEW_ALL. |
| <CopyableCode code="stepsLocation" /> | `string` | The Cloud Storage location where the steps are stored. |
| <CopyableCode code="tempFiles" /> | `array` | A set of files the system should be aware of that are used for temporary storage. These temporary files will be removed on job completion. No duplicates are allowed. No file patterns are supported. The supported files are: Google Cloud Storage: storage.googleapis.com/&#123;bucket&#125;/&#123;object&#125; bucket.storage.googleapis.com/&#123;object&#125; |
| <CopyableCode code="transformNameMapping" /> | `object` | The map of transform name prefixes of the job to be replaced to the corresponding name prefixes of the new job. |
| <CopyableCode code="type" /> | `string` | Optional. The type of Dataflow job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_jobs_get" /> | `SELECT` | <CopyableCode code="jobId, projectId" /> | Gets the state of the specified Cloud Dataflow job. To get the state of a job, we recommend using `projects.locations.jobs.get` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.get` is not recommended, as you can only get the state of jobs that are running in `us-central1`. |
| <CopyableCode code="projects_jobs_list" /> | `SELECT` | <CopyableCode code="projectId" /> | List the jobs of a project. To list the jobs of a project in a region, we recommend using `projects.locations.jobs.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use `projects.jobs.aggregated`. Using `projects.jobs.list` is not recommended, because you can only get the list of jobs that are running in `us-central1`. `projects.locations.jobs.list` and `projects.jobs.list` support filtering the list of jobs by name. Filtering by name isn't supported by `projects.jobs.aggregated`. |
| <CopyableCode code="projects_locations_jobs_get" /> | `SELECT` | <CopyableCode code="jobId, location, projectId" /> | Gets the state of the specified Cloud Dataflow job. To get the state of a job, we recommend using `projects.locations.jobs.get` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.get` is not recommended, as you can only get the state of jobs that are running in `us-central1`. |
| <CopyableCode code="projects_locations_jobs_list" /> | `SELECT` | <CopyableCode code="location, projectId" /> | List the jobs of a project. To list the jobs of a project in a region, we recommend using `projects.locations.jobs.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use `projects.jobs.aggregated`. Using `projects.jobs.list` is not recommended, because you can only get the list of jobs that are running in `us-central1`. `projects.locations.jobs.list` and `projects.jobs.list` support filtering the list of jobs by name. Filtering by name isn't supported by `projects.jobs.aggregated`. |
| <CopyableCode code="projects_jobs_create" /> | `INSERT` | <CopyableCode code="projectId" /> | Creates a Cloud Dataflow job. To create a job, we recommend using `projects.locations.jobs.create` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.create` is not recommended, as your job will always start in `us-central1`. Do not enter confidential information when you supply string values using the API. |
| <CopyableCode code="projects_locations_jobs_create" /> | `INSERT` | <CopyableCode code="location, projectId" /> | Creates a Cloud Dataflow job. To create a job, we recommend using `projects.locations.jobs.create` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.create` is not recommended, as your job will always start in `us-central1`. Do not enter confidential information when you supply string values using the API. |
| <CopyableCode code="projects_jobs_update" /> | `UPDATE` | <CopyableCode code="jobId, projectId" /> | Updates the state of an existing Cloud Dataflow job. To update the state of an existing job, we recommend using `projects.locations.jobs.update` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.update` is not recommended, as you can only update the state of jobs that are running in `us-central1`. |
| <CopyableCode code="projects_locations_jobs_update" /> | `UPDATE` | <CopyableCode code="jobId, location, projectId" /> | Updates the state of an existing Cloud Dataflow job. To update the state of an existing job, we recommend using `projects.locations.jobs.update` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). Using `projects.jobs.update` is not recommended, as you can only update the state of jobs that are running in `us-central1`. |
| <CopyableCode code="_projects_jobs_list" /> | `EXEC` | <CopyableCode code="projectId" /> | List the jobs of a project. To list the jobs of a project in a region, we recommend using `projects.locations.jobs.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use `projects.jobs.aggregated`. Using `projects.jobs.list` is not recommended, because you can only get the list of jobs that are running in `us-central1`. `projects.locations.jobs.list` and `projects.jobs.list` support filtering the list of jobs by name. Filtering by name isn't supported by `projects.jobs.aggregated`. |
| <CopyableCode code="_projects_locations_jobs_list" /> | `EXEC` | <CopyableCode code="location, projectId" /> | List the jobs of a project. To list the jobs of a project in a region, we recommend using `projects.locations.jobs.list` with a [regional endpoint] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints). To list the all jobs across all regions, use `projects.jobs.aggregated`. Using `projects.jobs.list` is not recommended, because you can only get the list of jobs that are running in `us-central1`. `projects.locations.jobs.list` and `projects.jobs.list` support filtering the list of jobs by name. Filtering by name isn't supported by `projects.jobs.aggregated`. |
| <CopyableCode code="projects_jobs_aggregated" /> | `EXEC` | <CopyableCode code="projectId" /> | List the jobs of a project across all regions. **Note:** This method doesn't support filtering the list of jobs by name. |
| <CopyableCode code="projects_jobs_snapshot" /> | `EXEC` | <CopyableCode code="jobId, projectId" /> | Snapshot the state of a streaming job. |
| <CopyableCode code="projects_locations_jobs_snapshot" /> | `EXEC` | <CopyableCode code="jobId, location, projectId" /> | Snapshot the state of a streaming job. |
