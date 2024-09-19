---
title: oauth_client_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - oauth_client_credentials
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

Creates, updates, deletes, gets or lists a <code>oauth_client_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oauth_client_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.oauth_client_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the OauthClientCredential. Format: `projects/{project}/locations/{location}/oauthClients/{oauth_client}/credentials/{credential}` |
| <CopyableCode code="clientSecret" /> | `string` | Output only. The system-generated OAuth client secret. The client secret must be stored securely. If the client secret is leaked, you must delete and re-create the client credential. To learn more, see [OAuth client and credential security risks and mitigations](https://cloud.google.com/iam/docs/workforce-oauth-app#security) |
| <CopyableCode code="disabled" /> | `boolean` | Optional. Whether the OauthClientCredential is disabled. You cannot use a disabled OauthClientCredential. |
| <CopyableCode code="displayName" /> | `string` | Optional. A user-specified display name of the OauthClientCredential. Cannot exceed 32 characters. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credentialsId, locationsId, oauthClientsId, projectsId" /> | Gets an individual OauthClientCredential. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, oauthClientsId, projectsId" /> | Lists all OauthClientCredentials in an OauthClient. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, oauthClientsId, projectsId" /> | Creates a new OauthClientCredential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialsId, locationsId, oauthClientsId, projectsId" /> | Deletes an OauthClientCredential. Before deleting an OauthClientCredential, it should first be disabled. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="credentialsId, locationsId, oauthClientsId, projectsId" /> | Updates an existing OauthClientCredential. |

## `SELECT` examples

Lists all OauthClientCredentials in an OauthClient.

```sql
SELECT
name,
clientSecret,
disabled,
displayName
FROM google.iam.oauth_client_credentials
WHERE locationsId = '{{ locationsId }}'
AND oauthClientsId = '{{ oauthClientsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>oauth_client_credentials</code> resource.

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
INSERT INTO google.iam.oauth_client_credentials (
locationsId,
oauthClientsId,
projectsId,
name,
disabled,
displayName
)
SELECT 
'{{ locationsId }}',
'{{ oauthClientsId }}',
'{{ projectsId }}',
'{{ name }}',
{{ disabled }},
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: disabled
      value: boolean
    - name: clientSecret
      value: string
    - name: displayName
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>oauth_client_credentials</code> resource.

```sql
/*+ update */
UPDATE google.iam.oauth_client_credentials
SET 
name = '{{ name }}',
disabled = true|false,
displayName = '{{ displayName }}'
WHERE 
credentialsId = '{{ credentialsId }}'
AND locationsId = '{{ locationsId }}'
AND oauthClientsId = '{{ oauthClientsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>oauth_client_credentials</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.oauth_client_credentials
WHERE credentialsId = '{{ credentialsId }}'
AND locationsId = '{{ locationsId }}'
AND oauthClientsId = '{{ oauthClientsId }}'
AND projectsId = '{{ projectsId }}';
```
