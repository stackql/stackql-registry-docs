---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
  - cloudidentity
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.memberships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `memberships` | `array` | The `Membership`s under the specified `parent`. |
| `nextPageToken` | `string` | A continuation token to retrieve the next page of results, or empty if there are no more results available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupsId, membershipsId` | Retrieves a `Membership`. |
| `list` | `SELECT` | `groupsId` | Lists the `Membership`s within a `Group`. |
| `create` | `INSERT` | `groupsId` | Creates a `Membership`. |
| `delete` | `DELETE` | `groupsId, membershipsId` | Deletes a `Membership`. |
| `check_transitive_membership` | `EXEC` | `groupsId` | Check a potential member for membership in a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A member has membership to a group as long as there is a single viewable transitive membership between the group and the member. The actor must have view permissions to at least one transitive membership between the member and group. |
| `lookup` | `EXEC` | `groupsId` | Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Membership` by its `EntityKey`. |
| `modify_membership_roles` | `EXEC` | `groupsId, membershipsId` | Modifies the `MembershipRole`s of a `Membership`. |
| `search_direct_groups` | `EXEC` | `groupsId` | Searches direct groups of a member. |
| `search_transitive_groups` | `EXEC` | `groupsId` | Search transitive groups of a member. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A transitive group is any group that has a direct or indirect membership to the member. Actor must have view permissions all transitive groups. |
| `search_transitive_memberships` | `EXEC` | `groupsId` | Search transitive memberships of a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the group is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A transitive membership is any direct or indirect membership of a group. Actor must have view permissions to all transitive memberships. |
