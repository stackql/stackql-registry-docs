---
title: service_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - service_accounts
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

Creates, updates, deletes, gets or lists a <code>service_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.service_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the service account. Use one of the following formats: * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS}` * `projects/{PROJECT_ID}/serviceAccounts/{UNIQUE_ID}` As an alternative, you can use the `-` wildcard character instead of the project ID: * `projects/-/serviceAccounts/{EMAIL_ADDRESS}` * `projects/-/serviceAccounts/{UNIQUE_ID}` When possible, avoid using the `-` wildcard character, because it can cause response messages to contain misleading error codes. For example, if you try to access the service account `projects/-/serviceAccounts/fake@example.com`, which does not exist, the response contains an HTTP `403 Forbidden` error instead of a `404 Not Found` error. |
| <CopyableCode code="description" /> | `string` | Optional. A user-specified, human-readable description of the service account. The maximum length is 256 UTF-8 bytes. |
| <CopyableCode code="disabled" /> | `boolean` | Output only. Whether the service account is disabled. |
| <CopyableCode code="displayName" /> | `string` | Optional. A user-specified, human-readable name for the service account. The maximum length is 100 UTF-8 bytes. |
| <CopyableCode code="email" /> | `string` | Output only. The email address of the service account. |
| <CopyableCode code="etag" /> | `string` | Deprecated. Do not use. |
| <CopyableCode code="oauth2ClientId" /> | `string` | Output only. The OAuth 2.0 client ID for the service account. |
| <CopyableCode code="projectId" /> | `string` | Output only. The ID of the project that owns the service account. |
| <CopyableCode code="uniqueId" /> | `string` | Output only. The unique, stable numeric ID for the service account. Each service account retains its unique ID even if you delete the service account. For example, if you delete a service account, then create a new service account with the same name, the new service account has a different unique ID than the deleted service account. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectsId, serviceAccountsId" /> | Gets a ServiceAccount. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists every ServiceAccount that belongs to a specific project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a ServiceAccount. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectsId, serviceAccountsId" /> | Deletes a ServiceAccount. **Warning:** After you delete a service account, you might not be able to undelete it. If you know that you need to re-enable the service account in the future, use DisableServiceAccount instead. If you delete a service account, IAM permanently removes the service account 30 days later. Google Cloud cannot recover the service account after it is permanently removed, even if you file a support request. To help avoid unplanned outages, we recommend that you disable the service account before you delete it. Use DisableServiceAccount to disable the service account, then wait at least 24 hours and watch for unintended consequences. If there are no unintended consequences, you can delete the service account. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="projectsId, serviceAccountsId" /> | Patches a ServiceAccount. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Disables a ServiceAccount immediately. If an application uses the service account to authenticate, that application can no longer call Google APIs or access Google Cloud resources. Existing access tokens for the service account are rejected, and requests for new access tokens will fail. To re-enable the service account, use EnableServiceAccount. After you re-enable the service account, its existing access tokens will be accepted, and you can request new access tokens. To help avoid unplanned outages, we recommend that you disable the service account before you delete it. Use this method to disable the service account, then wait at least 24 hours and watch for unintended consequences. If there are no unintended consequences, you can delete the service account with DeleteServiceAccount. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Enables a ServiceAccount that was disabled by DisableServiceAccount. If the service account is already enabled, then this method has no effect. If the service account was disabled by other means—for example, if Google disabled the service account because it was compromised—you cannot use this method to enable the service account. |
| <CopyableCode code="sign_blob" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | **Note:** This method is deprecated. Use the [signBlob](https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signBlob) method in the IAM Service Account Credentials API instead. If you currently use this method, see the [migration guide](https://cloud.google.com/iam/help/credentials/migrate-api) for instructions. Signs a blob using the system-managed private key for a ServiceAccount. |
| <CopyableCode code="sign_jwt" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | **Note:** This method is deprecated. Use the [signJwt](https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signJwt) method in the IAM Service Account Credentials API instead. If you currently use this method, see the [migration guide](https://cloud.google.com/iam/help/credentials/migrate-api) for instructions. Signs a JSON Web Token (JWT) using the system-managed private key for a ServiceAccount. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | Restores a deleted ServiceAccount. **Important:** It is not always possible to restore a deleted service account. Use this method only as a last resort. After you delete a service account, IAM permanently removes the service account 30 days later. There is no way to restore a deleted service account that has been permanently removed. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="projectsId, serviceAccountsId" /> | **Note:** We are in the process of deprecating this method. Use PatchServiceAccount instead. Updates a ServiceAccount. You can update only the `display_name` field. |

## `SELECT` examples

Lists every ServiceAccount that belongs to a specific project.

```sql
SELECT
name,
description,
disabled,
displayName,
email,
etag,
oauth2ClientId,
projectId,
uniqueId
FROM google.iam.service_accounts
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_accounts</code> resource.

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
INSERT INTO google.iam.service_accounts (
projectsId,
accountId,
serviceAccount
)
SELECT 
'{{ projectsId }}',
'{{ accountId }}',
'{{ serviceAccount }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: accountId
        value: '{{ accountId }}'
      - name: serviceAccount
        value: '{{ serviceAccount }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>service_accounts</code> resource.

```sql
/*+ update */
UPDATE google.iam.service_accounts
SET 
serviceAccount = '{{ serviceAccount }}',
updateMask = '{{ updateMask }}'
WHERE 
projectsId = '{{ projectsId }}'
AND serviceAccountsId = '{{ serviceAccountsId }}';
```

## `DELETE` example

Deletes the specified <code>service_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.service_accounts
WHERE projectsId = '{{ projectsId }}'
AND serviceAccountsId = '{{ serviceAccountsId }}';
```
