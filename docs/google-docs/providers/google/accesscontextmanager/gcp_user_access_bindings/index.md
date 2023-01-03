---
title: gcp_user_access_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - gcp_user_access_bindings
  - accesscontextmanager
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
<tr><td><b>Name</b></td><td><code>gcp_user_access_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accesscontextmanager.gcp_user_access_bindings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by [RFC 3986 Section 2.3](https://tools.ietf.org/html/rfc3986#section-2.3)). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N" |
| `accessLevels` | `array` | Required. Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted" |
| `groupKey` | `string` | Required. Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the [G Suite Directory API's Groups resource] (https://developers.google.com/admin-sdk/directory/v1/reference/groups#resource). If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_gcpUserAccessBindings_get` | `SELECT` | `gcpUserAccessBindingsId, organizationsId` | Gets the GcpUserAccessBinding with the given name. |
| `organizations_gcpUserAccessBindings_list` | `SELECT` | `organizationsId` | Lists all GcpUserAccessBindings for a Google Cloud organization. |
| `organizations_gcpUserAccessBindings_create` | `INSERT` | `organizationsId` | Creates a GcpUserAccessBinding. If the client specifies a name, the server ignores it. Fails if a resource already exists with the same group_key. Completion of this long-running operation does not necessarily signify that the new binding is deployed onto all affected users, which may take more time. |
| `organizations_gcpUserAccessBindings_delete` | `DELETE` | `gcpUserAccessBindingsId, organizationsId` | Deletes a GcpUserAccessBinding. Completion of this long-running operation does not necessarily signify that the binding deletion is deployed onto all affected users, which may take more time. |
| `organizations_gcpUserAccessBindings_patch` | `EXEC` | `gcpUserAccessBindingsId, organizationsId` | Updates a GcpUserAccessBinding. Completion of this long-running operation does not necessarily signify that the changed binding is deployed onto all affected users, which may take more time. |
