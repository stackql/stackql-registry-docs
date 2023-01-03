---
title: npm_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - npm_packages
  - artifactregistry
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
<tr><td><b>Name</b></td><td><code>npm_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.npm_packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. registry_location, project_id, repository_name and npm_package forms a unique package For example, "projects/test-project/locations/us-west4/repositories/test-repo/npmPackages/ npm_test:1.0.0", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and npm_test:1.0.0" is the npm package. |
| `packageName` | `string` | Package for the artifact. |
| `tags` | `array` | Tags attached to this package. |
| `updateTime` | `string` | Output only. Time the package was updated. |
| `version` | `string` | Version of this package. |
| `createTime` | `string` | Output only. Time the package was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_npmPackages_get` | `SELECT` | `locationsId, npmPackagesId, projectsId, repositoriesId` | Gets a npm package. |
| `projects_locations_repositories_npmPackages_list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists npm packages. |
