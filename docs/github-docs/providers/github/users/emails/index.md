---
title: emails
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>emails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.emails</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `verified` | `boolean` |
| `visibility` | `string` |
| `email` | `string` |
| `primary` | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_emails_for_authenticated_user` | `SELECT` |  | Lists all of your email addresses, and specifies which one is visible to the public. This endpoint is accessible with the `user:email` scope. |
| `add_email_for_authenticated_user` | `INSERT` |  | This endpoint is accessible with the `user` scope. |
| `delete_email_for_authenticated_user` | `DELETE` |  | This endpoint is accessible with the `user` scope. |
| `set_primary_email_visibility_for_authenticated_user` | `EXEC` | `data__visibility` | Sets the visibility for your primary email addresses. |
