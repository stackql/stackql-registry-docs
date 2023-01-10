---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - chat
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.chat.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the membership. Format: spaces/&#123;space&#125;/members/&#123;member&#125; |
| `state` | `string` | Output only. State of the membership. |
| `createTime` | `string` | Output only. The creation time of the membership, such as when a member joined or was invited to join a space. |
| `member` | `object` | A user in Google Chat. |
| `role` | `string` | Output only. User's role within a Chat space, which determines their permitted actions in the space. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `spaces_members_get` | `SELECT` | `membersId, spacesId` | [Developer Preview](https://developers.google.com/workspace/preview): Returns a membership. Requires [authentication](https://developers.google.com/chat/api/guides/auth/). Fully supports [service account authentication](https://developers.google.com/chat/api/guides/auth/service-accounts). Supports [user authentication](https://developers.google.com/chat/api/guides/auth/users) as part of the [Google Workspace Developer Preview Program](https://developers.google.com/workspace/preview), which grants early access to certain features. [User authentication](https://developers.google.com/chat/api/guides/auth/users) requires the `chat.memberships` or `chat.memberships.readonly` authorization scope. |
| `spaces_members_list` | `SELECT` | `spacesId` | [Developer Preview](https://developers.google.com/workspace/preview): Lists memberships in a space. Requires [authentication](https://developers.google.com/chat/api/guides/auth/). Fully supports [service account authentication](https://developers.google.com/chat/api/guides/auth/service-accounts). Supports [user authentication](https://developers.google.com/chat/api/guides/auth/users) as part of the [Google Workspace Developer Preview Program](https://developers.google.com/workspace/preview), which grants early access to certain features. [User authentication](https://developers.google.com/chat/api/guides/auth/users) requires the `chat.memberships` or `chat.memberships.readonly` authorization scope. |
