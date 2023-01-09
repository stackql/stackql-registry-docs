---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the comment. |
| `replies` | `array` | The full list of replies to the comment in chronological order. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#comment". |
| `anchor` | `string` | A region of the document represented as a JSON string. For details on defining anchor properties, refer to  Add comments and replies. |
| `modifiedTime` | `string` | The last time the comment or any of its replies was modified (RFC 3339 date-time). |
| `deleted` | `boolean` | Whether the comment has been deleted. A deleted comment has no content. |
| `author` | `object` | Information about a Drive user. |
| `content` | `string` | The plain text content of the comment. This field is used for setting the content, while htmlContent should be displayed. |
| `resolved` | `boolean` | Whether the comment has been resolved by one of its replies. |
| `createdTime` | `string` | The time at which the comment was created (RFC 3339 date-time). |
| `htmlContent` | `string` | The content of the comment with HTML formatting. |
| `quotedFileContent` | `object` | The file content to which the comment refers, typically within the anchor region. For a text file, for example, this would be the text at the location of the comment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `commentId, fileId` | Gets a comment by ID. |
| `list` | `SELECT` | `fileId` | Lists a file's comments. |
| `create` | `INSERT` | `fileId` | Creates a comment on a file. |
| `delete` | `DELETE` | `commentId, fileId` | Deletes a comment. |
| `update` | `EXEC` | `commentId, fileId` | Updates a comment with patch semantics. |
