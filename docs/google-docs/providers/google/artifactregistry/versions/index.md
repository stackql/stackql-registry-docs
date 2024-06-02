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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="artifactregistry.versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the version, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/art1". If the package or version ID parts contain slashes, the slashes are escaped. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the version, as specified in its metadata. |
| <CopyableCode code="createTime" /> | `string` | The time when the version was created. |
| <CopyableCode code="metadata" /> | `object` | Output only. Repository-specific Metadata stored against this version. The fields returned are defined by the underlying repository-specific resource. Currently, the resources could be: DockerImage MavenArtifact |
| <CopyableCode code="relatedTags" /> | `array` | Output only. A list of related tags. Will contain up to 100 tags that reference this version. |
| <CopyableCode code="updateTime" /> | `string` | The time when the version was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId, versionsId" /> | Gets a version |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Lists versions. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId, versionsId" /> | Deletes a version and all of its content. The returned operation will complete once the version has been deleted. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Lists versions. |
| <CopyableCode code="batch_delete" /> | `EXEC` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Deletes multiple versions across a repository. The returned operation will complete once the versions have been deleted. |
