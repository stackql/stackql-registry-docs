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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>approval_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accessapproval.approval_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the request. Format is "{projects\|folders\|organizations}/{id}/approvalRequests/{approval_request}". |
| `requestedReason` | `object` |  |
| `requestedExpiration` | `string` | The requested expiration for the approval. If the request is approved, access will be granted from the time of approval until the expiration time. |
| `dismiss` | `object` | A decision that has been made to dismiss an approval request. |
| `requestedResourceProperties` | `object` | The properties associated with the resource of the request. |
| `requestedLocations` | `object` | Home office and physical location of the principal. |
| `requestTime` | `string` | The time at which approval was requested. |
| `requestedResourceName` | `string` | The resource for which approval is being requested. The format of the resource name is defined at https://cloud.google.com/apis/design/resource_names. The resource name here may either be a "full" resource name (e.g. "//library.googleapis.com/shelves/shelf1/books/book2") or a "relative" resource name (e.g. "shelves/shelf1/books/book2") as described in the resource name specification. |
| `approve` | `object` | A decision that has been made to approve access to a resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_approvalRequests_get` | `SELECT` | `approvalRequestsId, foldersId` | Gets an approval request. Returns NOT_FOUND if the request does not exist. |
| `folders_approvalRequests_list` | `SELECT` | `foldersId` | Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological. |
| `organizations_approvalRequests_get` | `SELECT` | `approvalRequestsId, organizationsId` | Gets an approval request. Returns NOT_FOUND if the request does not exist. |
| `organizations_approvalRequests_list` | `SELECT` | `organizationsId` | Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological. |
| `projects_approvalRequests_get` | `SELECT` | `approvalRequestsId, projectsId` | Gets an approval request. Returns NOT_FOUND if the request does not exist. |
| `projects_approvalRequests_list` | `SELECT` | `projectsId` | Lists approval requests associated with a project, folder, or organization. Approval requests can be filtered by state (pending, active, dismissed). The order is reverse chronological. |
| `folders_approvalRequests_approve` | `EXEC` | `approvalRequestsId, foldersId` | Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| `folders_approvalRequests_dismiss` | `EXEC` | `approvalRequestsId, foldersId` | Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| `folders_approvalRequests_invalidate` | `EXEC` | `approvalRequestsId, foldersId` | Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval. Returns FAILED_PRECONDITION if the request exists but is not in an approved state. |
| `organizations_approvalRequests_approve` | `EXEC` | `approvalRequestsId, organizationsId` | Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| `organizations_approvalRequests_dismiss` | `EXEC` | `approvalRequestsId, organizationsId` | Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| `organizations_approvalRequests_invalidate` | `EXEC` | `approvalRequestsId, organizationsId` | Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval. Returns FAILED_PRECONDITION if the request exists but is not in an approved state. |
| `projects_approvalRequests_approve` | `EXEC` | `approvalRequestsId, projectsId` | Approves a request and returns the updated ApprovalRequest. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| `projects_approvalRequests_dismiss` | `EXEC` | `approvalRequestsId, projectsId` | Dismisses a request. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It is equivalent in effect to ignoring the request altogether. Returns NOT_FOUND if the request does not exist. Returns FAILED_PRECONDITION if the request exists but is not in a pending state. |
| `projects_approvalRequests_invalidate` | `EXEC` | `approvalRequestsId, projectsId` | Invalidates an existing ApprovalRequest. Returns the updated ApprovalRequest. NOTE: This does not deny access to the resource if another request has been made and approved. It only invalidates a single approval. Returns FAILED_PRECONDITION if the request exists but is not in an approved state. |
