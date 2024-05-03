---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Read-only. The unique ID of a group. A group `id` can be used as a group request URI's `groupKey`. |
| <CopyableCode code="name" /> | `string` | The group's display name. |
| <CopyableCode code="description" /> | `string` | An extended description to help users determine the purpose of a group. For example, you can include information about who should join the group, the types of messages to send to the group, links to FAQs about the group, or related groups. Maximum length is `4,096` characters. |
| <CopyableCode code="adminCreated" /> | `boolean` | Read-only. Value is `true` if this group was created by an administrator rather than a user. |
| <CopyableCode code="aliases" /> | `array` | Read-only. The list of a group's alias email addresses. To add, update, or remove a group's aliases, use the `groups.aliases` methods. If edited in a group's POST or PUT request, the edit is ignored. |
| <CopyableCode code="directMembersCount" /> | `string` | The number of users that are direct members of the group. If a group is a member (child) of this group (the parent), members of the child group are not counted in the `directMembersCount` property of the parent group. |
| <CopyableCode code="email" /> | `string` | The group's email address. If your account has multiple domains, select the appropriate domain for the email address. The `email` must be unique. This property is required when creating a group. Group email addresses are subject to the same character usage rules as usernames, see the [help center](https://support.google.com/a/answer/9193374) for details. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="kind" /> | `string` | The type of the API resource. For Groups resources, the value is `admin#directory#group`. |
| <CopyableCode code="nonEditableAliases" /> | `array` | Read-only. The list of the group's non-editable alias email addresses that are outside of the account's primary domain or subdomains. These are functioning email addresses used by the group. This is a read-only property returned in the API's response for a group. If edited in a group's POST or PUT request, the edit is ignored. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupKey" /> | Retrieves a group's properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domain" /> | Retrieves all groups of a domain or of a user given a userKey (paginated). |
| <CopyableCode code="insert" /> | `INSERT` |  | Creates a group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupKey" /> | Deletes a group. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="domain" /> | Retrieves all groups of a domain or of a user given a userKey (paginated). |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="groupKey" /> | Updates a group's properties. This method supports [patch semantics](/admin-sdk/directory/v1/guides/performance#patch). |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="groupKey" /> | Updates a group's properties. |
