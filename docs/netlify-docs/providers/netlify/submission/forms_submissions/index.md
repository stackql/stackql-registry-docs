---
title: forms_submissions
hide_title: false
hide_table_of_contents: false
keywords:
  - forms_submissions
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
<tr><td><b>Name</b></td><td><code>forms_submissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.submission.forms_submissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `body` | `string` |
| `company` | `string` |
| `email` | `string` |
| `summary` | `string` |
| `created_at` | `string` |
| `last_name` | `string` |
| `first_name` | `string` |
| `number` | `integer` |
| `data` | `object` |
| `site_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listFormSubmissions` | `SELECT` | `form_id` |
