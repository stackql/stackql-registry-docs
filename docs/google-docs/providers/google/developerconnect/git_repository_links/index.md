---
title: git_repository_links
hide_title: false
hide_table_of_contents: false
keywords:
  - git_repository_links
  - developerconnect
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
<tr><td><b>Name</b></td><td><code>git_repository_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="developerconnect.git_repository_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the repository, in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. |
| <CopyableCode code="annotations" /> | `object` | Optional. Allows clients to store small amounts of arbitrary data. |
| <CopyableCode code="cloneUri" /> | `string` | Required. Git Clone URI. |
| <CopyableCode code="createTime" /> | `string` | Output only. [Output only] Create timestamp |
| <CopyableCode code="deleteTime" /> | `string` | Output only. [Output only] Delete timestamp |
| <CopyableCode code="etag" /> | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Set to true when the connection is being set up or updated in the background. |
| <CopyableCode code="uid" /> | `string` | Output only. A system-assigned unique identifier for a the GitRepositoryLink. |
| <CopyableCode code="updateTime" /> | `string` | Output only. [Output only] Update timestamp |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionsId, gitRepositoryLinksId, locationsId, projectsId" /> | Gets details of a single GitRepositoryLink. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Lists GitRepositoryLinks in a given project, location, and connection. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Creates a GitRepositoryLink. Upon linking a Git Repository, Developer Connect will configure the Git Repository to send webhook events to Developer Connect. Connections that use Firebase GitHub Application will have events forwarded to the Firebase service. All other Connections will have events forwarded to Cloud Build. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionsId, gitRepositoryLinksId, locationsId, projectsId" /> | Deletes a single GitRepositoryLink. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Lists GitRepositoryLinks in a given project, location, and connection. |
