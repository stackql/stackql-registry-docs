---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
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
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the package, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1". If the package ID part contains slashes, the slashes are escaped. |
| `updateTime` | `string` | The time when the package was last updated. This includes publishing a new version of the package. |
| `createTime` | `string` | The time when the package was created. |
| `displayName` | `string` | The display name of the package. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_packages_get` | `SELECT` | `locationsId, packagesId, projectsId, repositoriesId` | Gets a package. |
| `projects_locations_repositories_packages_list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists packages. |
| `projects_locations_repositories_packages_delete` | `DELETE` | `locationsId, packagesId, projectsId, repositoriesId` | Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted. |
