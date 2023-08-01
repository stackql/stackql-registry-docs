---
title: builds
hide_title: false
hide_table_of_contents: false
keywords:
  - builds
  - cloudbuild
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
<tr><td><b>Name</b></td><td><code>builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.builds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `builds` | `array` | Builds will be sorted by `create_time`, descending. |
| `nextPageToken` | `string` | Token to receive the next page of results. This will be absent if the end of the response list has been reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_builds_list` | `SELECT` | `projectId` | Lists previously requested builds. Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully. |
| `projects_locations_builds_list` | `SELECT` | `locationsId, projectsId` | Lists previously requested builds. Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully. |
| `projects_builds_create` | `INSERT` | `projectId` | Starts a build with the specified configuration. This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`). |
| `projects_locations_builds_create` | `INSERT` | `locationsId, projectsId` | Starts a build with the specified configuration. This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`). |
| `projects_builds_approve` | `EXEC` | `buildsId, projectsId` | Approves or rejects a pending build. If approved, the returned LRO will be analogous to the LRO returned from a CreateBuild call. If rejected, the returned LRO will be immediately done. |
| `projects_builds_cancel` | `EXEC` | `id, projectId` | Cancels a build in progress. |
| `projects_builds_get` | `EXEC` | `id, projectId` | Returns information about a previously requested build. The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information. |
| `projects_builds_retry` | `EXEC` | `id, projectId` | Creates a new build based on the specified build. This method creates a new build using the original build request, which may or may not result in an identical build. For triggered builds: * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. For non-triggered builds that specify `RepoSource`: * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. * If the original build specified a commit sha or revision ID, the retried build will use the identical source. For builds that specify `StorageSource`: * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. |
| `projects_locations_builds_approve` | `EXEC` | `buildsId, locationsId, projectsId` | Approves or rejects a pending build. If approved, the returned LRO will be analogous to the LRO returned from a CreateBuild call. If rejected, the returned LRO will be immediately done. |
| `projects_locations_builds_cancel` | `EXEC` | `buildsId, locationsId, projectsId` | Cancels a build in progress. |
| `projects_locations_builds_get` | `EXEC` | `buildsId, locationsId, projectsId` | Returns information about a previously requested build. The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information. |
| `projects_locations_builds_retry` | `EXEC` | `buildsId, locationsId, projectsId` | Creates a new build based on the specified build. This method creates a new build using the original build request, which may or may not result in an identical build. For triggered builds: * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. For non-triggered builds that specify `RepoSource`: * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. * If the original build specified a commit sha or revision ID, the retried build will use the identical source. For builds that specify `StorageSource`: * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. |
