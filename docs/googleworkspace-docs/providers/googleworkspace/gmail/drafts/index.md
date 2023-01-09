---
title: drafts
hide_title: false
hide_table_of_contents: false
keywords:
  - drafts
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
<tr><td><b>Name</b></td><td><code>drafts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.drafts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The immutable ID of the draft. |
| `message` | `object` | An email message. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_drafts_get` | `SELECT` | `id, userId` | Gets the specified draft. |
| `users_drafts_list` | `SELECT` | `userId` | Lists the drafts in the user's mailbox. |
| `users_drafts_create` | `INSERT` | `userId` | Creates a new draft with the `DRAFT` label. |
| `users_drafts_delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified draft. Does not simply trash it. |
| `users_drafts_send` | `EXEC` | `userId` | Sends the specified, existing draft to the recipients in the `To`, `Cc`, and `Bcc` headers. |
| `users_drafts_update` | `EXEC` | `id, userId` | Replaces a draft's content. |
