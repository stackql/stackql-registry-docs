---
title: evaluation_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluation_jobs
  - datalabeling
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
<tr><td><b>Name</b></td><td><code>evaluation_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datalabeling.evaluation_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. After you create a job, Data Labeling Service assigns a name to the job with the following format: "projects/&#123;project_id&#125;/evaluationJobs/ &#123;evaluation_job_id&#125;" |
| <CopyableCode code="description" /> | `string` | Required. Description of the job. The description can be up to 25,000 characters long. |
| <CopyableCode code="annotationSpecSet" /> | `string` | Required. Name of the AnnotationSpecSet describing all the labels that your machine learning model outputs. You must create this resource before you create an evaluation job and provide its name in the following format: "projects/&#123;project_id&#125;/annotationSpecSets/&#123;annotation_spec_set_id&#125;" |
| <CopyableCode code="attempts" /> | `array` | Output only. Every time the evaluation job runs and an error occurs, the failed attempt is appended to this array. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp of when this evaluation job was created. |
| <CopyableCode code="evaluationJobConfig" /> | `object` | Configures specific details of how a continuous evaluation job works. Provide this configuration when you create an EvaluationJob. |
| <CopyableCode code="labelMissingGroundTruth" /> | `boolean` | Required. Whether you want Data Labeling Service to provide ground truth labels for prediction input. If you want the service to assign human labelers to annotate your data, set this to `true`. If you want to provide your own ground truth labels in the evaluation job's BigQuery table, set this to `false`. |
| <CopyableCode code="modelVersion" /> | `string` | Required. The [AI Platform Prediction model version](/ml-engine/docs/prediction-overview) to be evaluated. Prediction input and output is sampled from this model version. When creating an evaluation job, specify the model version in the following format: "projects/&#123;project_id&#125;/models/&#123;model_name&#125;/versions/&#123;version_name&#125;" There can only be one evaluation job per model version. |
| <CopyableCode code="schedule" /> | `string` | Required. Describes the interval at which the job runs. This interval must be at least 1 day, and it is rounded to the nearest day. For example, if you specify a 50-hour interval, the job runs every 2 days. You can provide the schedule in [crontab format](/scheduler/docs/configuring/cron-job-schedules) or in an [English-like format](/appengine/docs/standard/python/config/cronref#schedule_format). Regardless of what you specify, the job will run at 10:00 AM UTC. Only the interval from this schedule is used, not the specific time of day. |
| <CopyableCode code="state" /> | `string` | Output only. Describes the current state of the job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_evaluation_jobs_get" /> | `SELECT` | <CopyableCode code="evaluationJobsId, projectsId" /> | Gets an evaluation job by resource name. |
| <CopyableCode code="projects_evaluation_jobs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all evaluation jobs within a project with possible filters. Pagination is supported. |
| <CopyableCode code="projects_evaluation_jobs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an evaluation job. |
| <CopyableCode code="projects_evaluation_jobs_delete" /> | `DELETE` | <CopyableCode code="evaluationJobsId, projectsId" /> | Stops and deletes an evaluation job. |
| <CopyableCode code="_projects_evaluation_jobs_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists all evaluation jobs within a project with possible filters. Pagination is supported. |
| <CopyableCode code="projects_evaluation_jobs_patch" /> | `EXEC` | <CopyableCode code="evaluationJobsId, projectsId" /> | Updates an evaluation job. You can only update certain fields of the job's EvaluationJobConfig: `humanAnnotationConfig.instruction`, `exampleCount`, and `exampleSamplePercentage`. If you want to change any other aspect of the evaluation job, you must delete the job and create a new one. |
| <CopyableCode code="projects_evaluation_jobs_pause" /> | `EXEC` | <CopyableCode code="evaluationJobsId, projectsId" /> | Pauses an evaluation job. Pausing an evaluation job that is already in a `PAUSED` state is a no-op. |
| <CopyableCode code="projects_evaluation_jobs_resume" /> | `EXEC` | <CopyableCode code="evaluationJobsId, projectsId" /> | Resumes a paused evaluation job. A deleted evaluation job can't be resumed. Resuming a running or scheduled evaluation job is a no-op. |
