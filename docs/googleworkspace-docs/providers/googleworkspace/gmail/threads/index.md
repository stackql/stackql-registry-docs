---
title: threads
hide_title: false
hide_table_of_contents: false
keywords:
  - threads
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
<tr><td><b>Name</b></td><td><code>threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.threads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of the thread. |
| `messages` | `array` | The list of messages in the thread. |
| `snippet` | `string` | A short part of the message text. |
| `historyId` | `string` | The ID of the last history record that modified this thread. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_threads_get` | `SELECT` | `id, userId` | Gets the specified thread. |
| `users_threads_list` | `SELECT` | `userId` | Lists the threads in the user's mailbox. |
| `users_threads_delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified thread. Any messages that belong to the thread are also deleted. This operation cannot be undone. Prefer `threads.trash` instead. |
| `users_threads_modify` | `EXEC` | `id, userId` | Modifies the labels applied to the thread. This applies to all messages in the thread. |
| `users_threads_trash` | `EXEC` | `id, userId` | Moves the specified thread to the trash. Any messages that belong to the thread are also moved to the trash. |
| `users_threads_untrash` | `EXEC` | `id, userId` | Removes the specified thread from the trash. Any messages that belong to the thread are also removed from the trash. |
