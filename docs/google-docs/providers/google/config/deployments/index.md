---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.config.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the deployment. Format: `projects/{project}/locations/{location}/deployments/{deployment}` |
| <CopyableCode code="annotations" /> | `object` | Optional. Arbitrary key-value metadata storage e.g. to help client tools identify deployments during automation. See https://google.aip.dev/148#annotations for details on format and size limitations. |
| <CopyableCode code="artifactsGcsBucket" /> | `string` | Optional. User-defined location of Cloud Build logs and artifacts in Google Cloud Storage. Format: `gs://{bucket}/{folder}` A default bucket will be bootstrapped if the field is not set or empty. Default bucket format: `gs://--blueprint-config` Constraints: - The bucket needs to be in the same project as the deployment - The path cannot be within the path of `gcs_source` - The field cannot be updated, including changing its presence |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the deployment was created. |
| <CopyableCode code="deleteBuild" /> | `string` | Output only. Cloud Build instance UUID associated with deleting this deployment. |
| <CopyableCode code="deleteLogs" /> | `string` | Output only. Location of Cloud Build logs in Google Cloud Storage, populated when deleting this deployment. Format: `gs://{bucket}/{object}`. |
| <CopyableCode code="deleteResults" /> | `object` | Outputs and artifacts from applying a deployment. |
| <CopyableCode code="errorCode" /> | `string` | Output only. Error code describing errors that may have occurred. |
| <CopyableCode code="errorLogs" /> | `string` | Output only. Location of Terraform error logs in Google Cloud Storage. Format: `gs://{bucket}/{object}`. |
| <CopyableCode code="importExistingResources" /> | `boolean` | By default, Infra Manager will return a failure when Terraform encounters a 409 code (resource conflict error) during actuation. If this flag is set to true, Infra Manager will instead attempt to automatically import the resource into the Terraform state (for supported resource types) and continue actuation. Not all resource types are supported, refer to documentation. |
| <CopyableCode code="labels" /> | `object` | User-defined metadata for the deployment. |
| <CopyableCode code="latestRevision" /> | `string` | Output only. Revision name that was most recently applied. Format: `projects/{project}/locations/{location}/deployments/{deployment}/ revisions/{revision}` |
| <CopyableCode code="lockState" /> | `string` | Output only. Current lock state of the deployment. |
| <CopyableCode code="quotaValidation" /> | `string` | Optional. Input to control quota checks for resources in terraform configuration files. There are limited resources on which quota validation applies. |
| <CopyableCode code="serviceAccount" /> | `string` | Optional. User-specified Service Account (SA) credentials to be used when actuating resources. Format: `projects/{projectID}/serviceAccounts/{serviceAccount}` |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the deployment. |
| <CopyableCode code="stateDetail" /> | `string` | Output only. Additional information regarding the current state. |
| <CopyableCode code="terraformBlueprint" /> | `object` | TerraformBlueprint describes the source of a Terraform root module which describes the resources and configs to be deployed. |
| <CopyableCode code="tfErrors" /> | `array` | Output only. Errors encountered when deleting this deployment. Errors are truncated to 10 entries, see `delete_results` and `error_logs` for full details. |
| <CopyableCode code="tfVersion" /> | `string` | Output only. The current Terraform version set on the deployment. It is in the format of "Major.Minor.Patch", for example, "1.3.10". |
| <CopyableCode code="tfVersionConstraint" /> | `string` | Optional. The user-specified Terraform version constraint. Example: "=1.3.10". |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the deployment was last modified. |
| <CopyableCode code="workerPool" /> | `string` | Optional. The user-specified Cloud Build worker pool resource in which the Cloud Build job will execute. Format: `projects/{project}/locations/{location}/workerPools/{workerPoolId}`. If this field is unspecified, the default Cloud Build worker pool will be used. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Gets details about a Deployment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Deployments in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Deployment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Deletes a Deployment. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Updates a Deployment. |
| <CopyableCode code="export_lock" /> | `EXEC` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Exports the lock info on a locked deployment. |
| <CopyableCode code="export_state" /> | `EXEC` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Exports Terraform state file from a given deployment. |
| <CopyableCode code="import_state" /> | `EXEC` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Imports Terraform state file in a given deployment. The state file does not take effect until the Deployment has been unlocked. |
| <CopyableCode code="lock" /> | `EXEC` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Locks a deployment. |
| <CopyableCode code="unlock" /> | `EXEC` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Unlocks a locked deployment. |

## `SELECT` examples

Lists Deployments in a given project and location.

```sql
SELECT
name,
annotations,
artifactsGcsBucket,
createTime,
deleteBuild,
deleteLogs,
deleteResults,
errorCode,
errorLogs,
importExistingResources,
labels,
latestRevision,
lockState,
quotaValidation,
serviceAccount,
state,
stateDetail,
terraformBlueprint,
tfErrors,
tfVersion,
tfVersionConstraint,
updateTime,
workerPool
FROM google.config.deployments
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

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
INSERT INTO google.config.deployments (
locationsId,
projectsId,
terraformBlueprint,
name,
labels,
artifactsGcsBucket,
serviceAccount,
importExistingResources,
workerPool,
tfVersionConstraint,
quotaValidation,
annotations
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ terraformBlueprint }}',
'{{ name }}',
'{{ labels }}',
'{{ artifactsGcsBucket }}',
'{{ serviceAccount }}',
{{ importExistingResources }},
'{{ workerPool }}',
'{{ tfVersionConstraint }}',
'{{ quotaValidation }}',
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
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: state
      value: string
    - name: latestRevision
      value: string
    - name: stateDetail
      value: string
    - name: errorCode
      value: string
    - name: deleteResults
      value:
        - name: content
          value: string
        - name: artifacts
          value: string
        - name: outputs
          value: object
    - name: deleteBuild
      value: string
    - name: deleteLogs
      value: string
    - name: tfErrors
      value:
        - - name: resourceAddress
            value: string
          - name: httpResponseCode
            value: integer
          - name: errorDescription
            value: string
          - name: error
            value:
              - name: code
                value: integer
              - name: message
                value: string
              - name: details
                value:
                  - object
    - name: errorLogs
      value: string
    - name: artifactsGcsBucket
      value: string
    - name: serviceAccount
      value: string
    - name: importExistingResources
      value: boolean
    - name: workerPool
      value: string
    - name: lockState
      value: string
    - name: tfVersionConstraint
      value: string
    - name: tfVersion
      value: string
    - name: quotaValidation
      value: string
    - name: annotations
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>deployments</code> resource.

```sql
/*+ update */
UPDATE google.config.deployments
SET 
terraformBlueprint = '{{ terraformBlueprint }}',
name = '{{ name }}',
labels = '{{ labels }}',
artifactsGcsBucket = '{{ artifactsGcsBucket }}',
serviceAccount = '{{ serviceAccount }}',
importExistingResources = true|false,
workerPool = '{{ workerPool }}',
tfVersionConstraint = '{{ tfVersionConstraint }}',
quotaValidation = '{{ quotaValidation }}',
annotations = '{{ annotations }}'
WHERE 
deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>deployments</code> resource.

```sql
/*+ delete */
DELETE FROM google.config.deployments
WHERE deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
