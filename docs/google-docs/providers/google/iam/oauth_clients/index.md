---
title: oauth_clients
hide_title: false
hide_table_of_contents: false
keywords:
  - oauth_clients
  - iam
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>oauth_clients</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oauth_clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.oauth_clients" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the OauthClient. Format:`projects/{project}/locations/{location}/oauthClients/{oauth_client}`. |
| <CopyableCode code="description" /> | `string` | Optional. A user-specified description of the OauthClient. Cannot exceed 256 characters. |
| <CopyableCode code="allowedGrantTypes" /> | `array` | Required. The list of OAuth grant types is allowed for the OauthClient. |
| <CopyableCode code="allowedRedirectUris" /> | `array` | Required. The list of redirect uris that is allowed to redirect back when authorization process is completed. |
| <CopyableCode code="allowedScopes" /> | `array` | Required. The list of scopes that the OauthClient is allowed to request during OAuth flows. The following scopes are supported: * `https://www.googleapis.com/auth/cloud-platform`: See, edit, configure, and delete your Google Cloud data and see the email address for your Google Account. |
| <CopyableCode code="clientId" /> | `string` | Output only. The system-generated OauthClient id. |
| <CopyableCode code="clientType" /> | `string` | Immutable. The type of OauthClient. Either public or private. For private clients, the client secret can be managed using the dedicated OauthClientCredential resource. |
| <CopyableCode code="disabled" /> | `boolean` | Optional. Whether the OauthClient is disabled. You cannot use a disabled OAuth client. |
| <CopyableCode code="displayName" /> | `string` | Optional. A user-specified display name of the OauthClient. Cannot exceed 32 characters. |
| <CopyableCode code="expireTime" /> | `string` | Output only. Time after which the OauthClient will be permanently purged and cannot be recovered. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the OauthClient. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, oauthClientsId, projectsId" /> | Gets an individual OauthClient. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all non-deleted OauthClients in a project. If `show_deleted` is set to `true`, then deleted OauthClients are also listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new OauthClient. You cannot reuse the name of a deleted OauthClient until 30 days after deletion. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, oauthClientsId, projectsId" /> | Deletes an OauthClient. You cannot use a deleted OauthClient. However, deletion does not revoke access tokens that have already been issued. They continue to grant access. Deletion does revoke refresh tokens that have already been issued. They cannot be used to renew an access token. If the OauthClient is undeleted, and the refresh tokens are not expired, they are valid for token exchange again. You can undelete an OauthClient for 30 days. After 30 days, deletion is permanent. You cannot update deleted OauthClients. However, you can view and list them. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, oauthClientsId, projectsId" /> | Updates an existing OauthClient. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="locationsId, oauthClientsId, projectsId" /> | Undeletes an OauthClient, as long as it was deleted fewer than 30 days ago. |

## `SELECT` examples

Lists all non-deleted OauthClients in a project. If `show_deleted` is set to `true`, then deleted OauthClients are also listed.

```sql
SELECT
name,
description,
allowedGrantTypes,
allowedRedirectUris,
allowedScopes,
clientId,
clientType,
disabled,
displayName,
expireTime,
state
FROM google.iam.oauth_clients
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>oauth_clients</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.iam.oauth_clients (
locationsId,
projectsId,
name,
disabled,
displayName,
description,
clientType,
allowedGrantTypes,
allowedScopes,
allowedRedirectUris
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
true|false,
'{{ displayName }}',
'{{ description }}',
'{{ clientType }}',
'{{ allowedGrantTypes }}',
'{{ allowedScopes }}',
'{{ allowedRedirectUris }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
state: string
disabled: boolean
clientId: string
displayName: string
description: string
clientType: string
allowedGrantTypes:
  - type: string
    enumDescriptions: string
    enum: string
allowedScopes:
  - type: string
allowedRedirectUris:
  - type: string
expireTime: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>oauth_clients</code> resource.

```sql
/*+ update */
UPDATE google.iam.oauth_clients
SET 
name = '{{ name }}',
disabled = true|false,
displayName = '{{ displayName }}',
description = '{{ description }}',
clientType = '{{ clientType }}',
allowedGrantTypes = '{{ allowedGrantTypes }}',
allowedScopes = '{{ allowedScopes }}',
allowedRedirectUris = '{{ allowedRedirectUris }}'
WHERE 
locationsId = '{{ locationsId }}'
AND oauthClientsId = '{{ oauthClientsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>oauth_clients</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.oauth_clients
WHERE locationsId = '{{ locationsId }}'
AND oauthClientsId = '{{ oauthClientsId }}'
AND projectsId = '{{ projectsId }}';
```
