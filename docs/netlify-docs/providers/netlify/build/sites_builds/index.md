---
title: sites_builds
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_builds
  - build
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
<tr><td><b>Name</b></td><td><code>sites_builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.build.sites_builds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `created_at` | `string` |
| `deploy_id` | `string` |
| `done` | `boolean` |
| `error` | `string` |
| `sha` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listSiteBuilds` | `SELECT` | `site_id` |
| `createSiteBuild` | `INSERT` | `site_id` |
