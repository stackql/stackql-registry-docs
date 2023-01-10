---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
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
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The immutable ID of the label. |
| `name` | `string` | The display name of the label. |
| `threadsTotal` | `integer` | The total number of threads with the label. |
| `messageListVisibility` | `string` | The visibility of messages with this label in the message list in the Gmail web interface. |
| `type` | `string` | The owner type for the label. User labels are created by the user and can be modified and deleted by the user and can be applied to any message or thread. System labels are internally created and cannot be added, modified, or deleted. System labels may be able to be applied to or removed from messages and threads under some circumstances but this is not guaranteed. For example, users can apply and remove the `INBOX` and `UNREAD` labels from messages and threads, but cannot apply or remove the `DRAFTS` or `SENT` labels from messages or threads. |
| `messagesUnread` | `integer` | The number of unread messages with the label. |
| `labelListVisibility` | `string` | The visibility of the label in the label list in the Gmail web interface. |
| `messagesTotal` | `integer` | The total number of messages with the label. |
| `threadsUnread` | `integer` | The number of unread threads with the label. |
| `color` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_labels_get` | `SELECT` | `id, userId` | Gets the specified label. |
| `users_labels_list` | `SELECT` | `userId` | Lists all labels in the user's mailbox. |
| `users_labels_create` | `INSERT` | `userId` | Creates a new label. |
| `users_labels_delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to. |
| `users_labels_patch` | `EXEC` | `id, userId` | Patch the specified label. |
| `users_labels_update` | `EXEC` | `id, userId` | Updates the specified label. |
