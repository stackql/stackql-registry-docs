---
title: sites_deploys
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_deploys
  - deploy
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
<tr><td><b>Name</b></td><td><code>sites_deploys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.sites_deploys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `framework` | `string` |
| `screenshot_url` | `string` |
| `function_schedules` | `array` |
| `deploy_ssl_url` | `string` |
| `commit_url` | `string` |
| `skipped` | `boolean` |
| `draft` | `boolean` |
| `published_at` | `string` |
| `deploy_url` | `string` |
| `required` | `array` |
| `required_functions` | `array` |
| `commit_ref` | `string` |
| `build_id` | `string` |
| `user_id` | `string` |
| `branch` | `string` |
| `error_message` | `string` |
| `review_id` | `number` |
| `title` | `string` |
| `state` | `string` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `context` | `string` |
| `review_url` | `string` |
| `site_id` | `string` |
| `ssl_url` | `string` |
| `url` | `string` |
| `site_capabilities` | `object` |
| `locked` | `boolean` |
| `admin_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSiteDeploy` | `SELECT` | `deploy_id, site_id` |
| `listSiteDeploys` | `SELECT` | `site_id` |
| `createSiteDeploy` | `INSERT` | `site_id` |
| `updateSiteDeploy` | `EXEC` | `deploy_id, site_id` |
