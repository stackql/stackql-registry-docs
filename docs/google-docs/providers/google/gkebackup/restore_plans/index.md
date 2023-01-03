---
title: restore_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_plans
  - gkebackup
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
<tr><td><b>Name</b></td><td><code>restore_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.restore_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the RestorePlan resource. Format: projects/*/locations/*/restorePlans/*. |
| `description` | `string` | User specified descriptive string for this RestorePlan. |
| `cluster` | `string` | Required. Immutable. The target cluster into which Restores created via this RestorePlan will restore data. NOTE: the cluster's region must be the same as the RestorePlan. Valid formats: - projects/*/locations/*/clusters/* - projects/*/zones/*/clusters/* |
| `etag` | `string` | Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `GetRestorePlan`, and systems are expected to put that etag in the request to `UpdateRestorePlan` or `DeleteRestorePlan` to ensure that their change will be applied to the same version of the resource. |
| `createTime` | `string` | Output only. The timestamp when this RestorePlan resource was created. |
| `labels` | `object` | A set of custom labels supplied by user. |
| `restoreConfig` | `object` | Configuration of a restore. Next id: 9 |
| `updateTime` | `string` | Output only. The timestamp when this RestorePlan resource was last updated. |
| `backupPlan` | `string` | Required. Immutable. A reference to the BackupPlan from which Backups may be used as the source for Restores created via this RestorePlan. Format: projects/*/locations/*/backupPlans/*. |
| `uid` | `string` | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_restorePlans_get` | `SELECT` | `locationsId, projectsId, restorePlansId` | Retrieve the details of a single RestorePlan. |
| `projects_locations_restorePlans_list` | `SELECT` | `locationsId, projectsId` | Lists RestorePlans in a given location. |
| `projects_locations_restorePlans_create` | `INSERT` | `locationsId, projectsId` | Creates a new RestorePlan in a given location. |
| `projects_locations_restorePlans_delete` | `DELETE` | `locationsId, projectsId, restorePlansId` | Deletes an existing RestorePlan. |
| `projects_locations_restorePlans_patch` | `EXEC` | `locationsId, projectsId, restorePlansId` | Update a RestorePlan. |
