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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>previews</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>previews</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.config.previews" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the preview. Resource name can be user provided or server generated ID if unspecified. Format: `projects/{project}/locations/{location}/previews/{preview}` |
| <CopyableCode code="annotations" /> | `object` | Optional. Arbitrary key-value metadata storage e.g. to help client tools identifiy preview during automation. See https://google.aip.dev/148#annotations for details on format and size limitations. |
| <CopyableCode code="artifactsGcsBucket" /> | `string` | Optional. User-defined location of Cloud Build logs, artifacts, and in Google Cloud Storage. Format: `gs://{bucket}/{folder}` A default bucket will be bootstrapped if the field is not set or empty Default Bucket Format: `gs://--blueprint-config` Constraints: - The bucket needs to be in the same project as the deployment - The path cannot be within the path of `gcs_source` If omitted and deployment resource ref provided has artifacts_gcs_bucket defined, that artifact bucket is used. |
| <CopyableCode code="build" /> | `string` | Output only. Cloud Build instance UUID associated with this preview. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the preview was created. |
| <CopyableCode code="deployment" /> | `string` | Optional. Optional deployment reference. If specified, the preview will be performed using the provided deployment's current state and use any relevant fields from the deployment unless explicitly specified in the preview create request. |
| <CopyableCode code="errorCode" /> | `string` | Output only. Code describing any errors that may have occurred. |
| <CopyableCode code="errorLogs" /> | `string` | Output only. Link to tf-error.ndjson file, which contains the full list of the errors encountered during a Terraform preview. Format: `gs://{bucket}/{object}`. |
| <CopyableCode code="errorStatus" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the preview. |
| <CopyableCode code="logs" /> | `string` | Output only. Location of preview logs in `gs://{bucket}/{object}` format. |
| <CopyableCode code="previewArtifacts" /> | `object` | Artifacts created by preview. |
| <CopyableCode code="previewMode" /> | `string` | Optional. Current mode of preview. |
| <CopyableCode code="serviceAccount" /> | `string` | Optional. User-specified Service Account (SA) credentials to be used when previewing resources. Format: `projects/{projectID}/serviceAccounts/{serviceAccount}` |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the preview. |
| <CopyableCode code="terraformBlueprint" /> | `object` | TerraformBlueprint describes the source of a Terraform root module which describes the resources and configs to be deployed. |
| <CopyableCode code="tfErrors" /> | `array` | Output only. Summary of errors encountered during Terraform preview. It has a size limit of 10, i.e. only top 10 errors will be summarized here. |
| <CopyableCode code="tfVersion" /> | `string` | Output only. The current Terraform version set on the preview. It is in the format of "Major.Minor.Patch", for example, "1.3.10". |
| <CopyableCode code="tfVersionConstraint" /> | `string` | Optional. The user-specified Terraform version constraint. Example: "=1.3.10". |
| <CopyableCode code="workerPool" /> | `string` | Optional. The user-specified Worker Pool resource in which the Cloud Build job will execute. Format projects/{project}/locations/{location}/workerPools/{workerPoolId} If this field is unspecified, the default Cloud Build worker pool will be used. If omitted and deployment resource ref provided has worker_pool defined, that worker pool is used. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, previewsId, projectsId" /> | Gets details about a Preview. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Previews in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Preview. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, previewsId, projectsId" /> | Deletes a Preview. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="locationsId, previewsId, projectsId" /> | Export Preview results. |

## `SELECT` examples

Lists Previews in a given project and location.

```sql
SELECT
name,
annotations,
artifactsGcsBucket,
build,
createTime,
deployment,
errorCode,
errorLogs,
errorStatus,
labels,
logs,
previewArtifacts,
previewMode,
serviceAccount,
state,
terraformBlueprint,
tfErrors,
tfVersion,
tfVersionConstraint,
workerPool
FROM google.config.previews
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>previews</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.config.previews (
locationsId,
projectsId,
terraformBlueprint,
name,
labels,
deployment,
previewMode,
serviceAccount,
artifactsGcsBucket,
workerPool,
tfVersionConstraint,
annotations
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ terraformBlueprint }}',
'{{ name }}',
'{{ labels }}',
'{{ deployment }}',
'{{ previewMode }}',
'{{ serviceAccount }}',
'{{ artifactsGcsBucket }}',
'{{ workerPool }}',
'{{ tfVersionConstraint }}',
'{{ annotations }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: terraformBlueprint
      value:
        - name: gcsSource
          value: string
        - name: gitSource
          value:
            - name: repo
              value: string
            - name: directory
              value: string
            - name: ref
              value: string
        - name: inputValues
          value: object
    - name: name
      value: string
    - name: createTime
      value: string
    - name: labels
      value: object
    - name: state
      value: string
    - name: deployment
      value: string
    - name: previewMode
      value: string
    - name: serviceAccount
      value: string
    - name: artifactsGcsBucket
      value: string
    - name: workerPool
      value: string
    - name: errorCode
      value: string
    - name: errorStatus
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: build
      value: string
    - name: tfErrors
      value:
        - - name: resourceAddress
            value: string
          - name: httpResponseCode
            value: integer
          - name: errorDescription
            value: string
    - name: errorLogs
      value: string
    - name: previewArtifacts
      value:
        - name: content
          value: string
        - name: artifacts
          value: string
    - name: logs
      value: string
    - name: tfVersion
      value: string
    - name: tfVersionConstraint
      value: string
    - name: annotations
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>previews</code> resource.

```sql
/*+ delete */
DELETE FROM google.config.previews
WHERE locationsId = '{{ locationsId }}'
AND previewsId = '{{ previewsId }}'
AND projectsId = '{{ projectsId }}';
```
