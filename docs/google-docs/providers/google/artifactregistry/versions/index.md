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
| `name` | `string` | The name of the version, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/art1". If the package or version ID parts contain slashes, the slashes are escaped. |
| `description` | `string` | Optional. Description of the version, as specified in its metadata. |
| `createTime` | `string` | The time when the version was created. |
| `metadata` | `object` | Output only. Repository-specific Metadata stored against this version. The fields returned are defined by the underlying repository-specific resource. Currently, the resources could be: DockerImage MavenArtifact |
| `relatedTags` | `array` | Output only. A list of related tags. Will contain up to 100 tags that reference this version. |
| `updateTime` | `string` | The time when the version was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, packagesId, projectsId, repositoriesId, versionsId` | Gets a version |
| `list` | `SELECT` | `locationsId, packagesId, projectsId, repositoriesId` | Lists versions. |
| `delete` | `DELETE` | `locationsId, packagesId, projectsId, repositoriesId, versionsId` | Deletes a version and all of its content. The returned operation will complete once the version has been deleted. |
| `_list` | `EXEC` | `locationsId, packagesId, projectsId, repositoriesId` | Lists versions. |
| `batch_delete` | `EXEC` | `locationsId, packagesId, projectsId, repositoriesId` | Deletes multiple versions across a repository. The returned operation will complete once the versions have been deleted. |
