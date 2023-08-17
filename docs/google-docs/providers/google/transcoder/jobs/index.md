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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | The resource name of the job. Format: `projects/&#123;project_number&#125;/locations/&#123;location&#125;/jobs/&#123;job&#125;` |
| `templateId` | `string` | Input only. Specify the `template_id` to use for populating `Job.config`. The default is `preset/web-hd`, which is the only supported preset. User defined JobTemplate: `&#123;job_template_id&#125;` |
| `labels` | `object` | The labels associated with this job. You can use these to organize and group your jobs. |
| `optimization` | `string` | Optional. The optimization strategy of the job. The default is `AUTODETECT`. |
| `outputUri` | `string` | Input only. Specify the `output_uri` to populate an empty `Job.config.output.uri` or `JobTemplate.config.output.uri` when using template. URI for the output file(s). For example, `gs://my-bucket/outputs/`. See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). |
| `batchModePriority` | `integer` | The processing priority of a batch job. This field can only be set for batch mode jobs. The default value is 0. This value cannot be negative. Higher values correspond to higher priorities for the job. |
| `mode` | `string` | The processing mode of the job. The default is `PROCESSING_MODE_INTERACTIVE`. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `startTime` | `string` | Output only. The time the transcoding started. |
| `inputUri` | `string` | Input only. Specify the `input_uri` to populate empty `uri` fields in each element of `Job.config.inputs` or `JobTemplate.config.inputs` when using template. URI of the media. Input files must be at least 5 seconds in duration and stored in Cloud Storage (for example, `gs://bucket/inputs/file.mp4`). See [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats). |
| `createTime` | `string` | Output only. The time the job was created. |
| `ttlAfterCompletionDays` | `integer` | Job time to live value in days, which will be effective after job completion. Job should be deleted automatically after the given TTL. Enter a value between 1 and 90. The default is 30. |
| `endTime` | `string` | Output only. The time the transcoding finished. |
| `state` | `string` | Output only. The current state of the job. |
| `config` | `object` | Job configuration |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobsId, locationsId, projectsId` | Returns the job data. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists jobs in the specified region. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a job in the specified region. |
| `delete` | `DELETE` | `jobsId, locationsId, projectsId` | Deletes a job. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists jobs in the specified region. |
