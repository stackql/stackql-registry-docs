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
| `name` | `string` | Resource name. |
| `createTime` | `string` | Output only. Creation timestamp. |
| `mimeType` | `string` | A content type specifier for the artifact. Content type specifiers are Media Types (https://en.wikipedia.org/wiki/Media_type) with a possible "schema" parameter that specifies a schema for the stored information. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip"). |
| `sizeBytes` | `integer` | Output only. The size of the artifact in bytes. If the artifact is gzipped, this is the size of the uncompressed artifact. |
| `updateTime` | `string` | Output only. Last update timestamp. |
| `labels` | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "registry.googleapis.com/" and cannot be changed. |
| `hash` | `string` | Output only. A SHA-256 hash of the artifact's contents. If the artifact is gzipped, this is the hash of the uncompressed artifact. |
| `annotations` | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| `contents` | `string` | Input only. The contents of the artifact. Provided by API callers when artifacts are created or replaced. To access the contents of an artifact, use GetArtifactContents. |
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
| `_projects_locations_apis_artifacts_list` | `EXEC` | `apisId, locationsId, projectsId` | Returns matching artifacts. |
| `_projects_locations_apis_deployments_artifacts_list` | `EXEC` | `apisId, deploymentsId, locationsId, projectsId` | Returns matching artifacts. |
| `_projects_locations_apis_versions_artifacts_list` | `EXEC` | `apisId, locationsId, projectsId, versionsId` | Returns matching artifacts. |
| `_projects_locations_apis_versions_specs_artifacts_list` | `EXEC` | `apisId, locationsId, projectsId, specsId, versionsId` | Returns matching artifacts. |
| `_projects_locations_artifacts_list` | `EXEC` | `locationsId, projectsId` | Returns matching artifacts. |
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
