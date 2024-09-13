
---
title: revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions
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

Creates, updates, deletes or gets an <code>revision</code> resource or lists <code>revisions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.config.revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Revision name. Format: `projects/{project}/locations/{location}/deployments/{deployment}/ revisions/{revision}` |
| <CopyableCode code="action" /> | `string` | Output only. The action which created this revision |
| <CopyableCode code="applyResults" /> | `object` | Outputs and artifacts from applying a deployment. |
| <CopyableCode code="build" /> | `string` | Output only. Cloud Build instance UUID associated with this revision. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the revision was created. |
| <CopyableCode code="errorCode" /> | `string` | Output only. Code describing any errors that may have occurred. |
| <CopyableCode code="errorLogs" /> | `string` | Output only. Location of Terraform error logs in Google Cloud Storage. Format: `gs://{bucket}/{object}`. |
| <CopyableCode code="importExistingResources" /> | `boolean` | Output only. By default, Infra Manager will return a failure when Terraform encounters a 409 code (resource conflict error) during actuation. If this flag is set to true, Infra Manager will instead attempt to automatically import the resource into the Terraform state (for supported resource types) and continue actuation. Not all resource types are supported, refer to documentation. |
| <CopyableCode code="logs" /> | `string` | Output only. Location of Revision operation logs in `gs://{bucket}/{object}` format. |
| <CopyableCode code="quotaValidation" /> | `string` | Optional. Input to control quota checks for resources in terraform configuration files. There are limited resources on which quota validation applies. |
| <CopyableCode code="quotaValidationResults" /> | `string` | Output only. Cloud Storage path containing quota validation results. This field is set when a user sets Deployment.quota_validation field to ENABLED or ENFORCED. Format: `gs://{bucket}/{object}`. |
| <CopyableCode code="serviceAccount" /> | `string` | Output only. User-specified Service Account (SA) to be used as credential to manage resources. Format: `projects/{projectID}/serviceAccounts/{serviceAccount}` |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the revision. |
| <CopyableCode code="stateDetail" /> | `string` | Output only. Additional info regarding the current state. |
| <CopyableCode code="terraformBlueprint" /> | `object` | TerraformBlueprint describes the source of a Terraform root module which describes the resources and configs to be deployed. |
| <CopyableCode code="tfErrors" /> | `array` | Output only. Errors encountered when creating or updating this deployment. Errors are truncated to 10 entries, see `delete_results` and `error_logs` for full details. |
| <CopyableCode code="tfVersion" /> | `string` | Output only. The version of Terraform used to create the Revision. It is in the format of "Major.Minor.Patch", for example, "1.3.10". |
| <CopyableCode code="tfVersionConstraint" /> | `string` | Output only. The user-specified Terraform version constraint. Example: "=1.3.10". |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the revision was last modified. |
| <CopyableCode code="workerPool" /> | `string` | Output only. The user-specified Cloud Build worker pool resource in which the Cloud Build job will execute. Format: `projects/{project}/locations/{location}/workerPools/{workerPoolId}`. If this field is unspecified, the default Cloud Build worker pool will be used. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentsId, locationsId, projectsId, revisionsId" /> | Gets details about a Revision. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deploymentsId, locationsId, projectsId" /> | Lists Revisions of a deployment. |
| <CopyableCode code="export_state" /> | `EXEC` | <CopyableCode code="deploymentsId, locationsId, projectsId, revisionsId" /> | Exports Terraform state file from a given revision. |

## `SELECT` examples

Lists Revisions of a deployment.

```sql
SELECT
name,
action,
applyResults,
build,
createTime,
errorCode,
errorLogs,
importExistingResources,
logs,
quotaValidation,
quotaValidationResults,
serviceAccount,
state,
stateDetail,
terraformBlueprint,
tfErrors,
tfVersion,
tfVersionConstraint,
updateTime,
workerPool
FROM google.config.revisions
WHERE deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
