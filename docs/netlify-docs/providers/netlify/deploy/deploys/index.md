---
title: deploys
hide_title: false
hide_table_of_contents: false
keywords:
  - deploys
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
<tr><td><b>Name</b></td><td><code>deploys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.deploys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `updated_at` | `string` |
| `function_schedules` | `array` |
| `user_id` | `string` |
| `skipped` | `boolean` |
| `locked` | `boolean` |
| `ssl_url` | `string` |
| `title` | `string` |
| `context` | `string` |
| `required` | `array` |
| `review_id` | `number` |
| `screenshot_url` | `string` |
| `state` | `string` |
| `commit_ref` | `string` |
| `site_id` | `string` |
| `draft` | `boolean` |
| `error_message` | `string` |
| `deploy_url` | `string` |
| `published_at` | `string` |
| `deploy_ssl_url` | `string` |
| `commit_url` | `string` |
| `created_at` | `string` |
| `branch` | `string` |
| `required_functions` | `array` |
| `admin_url` | `string` |
| `build_id` | `string` |
| `site_capabilities` | `object` |
| `url` | `string` |
| `review_url` | `string` |
| `framework` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDeploy` | `SELECT` | `deploy_id` |
