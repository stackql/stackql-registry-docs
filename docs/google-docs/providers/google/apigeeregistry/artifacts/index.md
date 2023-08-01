---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
  - apigeeregistry
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
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `artifacts` | `array` | The artifacts from the specified publisher. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_apis_artifacts_list` | `SELECT` | `apisId, locationsId, projectsId` | Returns matching artifacts. |
| `projects_locations_apis_deployments_artifacts_list` | `SELECT` | `apisId, deploymentsId, locationsId, projectsId` | Returns matching artifacts. |
| `projects_locations_apis_versions_artifacts_list` | `SELECT` | `apisId, locationsId, projectsId, versionsId` | Returns matching artifacts. |
| `projects_locations_apis_versions_specs_artifacts_list` | `SELECT` | `apisId, locationsId, projectsId, specsId, versionsId` | Returns matching artifacts. |
| `projects_locations_artifacts_list` | `SELECT` | `locationsId, projectsId` | Returns matching artifacts. |
| `projects_locations_apis_artifacts_create` | `INSERT` | `apisId, locationsId, projectsId` | Creates a specified artifact. |
| `projects_locations_apis_deployments_artifacts_create` | `INSERT` | `apisId, deploymentsId, locationsId, projectsId` | Creates a specified artifact. |
| `projects_locations_apis_versions_artifacts_create` | `INSERT` | `apisId, locationsId, projectsId, versionsId` | Creates a specified artifact. |
| `projects_locations_apis_versions_specs_artifacts_create` | `INSERT` | `apisId, locationsId, projectsId, specsId, versionsId` | Creates a specified artifact. |
| `projects_locations_artifacts_create` | `INSERT` | `locationsId, projectsId` | Creates a specified artifact. |
| `projects_locations_apis_artifacts_delete` | `DELETE` | `apisId, artifactsId, locationsId, projectsId` | Removes a specified artifact. |
| `projects_locations_apis_deployments_artifacts_delete` | `DELETE` | `apisId, artifactsId, deploymentsId, locationsId, projectsId` | Removes a specified artifact. |
| `projects_locations_apis_versions_artifacts_delete` | `DELETE` | `apisId, artifactsId, locationsId, projectsId, versionsId` | Removes a specified artifact. |
| `projects_locations_apis_versions_specs_artifacts_delete` | `DELETE` | `apisId, artifactsId, locationsId, projectsId, specsId, versionsId` | Removes a specified artifact. |
| `projects_locations_artifacts_delete` | `DELETE` | `artifactsId, locationsId, projectsId` | Removes a specified artifact. |
| `projects_locations_apis_artifacts_get` | `EXEC` | `apisId, artifactsId, locationsId, projectsId` | Returns a specified artifact. |
| `projects_locations_apis_artifacts_replace_artifact` | `EXEC` | `apisId, artifactsId, locationsId, projectsId` | Used to replace a specified artifact. |
| `projects_locations_apis_deployments_artifacts_get` | `EXEC` | `apisId, artifactsId, deploymentsId, locationsId, projectsId` | Returns a specified artifact. |
| `projects_locations_apis_deployments_artifacts_replace_artifact` | `EXEC` | `apisId, artifactsId, deploymentsId, locationsId, projectsId` | Used to replace a specified artifact. |
| `projects_locations_apis_versions_artifacts_get` | `EXEC` | `apisId, artifactsId, locationsId, projectsId, versionsId` | Returns a specified artifact. |
| `projects_locations_apis_versions_artifacts_replace_artifact` | `EXEC` | `apisId, artifactsId, locationsId, projectsId, versionsId` | Used to replace a specified artifact. |
| `projects_locations_apis_versions_specs_artifacts_get` | `EXEC` | `apisId, artifactsId, locationsId, projectsId, specsId, versionsId` | Returns a specified artifact. |
| `projects_locations_apis_versions_specs_artifacts_replace_artifact` | `EXEC` | `apisId, artifactsId, locationsId, projectsId, specsId, versionsId` | Used to replace a specified artifact. |
| `projects_locations_artifacts_get` | `EXEC` | `artifactsId, locationsId, projectsId` | Returns a specified artifact. |
| `projects_locations_artifacts_replace_artifact` | `EXEC` | `artifactsId, locationsId, projectsId` | Used to replace a specified artifact. |
