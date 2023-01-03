---
title: autolinks
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
<tr><td><b>Name</b></td><td><code>autolinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.autolinks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `key_prefix` | `string` | The prefix of a key that is linkified. |
| `url_template` | `string` | A template for the target URL that is generated if a key was found. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_autolink` | `SELECT` | `autolink_id, owner, repo` | This returns a single autolink reference by ID that was configured for the given repository.<br /><br />Information about autolinks are only available to repository administrators. |
| `list_autolinks` | `SELECT` | `owner, repo` | This returns a list of autolinks configured for the given repository.<br /><br />Information about autolinks are only available to repository administrators. |
| `create_autolink` | `INSERT` | `owner, repo, data__key_prefix, data__url_template` | Users with admin access to the repository can create an autolink. |
| `delete_autolink` | `DELETE` | `autolink_id, owner, repo` | This deletes a single autolink reference by ID that was configured for the given repository.<br /><br />Information about autolinks are only available to repository administrators. |
