---
title: release_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - release_configs
  - dataform
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
<tr><td><b>Name</b></td><td><code>release_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataform.release_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The release config's name. |
| `codeCompilationConfig` | `object` | Configures various aspects of Dataform code compilation. |
| `cronSchedule` | `string` | Optional. Optional schedule (in cron format) for automatic creation of compilation results. |
| `gitCommitish` | `string` | Required. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` - a tag: `tag1` - a branch name: `branch1` |
| `recentScheduledReleaseRecords` | `array` | Output only. Records of the 10 most recent scheduled release attempts. Updated whenever automatic creation of a compilation result is triggered by cron_schedule. |
| `releaseCompilationResult` | `string` | Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is created from this release config, or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`. |
| `timeZone` | `string` | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_releaseConfigs_get` | `SELECT` | `locationsId, projectsId, releaseConfigsId, repositoriesId` | Fetches a single ReleaseConfig. |
| `projects_locations_repositories_releaseConfigs_list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists ReleaseConfigs in a given Repository. |
| `projects_locations_repositories_releaseConfigs_create` | `INSERT` | `locationsId, projectsId, repositoriesId` | Creates a new ReleaseConfig in a given Repository. |
| `projects_locations_repositories_releaseConfigs_delete` | `DELETE` | `locationsId, projectsId, releaseConfigsId, repositoriesId` | Deletes a single ReleaseConfig. |
| `projects_locations_repositories_releaseConfigs_patch` | `EXEC` | `locationsId, projectsId, releaseConfigsId, repositoriesId` | Updates a single ReleaseConfig. |
