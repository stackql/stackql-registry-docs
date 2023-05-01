---
title: sites_submissions
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_submissions
  - submission
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites_submissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.submission.sites_submissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `email` | `string` |
| `site_url` | `string` |
| `company` | `string` |
| `created_at` | `string` |
| `data` | `object` |
| `summary` | `string` |
| `number` | `integer` |
| `body` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listSiteSubmissions` | `SELECT` | `site_id` |
