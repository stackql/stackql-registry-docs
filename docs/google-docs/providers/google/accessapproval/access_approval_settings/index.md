
---
title: access_approval_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - access_approval_settings
  - accessapproval
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

Creates, updates, deletes or gets an <code>access_approval_setting</code> resource or lists <code>access_approval_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_approval_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.accessapproval.access_approval_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the settings. Format is one of: * "projects/{project}/accessApprovalSettings" * "folders/{folder}/accessApprovalSettings" * "organizations/{organization}/accessApprovalSettings" |
| <CopyableCode code="activeKeyVersion" /> | `string` | The asymmetric crypto key version to use for signing approval requests. Empty active_key_version indicates that a Google-managed key should be used for signing. This property will be ignored if set by an ancestor of this resource, and new non-empty values may not be set. |
| <CopyableCode code="ancestorHasActiveKeyVersion" /> | `boolean` | Output only. This field is read only (not settable via UpdateAccessApprovalSettings method). If the field is true, that indicates that an ancestor of this Project or Folder has set active_key_version (this field will always be unset for the organization since organizations do not have ancestors). |
| <CopyableCode code="enrolledAncestor" /> | `boolean` | Output only. This field is read only (not settable via UpdateAccessApprovalSettings method). If the field is true, that indicates that at least one service is enrolled for Access Approval in one or more ancestors of the Project or Folder (this field will always be unset for the organization since organizations do not have ancestors). |
| <CopyableCode code="enrolledServices" /> | `array` | A list of Google Cloud Services for which the given resource has Access Approval enrolled. Access requests for the resource given by name against any of these services contained here will be required to have explicit approval. If name refers to an organization, enrollment can be done for individual services. If name refers to a folder or project, enrollment can only be done on an all or nothing basis. If a cloud_product is repeated in this list, the first entry will be honored and all following entries will be discarded. A maximum of 10 enrolled services will be enforced, to be expanded as the set of supported services is expanded. |
| <CopyableCode code="invalidKeyVersion" /> | `boolean` | Output only. This field is read only (not settable via UpdateAccessApprovalSettings method). If the field is true, that indicates that there is some configuration issue with the active_key_version configured at this level in the resource hierarchy (e.g. it doesn't exist or the Access Approval service account doesn't have the correct permissions on it, etc.) This key version is not necessarily the effective key version at this level, as key versions are inherited top-down. |
| <CopyableCode code="notificationEmails" /> | `array` | A list of email addresses to which notifications relating to approval requests should be sent. Notifications relating to a resource will be sent to all emails in the settings of ancestor resources of that resource. A maximum of 50 email addresses are allowed. |
| <CopyableCode code="notificationPubsubTopic" /> | `string` | Optional. A pubsub topic to which notifications relating to approval requests should be sent. |
| <CopyableCode code="preferNoBroadApprovalRequests" /> | `boolean` | This preference is communicated to Google personnel when sending an approval request but can be overridden if necessary. |
| <CopyableCode code="preferredRequestExpirationDays" /> | `integer` | This preference is shared with Google personnel, but can be overridden if said personnel deems necessary. The approver ultimately can set the expiration at approval time. |
| <CopyableCode code="requestScopeMaxWidthPreference" /> | `string` | Optional. A setting to indicate the maximum width of an Access Approval request. |
| <CopyableCode code="requireCustomerVisibleJustification" /> | `boolean` | Optional. A setting to require approval request justifications to be customer visible. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_get_access_approval_settings" /> | `SELECT` | <CopyableCode code="foldersId" /> | Gets the settings associated with a project, folder, or organization. |
| <CopyableCode code="organizations_get_access_approval_settings" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Gets the settings associated with a project, folder, or organization. |
| <CopyableCode code="projects_get_access_approval_settings" /> | `SELECT` | <CopyableCode code="projectsId" /> | Gets the settings associated with a project, folder, or organization. |
| <CopyableCode code="folders_delete_access_approval_settings" /> | `DELETE` | <CopyableCode code="foldersId" /> | Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited. |
| <CopyableCode code="organizations_delete_access_approval_settings" /> | `DELETE` | <CopyableCode code="organizationsId" /> | Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited. |
| <CopyableCode code="projects_delete_access_approval_settings" /> | `DELETE` | <CopyableCode code="projectsId" /> | Deletes the settings associated with a project, folder, or organization. This will have the effect of disabling Access Approval for the project, folder, or organization, but only if all ancestors also have Access Approval disabled. If Access Approval is enabled at a higher level of the hierarchy, then Access Approval will still be enabled at this level as the settings are inherited. |
| <CopyableCode code="folders_update_access_approval_settings" /> | `UPDATE` | <CopyableCode code="foldersId" /> | Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask. |
| <CopyableCode code="organizations_update_access_approval_settings" /> | `UPDATE` | <CopyableCode code="organizationsId" /> | Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask. |
| <CopyableCode code="projects_update_access_approval_settings" /> | `UPDATE` | <CopyableCode code="projectsId" /> | Updates the settings associated with a project, folder, or organization. Settings to update are determined by the value of field_mask. |

## `SELECT` examples

Gets the settings associated with a project, folder, or organization.

```sql
SELECT
name,
activeKeyVersion,
ancestorHasActiveKeyVersion,
enrolledAncestor,
enrolledServices,
invalidKeyVersion,
notificationEmails,
notificationPubsubTopic,
preferNoBroadApprovalRequests,
preferredRequestExpirationDays,
requestScopeMaxWidthPreference,
requireCustomerVisibleJustification
FROM google.accessapproval.access_approval_settings
WHERE foldersId = '{{ foldersId }}'; 
```

## `UPDATE` example

Updates a access_approval_setting only if the necessary resources are available.

```sql
UPDATE google.accessapproval.access_approval_settings
SET 
name = '{{ name }}',
notificationEmails = '{{ notificationEmails }}',
enrolledServices = '{{ enrolledServices }}',
enrolledAncestor = true|false,
activeKeyVersion = '{{ activeKeyVersion }}',
ancestorHasActiveKeyVersion = true|false,
invalidKeyVersion = true|false,
preferredRequestExpirationDays = '{{ preferredRequestExpirationDays }}',
preferNoBroadApprovalRequests = true|false,
notificationPubsubTopic = '{{ notificationPubsubTopic }}',
requireCustomerVisibleJustification = true|false,
requestScopeMaxWidthPreference = '{{ requestScopeMaxWidthPreference }}'
WHERE 
foldersId = '{{ foldersId }}';
```

## `DELETE` example

Deletes the specified access_approval_setting resource.

```sql
DELETE FROM google.accessapproval.access_approval_settings
WHERE foldersId = '{{ foldersId }}';
```
