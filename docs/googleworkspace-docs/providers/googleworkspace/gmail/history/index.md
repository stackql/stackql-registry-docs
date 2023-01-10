---
title: history
hide_title: false
hide_table_of_contents: false
keywords:
  - history
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
<tr><td><b>Name</b></td><td><code>history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Page token to retrieve the next page of results in the list. |
| `history` | `array` | List of history records. Any `messages` contained in the response will typically only have `id` and `threadId` fields populated. |
| `historyId` | `string` | The ID of the mailbox's current history record. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users_history_list` | `SELECT` | `userId` |
