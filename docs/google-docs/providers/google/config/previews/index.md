---
title: previews
hide_title: false
hide_table_of_contents: false
keywords:
  - previews
  - config
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
<tr><td><b>Name</b></td><td><code>previews</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.config.previews" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the preview. Resource name can be user provided or server generated ID if unspecified. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/previews/&#123;preview&#125;` |
| <CopyableCode code="annotations" /> | `object` | Optional. Arbitrary key-value metadata storage e.g. to help client tools identifiy preview during automation. See https://google.aip.dev/148#annotations for details on format and size limitations. |
| <CopyableCode code="artifactsGcsBucket" /> | `string` | Optional. User-defined location of Cloud Build logs, artifacts, and in Google Cloud Storage. Format: `gs://&#123;bucket&#125;/&#123;folder&#125;` A default bucket will be bootstrapped if the field is not set or empty Default Bucket Format: `gs://--blueprint-config` Constraints: - The bucket needs to be in the same project as the deployment - The path cannot be within the path of `gcs_source` If omitted and deployment resource ref provided has artifacts_gcs_bucket defined, that artifact bucket is used. |
| <CopyableCode code="build" /> | `string` | Output only. Cloud Build instance UUID associated with this preview. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the preview was created. |
| <CopyableCode code="deployment" /> | `string` | Optional. Optional deployment reference. If specified, the preview will be performed using the provided deployment's current state and use any relevant fields from the deployment unless explicitly specified in the preview create request. |
| <CopyableCode code="errorCode" /> | `string` | Output only. Code describing any errors that may have occurred. |
| <CopyableCode code="errorLogs" /> | `string` | Output only. Link to tf-error.ndjson file, which contains the full list of the errors encountered during a Terraform preview. Format: `gs://&#123;bucket&#125;/&#123;object&#125;`. |
| <CopyableCode code="errorStatus" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the preview. |
| <CopyableCode code="logs" /> | `string` | Output only. Location of preview logs in `gs://&#123;bucket&#125;/&#123;object&#125;` format. |
| <CopyableCode code="previewArtifacts" /> | `object` | Artifacts created by preview. |
| <CopyableCode code="previewMode" /> | `string` | Optional. Current mode of preview. |
| <CopyableCode code="serviceAccount" /> | `string` | Optional. User-specified Service Account (SA) credentials to be used when previewing resources. Format: `projects/&#123;projectID&#125;/serviceAccounts/&#123;serviceAccount&#125;` |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the preview. |
| <CopyableCode code="terraformBlueprint" /> | `object` | TerraformBlueprint describes the source of a Terraform root module which describes the resources and configs to be deployed. |
| <CopyableCode code="tfErrors" /> | `array` | Output only. Summary of errors encountered during Terraform preview. It has a size limit of 10, i.e. only top 10 errors will be summarized here. |
| <CopyableCode code="tfVersion" /> | `string` | Output only. The current Terraform version set on the preview. It is in the format of "Major.Minor.Patch", for example, "1.3.10". |
| <CopyableCode code="tfVersionConstraint" /> | `string` | Optional. The user-specified Terraform version constraint. Example: "=1.3.10". |
| <CopyableCode code="workerPool" /> | `string` | Optional. The user-specified Worker Pool resource in which the Cloud Build job will execute. Format projects/&#123;project&#125;/locations/&#123;location&#125;/workerPools/&#123;workerPoolId&#125; If this field is unspecified, the default Cloud Build worker pool will be used. If omitted and deployment resource ref provided has worker_pool defined, that worker pool is used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, previewsId, projectsId" /> | Gets details about a Preview. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Previews in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Preview. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, previewsId, projectsId" /> | Deletes a Preview. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Previews in a given project and location. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="locationsId, previewsId, projectsId" /> | Export Preview results. |
