---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - artifactregistry
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
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token to retrieve the next page of versions, or empty if there are no more versions to return. |
| `versions` | `array` | The versions returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, packagesId, projectsId, repositoriesId, versionsId` | Gets a version |
| `list` | `SELECT` | `locationsId, packagesId, projectsId, repositoriesId` | Lists versions. |
| `delete` | `DELETE` | `locationsId, packagesId, projectsId, repositoriesId, versionsId` | Deletes a version and all of its content. The returned operation will complete once the version has been deleted. |
| `batch_delete` | `EXEC` | `locationsId, packagesId, projectsId, repositoriesId` | Deletes multiple versions across a repository. The returned operation will complete once the versions have been deleted. |
