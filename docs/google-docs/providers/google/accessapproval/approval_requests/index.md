
---
title: approval_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - approval_requests
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

Creates, updates, deletes or gets an <code>approval_request</code> resource or lists <code>approval_requests</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>approval_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.accessapproval.approval_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the request. Format is "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}". |
| <CopyableCode code="approve" /> | `object` | A decision that has been made to approve access to a resource. |
| <CopyableCode code="dismiss" /> | `object` | A decision that has been made to dismiss an approval request. |
| <CopyableCode code="requestTime" /> | `string` | The time at which approval was requested. |
| <CopyableCode code="requestedAugmentedInfo" /> | `object` | This field contains the augmented information of the request. |
| <CopyableCode code="requestedDuration" /> | `string` | The requested access duration. |
| <CopyableCode code="requestedExpiration" /> | `string` | The original requested expiration for the approval. Calculated by adding the requested_duration to the request_time. |
| <CopyableCode code="requestedLocations" /> | `object` | Home office and physical location of the principal. |
| <CopyableCode code="requestedReason" /> | `object` |  |
| <CopyableCode code="requestedResourceName" /> | `string` | The resource for which approval is being requested. The format of the resource name is defined at https://cloud.google.com/apis/design/resource_names. The resource name here may either be a "full" resource name (e.g. "//library.googleapis.com/shelves/shelf1/books/book2") or a "relative" resource name (e.g. "shelves/shelf1/books/book2") as described in the resource name specification. |
| <CopyableCode code="requestedResourceProperties" /> | `object` | The properties associated with the resource of the request. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_approval_requests_get" /> | `SELECT` | <CopyableCode code="approvalRequestsId, foldersId" /> | Gets an approval request. Returns NOT_FOUND if the request does not exist. |
| <CopyableCode code="folders_approval_requests_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological. |
| <CopyableCode code="organizations_approval_requests_get" /> | `SELECT` | <CopyableCode code="approvalRequestsId, organizationsId" /> | Gets an approval request. Returns NOT_FOUND if the request does not exist. |
| <CopyableCode code="organizations_approval_requests_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological. |
| <CopyableCode code="projects_approval_requests_get" /> | `SELECT` | <CopyableCode code="approvalRequestsId, projectsId" /> | Gets an approval request. Returns NOT_FOUND if the request does not exist. |
| <CopyableCode code="projects_approval_requests_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological. |
| <CopyableCode code="folders_approval_requests_approve" /> | `EXEC` | <CopyableCode code="approvalRequestsId, foldersId" /> | Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| <CopyableCode code="folders_approval_requests_dismiss" /> | `EXEC` | <CopyableCode code="approvalRequestsId, foldersId" /> | Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| <CopyableCode code="folders_approval_requests_invalidate" /> | `EXEC` | <CopyableCode code="approvalRequestsId, foldersId" /> | Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval. Returns FAILED_PRECONDITION if the request exists but is not in an approved state. |
| <CopyableCode code="organizations_approval_requests_approve" /> | `EXEC` | <CopyableCode code="approvalRequestsId, organizationsId" /> | Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| <CopyableCode code="organizations_approval_requests_dismiss" /> | `EXEC` | <CopyableCode code="approvalRequestsId, organizationsId" /> | Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| <CopyableCode code="organizations_approval_requests_invalidate" /> | `EXEC` | <CopyableCode code="approvalRequestsId, organizationsId" /> | Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval. Returns FAILED_PRECONDITION if the request exists but is not in an approved state. |
| <CopyableCode code="projects_approval_requests_approve" /> | `EXEC` | <CopyableCode code="approvalRequestsId, projectsId" /> | Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| <CopyableCode code="projects_approval_requests_dismiss" /> | `EXEC` | <CopyableCode code="approvalRequestsId, projectsId" /> | Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| <CopyableCode code="projects_approval_requests_invalidate" /> | `EXEC` | <CopyableCode code="approvalRequestsId, projectsId" /> | Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval. Returns FAILED_PRECONDITION if the request exists but is not in an approved state. |

## `SELECT` examples

Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological.

```sql
SELECT
name,
approve,
dismiss,
requestTime,
requestedAugmentedInfo,
requestedDuration,
requestedExpiration,
requestedLocations,
requestedReason,
requestedResourceName,
requestedResourceProperties
FROM google.accessapproval.approval_requests
WHERE foldersId = '{{ foldersId }}'; 
```
