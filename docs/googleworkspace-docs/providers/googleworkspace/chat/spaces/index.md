---
title: spaces
hide_title: false
hide_table_of_contents: false
keywords:
  - spaces
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
<tr><td><b>Name</b></td><td><code>spaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.chat.spaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the space. Format: spaces/&#123;space&#125; |
| `displayName` | `string` | The space's display name. Required when [creating a space](https://developers.google.com/chat/api/reference/rest/v1/spaces/create). For direct messages, this field may be empty. |
| `singleUserBotDm` | `boolean` | Optional. Whether the space is a DM between a Chat app and a single human. |
| `spaceDetails` | `object` | Details about the space including description and rules. |
| `spaceThreadingState` | `string` | Output only. The threading state in the Chat space. |
| `threaded` | `boolean` | Output only. Deprecated: Use `spaceThreadingState` instead. Whether messages are threaded in this space. |
| `type` | `string` | Output only. Deprecated: Use `singleUserBotDm` or `spaceType` (developer preview) instead. The type of a space. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `spacesId` | Returns a space. Requires [authentication](https://developers.google.com/chat/api/guides/auth). Fully supports [service account authentication](https://developers.google.com/chat/api/guides/auth/service-accounts). Supports [user authentication](https://developers.google.com/chat/api/guides/auth/users) as part of the [Google Workspace Developer Preview Program](https://developers.google.com/workspace/preview), which grants early access to certain features. [User authentication](https://developers.google.com/chat/api/guides/auth/users) requires the `chat.spaces` or `chat.spaces.readonly` authorization scope. |
| `list` | `SELECT` |  | Lists spaces the caller is a member of. Requires [authentication](https://developers.google.com/chat/api/guides/auth). Fully supports [service account authentication](https://developers.google.com/chat/api/guides/auth/service-accounts). Supports [user authentication](https://developers.google.com/chat/api/guides/auth/users) as part of the [Google Workspace Developer Preview Program](https://developers.google.com/workspace/preview), which grants early access to certain features. [User authentication](https://developers.google.com/chat/api/guides/auth/users) requires the `chat.spaces` or `chat.spaces.readonly` authorization scope. Lists spaces visible to the caller or authenticated user. Group chats and DMs aren't listed until the first message is sent. |
