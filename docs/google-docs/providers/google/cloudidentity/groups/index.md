---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - cloudidentity
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `Group`. Shall be of the form `groups/{group}`. |
| `description` | `string` | An extended description to help users determine the purpose of a `Group`. Must not be longer than 4,096 characters. |
| `createTime` | `string` | Output only. The time when the `Group` was created. |
| `updateTime` | `string` | Output only. The time when the `Group` was last updated. |
| `dynamicGroupMetadata` | `object` | Dynamic group metadata like queries and status. |
| `parent` | `string` | Required. Immutable. The resource name of the entity under which this `Group` resides in the Cloud Identity resource hierarchy. Must be of the form `identitysources/{identity_source}` for external- identity-mapped groups or `customers/{customer}` for Google Groups. The `customer` must begin with "C" (for example, 'C046psxkn'). |
| `displayName` | `string` | The display name of the `Group`. |
| `groupKey` | `object` | A unique identifier for an entity in the Cloud Identity Groups API. An entity can represent either a group with an optional `namespace` or a user without a `namespace`. The combination of `id` and `namespace` must be unique; however, the same `id` can be used with different `namespace`s. |
| `labels` | `object` | Required. One or more label entries that apply to the Group. Currently supported labels contain a key with an empty value. Google Groups are the default type of group and have a label with a key of `cloudidentity.googleapis.com/groups.discussion_forum` and an empty value. Existing Google Groups can have an additional label with a key of `cloudidentity.googleapis.com/groups.security` and an empty value added to them. **This is an immutable change and the security label cannot be removed once added.** Dynamic groups have a label with a key of `cloudidentity.googleapis.com/groups.dynamic`. Identity-mapped groups for Cloud Search have a label with a key of `system/groups/external` and an empty value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupsId` | Retrieves a `Group`. |
| `list` | `SELECT` |  | Lists the `Group` resources under a customer or namespace. |
| `create` | `INSERT` |  | Creates a Group. |
| `delete` | `DELETE` | `groupsId` | Deletes a `Group`. |
| `lookup` | `EXEC` |  | Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Group` by its `EntityKey`. |
| `patch` | `EXEC` | `groupsId` | Updates a `Group`. |
| `search` | `EXEC` |  | Searches for `Group` resources matching a specified query. |
| `updateSecuritySettings` | `EXEC` | `groupsId` | Update Security Settings |
