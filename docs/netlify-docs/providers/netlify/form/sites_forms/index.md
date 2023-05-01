---
title: sites_forms
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_forms
  - form
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
<tr><td><b>Name</b></td><td><code>sites_forms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.form.sites_forms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `site_id` | `string` |
| `submission_count` | `integer` |
| `created_at` | `string` |
| `fields` | `array` |
| `paths` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listSiteForms` | `SELECT` | `site_id` |
| `deleteSiteForm` | `DELETE` | `form_id, site_id` |
