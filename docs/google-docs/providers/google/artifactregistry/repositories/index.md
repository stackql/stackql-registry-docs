---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
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
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the repository, for example: "projects/p1/locations/us-central1/repositories/repo1". |
| <CopyableCode code="description" /> | `string` | The user-provided description of the repository. |
| <CopyableCode code="cleanupPolicies" /> | `object` | Optional. Cleanup policies for this repository. Cleanup policies indicate when certain package versions can be automatically deleted. Map keys are policy IDs supplied by users during policy creation. They must unique within a repository and be under 128 characters in length. |
| <CopyableCode code="cleanupPolicyDryRun" /> | `boolean` | Optional. If true, the cleanup pipeline is prevented from deleting versions in this repository. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the repository was created. |
| <CopyableCode code="dockerConfig" /> | `object` | DockerRepositoryConfig is docker related repository details. Provides additional configuration details for repositories of the docker format type. |
| <CopyableCode code="format" /> | `string` | The format of packages that are stored in the repository. |
| <CopyableCode code="kmsKeyName" /> | `string` | The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created. |
| <CopyableCode code="labels" /> | `object` | Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes. |
| <CopyableCode code="mavenConfig" /> | `object` | MavenRepositoryConfig is maven related repository details. Provides additional configuration details for repositories of the maven format type. |
| <CopyableCode code="mode" /> | `string` | The mode of the repository. |
| <CopyableCode code="remoteRepositoryConfig" /> | `object` | Remote repository configuration. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. If set, the repository satisfies physical zone separation. |
| <CopyableCode code="sbomConfig" /> | `object` | Config for whether to generate SBOMs for resources in this repository, as well as output fields describing current state. |
| <CopyableCode code="sizeBytes" /> | `string` | Output only. The size, in bytes, of all artifact storage in this repository. Repositories that are generally available or in public preview use this to calculate storage costs. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the repository was last updated. |
| <CopyableCode code="virtualRepositoryConfig" /> | `object` | Virtual repository configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Gets a repository. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists repositories. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists repositories. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Updates a repository. |
