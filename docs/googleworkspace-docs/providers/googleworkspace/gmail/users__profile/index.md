---
title: users__profile
hide_title: false
hide_table_of_contents: false
keywords:
  - users__profile
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
<tr><td><b>Name</b></td><td><code>users__profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.users__profile</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `emailAddress` | `string` | The user's email address. |
| `historyId` | `string` | The ID of the mailbox's current history record. |
| `messagesTotal` | `integer` | The total number of messages in the mailbox. |
| `threadsTotal` | `integer` | The total number of threads in the mailbox. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users_getProfile` | `SELECT` | `userId` |
