---
title: folders_access_approval_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - folders_access_approval_settings
  - accessapproval
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
<tr><td><b>Name</b></td><td><code>folders_access_approval_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accessapproval.folders_access_approval_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the settings. Format is one of: * "projects/{project}/accessApprovalSettings" * "folders/{folder}/accessApprovalSettings" * "organizations/{organization}/accessApprovalSettings" |
| `notificationEmails` | `array` | A list of email addresses to which notifications relating to approval requests should be sent. Notifications relating to a resource will be sent to all emails in the settings of ancestor resources of that resource. A maximum of 50 email addresses are allowed. |
| `activeKeyVersion` | `string` | The asymmetric crypto key version to use for signing approval requests. Empty active_key_version indicates that a Google-managed key should be used for signing. This property will be ignored if set by an ancestor of this resource, and new non-empty values may not be set. |
| `ancestorHasActiveKeyVersion` | `boolean` | Output only. This field is read only (not settable via UpdateAccessApprovalSettings method). If the field is true, that indicates that an ancestor of this Project or Folder has set active_key_version (this field will always be unset for the organization since organizations do not have ancestors). |
| `enrolledAncestor` | `boolean` | Output only. This field is read only (not settable via UpdateAccessApprovalSettings method). If the field is true, that indicates that at least one service is enrolled for Access Approval in one or more ancestors of the Project or Folder (this field will always be unset for the organization since organizations do not have ancestors). |
| `enrolledServices` | `array` | A list of Google Cloud Services for which the given resource has Access Approval enrolled. Access requests for the resource given by name against any of these services contained here will be required to have explicit approval. If name refers to an organization, enrollment can be done for individual services. If name refers to a folder or project, enrollment can only be done on an all or nothing basis. If a cloud_product is repeated in this list, the first entry will be honored and all following entries will be discarded. A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded. |
| `invalidKeyVersion` | `boolean` | Output only. This field is read only (not settable via UpdateAccessApprovalSettings method). If the field is true, that indicates that there is some configuration issue with the active_key_version configured at this level in the resource hierarchy (e.g. it doesn't exist or the Access Approval service account doesn't have the correct permissions on it, etc.) This key version is not necessarily the effective key version at this level, as key versions are inherited top-down. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_getAccessApprovalSettings` | `SELECT` | `foldersId` | Gets the settings associated with a project, folder, or organization. |
| `folders_deleteAccessApprovalSettings` | `DELETE` | `foldersId` | Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited. |
