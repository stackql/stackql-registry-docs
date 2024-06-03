---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the tag, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1". If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be URL encoded. |
| <CopyableCode code="version" /> | `string` | The name of the version the tag refers to, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811" If the package or version ID parts contain slashes, the slashes are escaped. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId, tagsId" /> | Gets a tag. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Lists tags. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Creates a tag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId, tagsId" /> | Deletes a tag. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId, tagsId" /> | Updates a tag. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Lists tags. |
