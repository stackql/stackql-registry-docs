---
title: sites_snippets
hide_title: false
hide_table_of_contents: false
keywords:
  - netlify
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites_snippets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.snippet.sites_snippets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `goal_position` | `string` |
| `site_id` | `string` |
| `title` | `string` |
| `general` | `string` |
| `general_position` | `string` |
| `goal` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSiteSnippet` | `SELECT` | `site_id, snippet_id` |
| `listSiteSnippets` | `SELECT` | `site_id` |
| `createSiteSnippet` | `INSERT` | `site_id` |
| `deleteSiteSnippet` | `DELETE` | `site_id, snippet_id` |
| `updateSiteSnippet` | `EXEC` | `site_id, snippet_id` |
