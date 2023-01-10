---
title: messages
hide_title: false
hide_table_of_contents: false
keywords:
  - messages
  - gmail
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
<tr><td><b>Name</b></td><td><code>messages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.messages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The immutable ID of the message. |
| `payload` | `object` | A single MIME message part. |
| `raw` | `string` | The entire email message in an RFC 2822 formatted and base64url encoded string. Returned in `messages.get` and `drafts.get` responses when the `format=RAW` parameter is supplied. |
| `threadId` | `string` | The ID of the thread the message belongs to. To add a message or draft to a thread, the following criteria must be met: 1. The requested `threadId` must be specified on the `Message` or `Draft.Message` you supply with your request. 2. The `References` and `In-Reply-To` headers must be set in compliance with the [RFC 2822](https://tools.ietf.org/html/rfc2822) standard. 3. The `Subject` headers must match.  |
| `internalDate` | `string` | The internal message creation timestamp (epoch ms), which determines ordering in the inbox. For normal SMTP-received email, this represents the time the message was originally accepted by Google, which is more reliable than the `Date` header. However, for API-migrated mail, it can be configured by client to be based on the `Date` header. |
| `labelIds` | `array` | List of IDs of labels applied to this message. |
| `snippet` | `string` | A short part of the message text. |
| `sizeEstimate` | `integer` | Estimated size in bytes of the message. |
| `historyId` | `string` | The ID of the last history record that modified this message. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_messages_get` | `SELECT` | `id, userId` | Gets the specified message. |
| `users_messages_list` | `SELECT` | `userId` | Lists the messages in the user's mailbox. |
| `users_messages_delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer `messages.trash` instead. |
| `users_messages_batchDelete` | `EXEC` | `userId` | Deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all. |
| `users_messages_batchModify` | `EXEC` | `userId` | Modifies the labels on the specified messages. |
| `users_messages_import` | `EXEC` | `userId` | Imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. This method doesn't perform SPF checks, so it might not work for some spam messages, such as those attempting to perform domain spoofing. This method does not send a message. Note: This function doesn't trigger forwarding rules or filters set up by the user. |
| `users_messages_insert` | `EXEC` | `userId` | Directly inserts a message into only this user's mailbox similar to `IMAP APPEND`, bypassing most scanning and classification. Does not send a message. |
| `users_messages_modify` | `EXEC` | `id, userId` | Modifies the labels on the specified message. |
| `users_messages_send` | `EXEC` | `userId` | Sends the specified message to the recipients in the `To`, `Cc`, and `Bcc` headers. |
| `users_messages_trash` | `EXEC` | `id, userId` | Moves the specified message to the trash. |
| `users_messages_untrash` | `EXEC` | `id, userId` | Removes the specified message from the trash. |
