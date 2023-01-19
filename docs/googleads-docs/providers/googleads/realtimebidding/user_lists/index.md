---
title: user_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - user_lists
  - realtimebidding
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.realtimebidding.user_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the user list that must follow the pattern `buyers/&#123;buyer&#125;/userLists/&#123;user_list&#125;`, where `&#123;buyer&#125;` represents the account ID of the buyer who owns the user list. For a bidder accessing user lists on behalf of a child seat buyer, `&#123;buyer&#125;` represents the account ID of the child seat buyer. `&#123;user_list&#125;` is an int64 identifier assigned by Google to uniquely identify a user list. |
| `description` | `string` | The description for the user list. |
| `status` | `string` | Output only. The status of the user list. A new user list starts out as open. |
| `urlRestriction` | `object` | Represents the URL restriction (for the URL captured by the pixel callback) for a user list. |
| `displayName` | `string` | Required. Display name of the user list. This must be unique across all user lists for a given account. |
| `membershipDurationDays` | `string` | Required. The number of days a user's cookie stays on the user list. The field must be between 0 and 540 inclusive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `buyers_userLists_get` | `SELECT` | `buyersId, userListsId` | Gets a user list by its name. |
| `buyers_userLists_list` | `SELECT` | `buyersId` | Lists the user lists visible to the current user. |
| `buyers_userLists_create` | `INSERT` | `buyersId` | Create a new user list. |
| `buyers_userLists_close` | `EXEC` | `buyersId, userListsId` | Change the status of a user list to CLOSED. This prevents new users from being added to the user list. |
| `buyers_userLists_open` | `EXEC` | `buyersId, userListsId` | Change the status of a user list to OPEN. This allows new users to be added to the user list. |
| `buyers_userLists_update` | `EXEC` | `buyersId, userListsId` | Update the given user list. Only user lists with URLRestrictions can be updated. |
