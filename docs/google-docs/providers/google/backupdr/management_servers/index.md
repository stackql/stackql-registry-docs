---
title: management_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - management_servers
  - backupdr
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
<tr><td><b>Name</b></td><td><code>management_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="backupdr.management_servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name. |
| <CopyableCode code="description" /> | `string` | Optional. The description of the ManagementServer instance (2048 characters or less). |
| <CopyableCode code="baProxyUri" /> | `array` | Output only. The hostname or ip address of the exposed AGM endpoints, used by BAs to connect to BA proxy. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user provided metadata. Labels currently defined: 1. migrate_from_go= If set to true, the MS is created in migration ready mode. |
| <CopyableCode code="managementUri" /> | `object` | ManagementURI for the Management Server resource. |
| <CopyableCode code="networks" /> | `array` | Required. VPC networks to which the ManagementServer instance is connected. For this version, only a single network is supported. |
| <CopyableCode code="oauth2ClientId" /> | `string` | Output only. The OAuth 2.0 client id is required to make API calls to the BackupDR instance API of this ManagementServer. This is the value that should be provided in the ‘aud’ field of the OIDC ID Token (see openid specification https://openid.net/specs/openid-connect-core-1_0.html#IDToken). |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The ManagementServer state. |
| <CopyableCode code="type" /> | `string` | Optional. The type of the ManagementServer resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the instance was updated. |
| <CopyableCode code="workforceIdentityBasedManagementUri" /> | `object` | ManagementURI depending on the Workforce Identity i.e. either 1p or 3p. |
| <CopyableCode code="workforceIdentityBasedOauth2ClientId" /> | `object` | OAuth Client ID depending on the Workforce Identity i.e. either 1p or 3p, |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, managementServersId, projectsId" /> | Gets details of a single ManagementServer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ManagementServers in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ManagementServer in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, managementServersId, projectsId" /> | Deletes a single ManagementServer. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists ManagementServers in a given project and location. |
