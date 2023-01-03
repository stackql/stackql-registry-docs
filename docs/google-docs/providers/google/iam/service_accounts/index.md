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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.service_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the service account. Use one of the following formats: * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS}` * `projects/{PROJECT_ID}/serviceAccounts/{UNIQUE_ID}` As an alternative, you can use the `-` wildcard character instead of the project ID: * `projects/-/serviceAccounts/{EMAIL_ADDRESS}` * `projects/-/serviceAccounts/{UNIQUE_ID}` When possible, avoid using the `-` wildcard character, because it can cause response messages to contain misleading error codes. For example, if you try to get the service account `projects/-/serviceAccounts/fake@example.com`, which does not exist, the response contains an HTTP `403 Forbidden` error instead of a `404 Not Found` error. |
| `description` | `string` | Optional. A user-specified, human-readable description of the service account. The maximum length is 256 UTF-8 bytes. |
| `etag` | `string` | Deprecated. Do not use. |
| `projectId` | `string` | Output only. The ID of the project that owns the service account. |
| `disabled` | `boolean` | Output only. Whether the service account is disabled. |
| `displayName` | `string` | Optional. A user-specified, human-readable name for the service account. The maximum length is 100 UTF-8 bytes. |
| `email` | `string` | Output only. The email address of the service account. |
| `oauth2ClientId` | `string` | Output only. The OAuth 2.0 client ID for the service account. |
| `uniqueId` | `string` | Output only. The unique, stable numeric ID for the service account. Each service account retains its unique ID even if you delete the service account. For example, if you delete a service account, then create a new service account with the same name, the new service account has a different unique ID than the deleted service account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_serviceAccounts_get` | `SELECT` | `projectsId, serviceAccountsId` | Gets a ServiceAccount. |
| `projects_serviceAccounts_list` | `SELECT` | `projectsId` | Lists every ServiceAccount that belongs to a specific project. |
| `projects_serviceAccounts_create` | `INSERT` | `projectsId` | Creates a ServiceAccount. |
| `projects_serviceAccounts_delete` | `DELETE` | `projectsId, serviceAccountsId` | Deletes a ServiceAccount. **Warning:** After you delete a service account, you might not be able to undelete it. If you know that you need to re-enable the service account in the future, use DisableServiceAccount instead. If you delete a service account, IAM permanently removes the service account 30 days later. Google Cloud cannot recover the service account after it is permanently removed, even if you file a support request. To help avoid unplanned outages, we recommend that you disable the service account before you delete it. Use DisableServiceAccount to disable the service account, then wait at least 24 hours and watch for unintended consequences. If there are no unintended consequences, you can delete the service account. |
| `projects_serviceAccounts_disable` | `EXEC` | `projectsId, serviceAccountsId` | Disables a ServiceAccount immediately. If an application uses the service account to authenticate, that application can no longer call Google APIs or access Google Cloud resources. Existing access tokens for the service account are rejected, and requests for new access tokens will fail. To re-enable the service account, use EnableServiceAccount. After you re-enable the service account, its existing access tokens will be accepted, and you can request new access tokens. To help avoid unplanned outages, we recommend that you disable the service account before you delete it. Use this method to disable the service account, then wait at least 24 hours and watch for unintended consequences. If there are no unintended consequences, you can delete the service account with DeleteServiceAccount. |
| `projects_serviceAccounts_enable` | `EXEC` | `projectsId, serviceAccountsId` | Enables a ServiceAccount that was disabled by DisableServiceAccount. If the service account is already enabled, then this method has no effect. If the service account was disabled by other means—for example, if Google disabled the service account because it was compromised—you cannot use this method to enable the service account. |
| `projects_serviceAccounts_patch` | `EXEC` | `projectsId, serviceAccountsId` | Patches a ServiceAccount. |
| `projects_serviceAccounts_signBlob` | `EXEC` | `projectsId, serviceAccountsId` | **Note:** This method is deprecated. Use the [`signBlob`](https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signBlob) method in the IAM Service Account Credentials API instead. If you currently use this method, see the [migration guide](https://cloud.google.com/iam/help/credentials/migrate-api) for instructions. Signs a blob using the system-managed private key for a ServiceAccount. |
| `projects_serviceAccounts_signJwt` | `EXEC` | `projectsId, serviceAccountsId` | **Note:** This method is deprecated. Use the [`signJwt`](https://cloud.google.com/iam/help/rest-credentials/v1/projects.serviceAccounts/signJwt) method in the IAM Service Account Credentials API instead. If you currently use this method, see the [migration guide](https://cloud.google.com/iam/help/credentials/migrate-api) for instructions. Signs a JSON Web Token (JWT) using the system-managed private key for a ServiceAccount. |
| `projects_serviceAccounts_undelete` | `EXEC` | `projectsId, serviceAccountsId` | Restores a deleted ServiceAccount. **Important:** It is not always possible to restore a deleted service account. Use this method only as a last resort. After you delete a service account, IAM permanently removes the service account 30 days later. There is no way to restore a deleted service account that has been permanently removed. |
| `projects_serviceAccounts_update` | `EXEC` | `projectsId, serviceAccountsId` | **Note:** We are in the process of deprecating this method. Use PatchServiceAccount instead. Updates a ServiceAccount. You can update only the `display_name` field. |
