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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.memberships" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Membership`. Shall be of the form `groups/&#123;group&#125;/memberships/&#123;membership&#125;`. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the `Membership` was created. |
| <CopyableCode code="deliverySetting" /> | `string` | Output only. Delivery setting associated with the membership. |
| <CopyableCode code="preferredMemberKey" /> | `object` | A unique identifier for an entity in the Cloud Identity Groups API. An entity can represent either a group with an optional `namespace` or a user without a `namespace`. The combination of `id` and `namespace` must be unique; however, the same `id` can be used with different `namespace`s. |
| <CopyableCode code="roles" /> | `array` | The `MembershipRole`s that apply to the `Membership`. If unspecified, defaults to a single `MembershipRole` with `name` `MEMBER`. Must not contain duplicate `MembershipRole`s with the same `name`. |
| <CopyableCode code="type" /> | `string` | Output only. The type of the membership. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the `Membership` was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupsId, membershipsId" /> | Retrieves a `Membership`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupsId" /> | Lists the `Membership`s within a `Group`. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="groupsId" /> | Creates a `Membership`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupsId, membershipsId" /> | Deletes a `Membership`. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="groupsId" /> | Lists the `Membership`s within a `Group`. |
| <CopyableCode code="check_transitive_membership" /> | `EXEC` | <CopyableCode code="groupsId" /> | Check a potential member for membership in a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A member has membership to a group as long as there is a single viewable transitive membership between the group and the member. The actor must have view permissions to at least one transitive membership between the member and group. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="groupsId" /> | Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Membership` by its `EntityKey`. |
| <CopyableCode code="modify_membership_roles" /> | `EXEC` | <CopyableCode code="groupsId, membershipsId" /> | Modifies the `MembershipRole`s of a `Membership`. |
| <CopyableCode code="search_direct_groups" /> | `EXEC` | <CopyableCode code="groupsId" /> | Searches direct groups of a member. |
| <CopyableCode code="search_transitive_groups" /> | `EXEC` | <CopyableCode code="groupsId" /> | Search transitive groups of a member. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the member is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A transitive group is any group that has a direct or indirect membership to the member. Actor must have view permissions all transitive groups. |
| <CopyableCode code="search_transitive_memberships" /> | `EXEC` | <CopyableCode code="groupsId" /> | Search transitive memberships of a group. **Note:** This feature is only available to Google Workspace Enterprise Standard, Enterprise Plus, and Enterprise for Education; and Cloud Identity Premium accounts. If the account of the group is not one of these, a 403 (PERMISSION_DENIED) HTTP status code will be returned. A transitive membership is any direct or indirect membership of a group. Actor must have view permissions to all transitive memberships. |
