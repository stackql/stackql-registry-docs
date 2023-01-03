---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - transcoder
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
<tr><td><b>Id</b></td><td><code>google.transcoder.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the job. Format: `projects/{project_number}/locations/{location}/jobs/{job}` |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `templateId` | `string` | Input only. Specify the `template_id` to use for populating `Job.config`. The default is `preset/web-hd`. Preset Transcoder templates: - `preset/{preset_id}` - User defined JobTemplate: `{job_template_id}` |
| `endTime` | `string` | Output only. The time the transcoding finished. |
| `state` | `string` | Output only. The current state of the job. |
| `createTime` | `string` | Output only. The time the job was created. |
| `labels` | `object` | The labels associated with this job. You can use these to organize and group your jobs. |
| `ttlAfterCompletionDays` | `integer` | Job time to live value in days, which will be effective after job completion. Job should be deleted automatically after the given TTL. Enter a value between 1 and 90. The default is 30. |
| `config` | `object` | Job configuration |
| `inputUri` | `string` | Input only. Specify the `input_uri` to populate empty `uri` fields in each element of `Job.config.inputs` or `JobTemplate.config.inputs` when using template. URI of the media. Input files must be at least 5 seconds in duration and stored in Cloud Storage (for example, `gs://bucket/inputs/file.mp4`). See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). |
| `outputUri` | `string` | Input only. Specify the `output_uri` to populate an empty `Job.config.output.uri` or `JobTemplate.config.output.uri` when using template. URI for the output file(s). For example, `gs://my-bucket/outputs/`. See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). |
| `startTime` | `string` | Output only. The time the transcoding started. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_get` | `SELECT` | `jobsId, locationsId, projectsId` | Returns the job data. |
| `projects_locations_jobs_list` | `SELECT` | `locationsId, projectsId` | Lists jobs in the specified region. |
| `projects_locations_jobs_create` | `INSERT` | `locationsId, projectsId` | Creates a job in the specified region. |
| `projects_locations_jobs_delete` | `DELETE` | `jobsId, locationsId, projectsId` | Deletes a job. |
