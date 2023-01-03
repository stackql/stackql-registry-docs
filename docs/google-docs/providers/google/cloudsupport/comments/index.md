---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
  - cloudsupport
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsupport.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for the comment. |
| `createTime` | `string` | Output only. The time when this comment was created. |
| `creator` | `object` | An object containing information about the effective user and authenticated principal responsible for an action. |
| `plainTextBody` | `string` | Output only. An automatically generated plain text version of body with all rich text syntax stripped. |
| `body` | `string` | The full comment body. Maximum of 120000 characters. This can contain rich text syntax. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `cases_comments_list` | `SELECT` | `parent` | Retrieve all Comments associated with the Case object. |
| `cases_comments_create` | `INSERT` | `parent` | Add a new comment to the specified Case. |
