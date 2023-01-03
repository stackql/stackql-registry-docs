---
title: sites_deploys
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
<tr><td><b>Name</b></td><td><code>sites_deploys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.sites_deploys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `required` | `array` |
| `framework` | `string` |
| `commit_url` | `string` |
| `user_id` | `string` |
| `error_message` | `string` |
| `build_id` | `string` |
| `state` | `string` |
| `created_at` | `string` |
| `title` | `string` |
| `locked` | `boolean` |
| `deploy_url` | `string` |
| `url` | `string` |
| `review_id` | `number` |
| `site_id` | `string` |
| `skipped` | `boolean` |
| `published_at` | `string` |
| `ssl_url` | `string` |
| `branch` | `string` |
| `admin_url` | `string` |
| `updated_at` | `string` |
| `context` | `string` |
| `function_schedules` | `array` |
| `screenshot_url` | `string` |
| `commit_ref` | `string` |
| `review_url` | `string` |
| `required_functions` | `array` |
| `draft` | `boolean` |
| `deploy_ssl_url` | `string` |
| `site_capabilities` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSiteDeploy` | `SELECT` | `deploy_id, site_id` |
| `listSiteDeploys` | `SELECT` | `site_id` |
| `createSiteDeploy` | `INSERT` | `site_id` |
| `updateSiteDeploy` | `EXEC` | `deploy_id, site_id` |
