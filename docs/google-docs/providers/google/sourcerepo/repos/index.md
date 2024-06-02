---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
  - sourcerepo
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sourcerepo.repos" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the repository, of the form `projects//repos/`. The repo name may contain slashes. eg, `projects/myproject/repos/name/with/slash` |
| <CopyableCode code="mirrorConfig" /> | `object` | Configuration to automatically mirror a repository from another hosting service, for example GitHub or Bitbucket. |
| <CopyableCode code="pubsubConfigs" /> | `object` | How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names. |
| <CopyableCode code="size" /> | `string` | The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo. |
| <CopyableCode code="url" /> | `string` | URL to clone the repository from Google Cloud Source Repositories. Read-only field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectsId, reposId" /> | Returns information about a repo. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns all repos belonging to a project. The sizes of the repos are not set by ListRepos. To get the size of a repo, use GetRepo. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a repo in the given project with the given name. If the named repository already exists, `CreateRepo` returns `ALREADY_EXISTS`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectsId, reposId" /> | Deletes a repo. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Returns all repos belonging to a project. The sizes of the repos are not set by ListRepos. To get the size of a repo, use GetRepo. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="projectsId, reposId" /> | Updates information about a repo. |
| <CopyableCode code="sync" /> | `EXEC` | <CopyableCode code="projectsId, reposId" /> | Synchronize a connected repo. The response contains SyncRepoMetadata in the metadata field. |
