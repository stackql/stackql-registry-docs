---
title: replies
hide_title: false
hide_table_of_contents: false
keywords:
  - replies
  - drive
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
<tr><td><b>Name</b></td><td><code>replies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.replies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the reply. |
| `author` | `object` | Information about a Drive user. |
| `createdTime` | `string` | The time at which the reply was created (RFC 3339 date-time). |
| `deleted` | `boolean` | Whether the reply has been deleted. A deleted reply has no content. |
| `htmlContent` | `string` | The content of the reply with HTML formatting. |
| `modifiedTime` | `string` | The last time the reply was modified (RFC 3339 date-time). |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#reply". |
| `content` | `string` | The plain text content of the reply. This field is used for setting the content, while htmlContent should be displayed. This is required on creates if no action is specified. |
| `action` | `string` | The action the reply performed to the parent comment. Valid values are:  <br />- resolve <br />- reopen |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `commentId, fileId, replyId` | Gets a reply by ID. |
| `list` | `SELECT` | `commentId, fileId` | Lists a comment's replies. |
| `create` | `INSERT` | `commentId, fileId` | Creates a reply to a comment. |
| `delete` | `DELETE` | `commentId, fileId, replyId` | Deletes a reply. |
| `update` | `EXEC` | `commentId, fileId, replyId` | Updates a reply with patch semantics. |
