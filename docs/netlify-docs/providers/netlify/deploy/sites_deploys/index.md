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
| `ssl_url` | `string` |
| `context` | `string` |
| `title` | `string` |
| `locked` | `boolean` |
| `updated_at` | `string` |
| `draft` | `boolean` |
| `admin_url` | `string` |
| `commit_ref` | `string` |
| `function_schedules` | `array` |
| `framework` | `string` |
| `required` | `array` |
| `error_message` | `string` |
| `published_at` | `string` |
| `site_id` | `string` |
| `branch` | `string` |
| `required_functions` | `array` |
| `commit_url` | `string` |
| `skipped` | `boolean` |
| `deploy_ssl_url` | `string` |
| `screenshot_url` | `string` |
| `site_capabilities` | `object` |
| `deploy_url` | `string` |
| `created_at` | `string` |
| `review_url` | `string` |
| `user_id` | `string` |
| `url` | `string` |
| `review_id` | `number` |
| `state` | `string` |
| `build_id` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSiteDeploy` | `SELECT` | `deploy_id, site_id` |
| `listSiteDeploys` | `SELECT` | `site_id` |
| `createSiteDeploy` | `INSERT` | `site_id` |
| `updateSiteDeploy` | `EXEC` | `deploy_id, site_id` |
