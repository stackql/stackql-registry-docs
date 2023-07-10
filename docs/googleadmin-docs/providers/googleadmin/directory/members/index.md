---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of the group member. A member `id` can be used as a member request URI's `memberKey`. |
| `type` | `string` | The type of group member. |
| `delivery_settings` | `string` | Defines mail delivery preferences of member. This field is only supported by `insert`, `update`, and `get` methods. |
| `email` | `string` | The member's email address. A member can be a user or another group. This property is required when adding a member to a group. The `email` must be unique and cannot be an alias of another group. If the email address is changed, the API automatically reflects the email address changes. |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | The type of the API resource. For Members resources, the value is `admin#directory#member`. |
| `role` | `string` | The member's role in a group. The API returns an error for cycles in group memberships. For example, if `group1` is a member of `group2`, `group2` cannot be a member of `group1`. For more information about a member's role, see the [administration help center](https://support.google.com/a/answer/167094). |
| `status` | `string` | Status of member (Immutable) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupKey, memberKey` | Retrieves a group member's properties. |
| `list` | `SELECT` | `groupKey` | Retrieves a paginated list of all members in a group. This method times out after 60 minutes. For more information, see [Troubleshoot error codes](https://developers.google.com/admin-sdk/directory/v1/guides/troubleshoot-error-codes). |
| `insert` | `INSERT` | `groupKey` | Adds a user to the specified group. |
| `delete` | `DELETE` | `groupKey, memberKey` | Removes a member from a group. |
| `_list` | `EXEC` | `groupKey` | Retrieves a paginated list of all members in a group. This method times out after 60 minutes. For more information, see [Troubleshoot error codes](https://developers.google.com/admin-sdk/directory/v1/guides/troubleshoot-error-codes). |
| `hasMember` | `EXEC` | `groupKey, memberKey` | Checks whether the given user is a member of the group. Membership can be direct or nested, but if nested, the `memberKey` and `groupKey` must be entities in the same domain or an `Invalid input` error is returned. To check for nested memberships that include entities outside of the group's domain, use the [`checkTransitiveMembership()`](https://cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/checkTransitiveMembership) method in the Cloud Identity Groups API. |
| `patch` | `EXEC` | `groupKey, memberKey` | Updates the membership properties of a user in the specified group. This method supports [patch semantics](/admin-sdk/directory/v1/guides/performance#patch). |
| `update` | `EXEC` | `groupKey, memberKey` | Updates the membership of a user in the specified group. |
