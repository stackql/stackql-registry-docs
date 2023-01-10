---
title: submissions
hide_title: false
hide_table_of_contents: false
keywords:
  - submissions
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
<tr><td><b>Name</b></td><td><code>submissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.submission.submissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `email` | `string` |
| `site_url` | `string` |
| `number` | `integer` |
| `data` | `object` |
| `first_name` | `string` |
| `body` | `string` |
| `company` | `string` |
| `last_name` | `string` |
| `summary` | `string` |
| `created_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listFormSubmission` | `SELECT` | `submission_id` |
| `deleteSubmission` | `DELETE` | `submission_id` |
