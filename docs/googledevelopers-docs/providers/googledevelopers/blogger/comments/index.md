---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
  - blogger
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.blogger.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier for this resource. |
| `content` | `string` | The actual content of the comment. May include HTML markup. |
| `status` | `string` | The status of the comment (only populated for admin users). |
| `kind` | `string` | The kind of this entry. Always blogger#comment. |
| `updated` | `string` | RFC 3339 date-time when this comment was last updated. |
| `author` | `object` | The author of this Comment. |
| `inReplyTo` | `object` | Data about the comment this is in reply to. |
| `post` | `object` | Data about the post containing this comment. |
| `published` | `string` | RFC 3339 date-time when this comment was published. |
| `selfLink` | `string` | The API REST URL to fetch this resource from. |
| `blog` | `object` | Data about the blog containing this comment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blogId, commentId, postId` | Gets a comment by id. |
| `list` | `SELECT` | `blogId, postId` | Lists comments. |
| `delete` | `DELETE` | `blogId, commentId, postId` | Deletes a comment by blog id, post id and comment id. |
| `approve` | `EXEC` | `blogId, commentId, postId` | Marks a comment as not spam by blog id, post id and comment id. |
| `markAsSpam` | `EXEC` | `blogId, commentId, postId` | Marks a comment as spam by blog id, post id and comment id. |
