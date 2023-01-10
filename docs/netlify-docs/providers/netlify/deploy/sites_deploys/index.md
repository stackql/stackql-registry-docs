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
| `user_id` | `string` |
| `required_functions` | `array` |
| `context` | `string` |
| `updated_at` | `string` |
| `title` | `string` |
| `published_at` | `string` |
| `commit_ref` | `string` |
| `build_id` | `string` |
| `created_at` | `string` |
| `branch` | `string` |
| `screenshot_url` | `string` |
| `admin_url` | `string` |
| `review_id` | `number` |
| `framework` | `string` |
| `deploy_ssl_url` | `string` |
| `state` | `string` |
| `required` | `array` |
| `deploy_url` | `string` |
| `function_schedules` | `array` |
| `site_capabilities` | `object` |
| `ssl_url` | `string` |
| `url` | `string` |
| `locked` | `boolean` |
| `review_url` | `string` |
| `skipped` | `boolean` |
| `draft` | `boolean` |
| `commit_url` | `string` |
| `error_message` | `string` |
| `site_id` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSiteDeploy` | `SELECT` | `deploy_id, site_id` |
| `listSiteDeploys` | `SELECT` | `site_id` |
| `createSiteDeploy` | `INSERT` | `site_id` |
| `updateSiteDeploy` | `EXEC` | `deploy_id, site_id` |
