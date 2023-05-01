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
| `deploy_ssl_url` | `string` |
| `framework` | `string` |
| `state` | `string` |
| `skipped` | `boolean` |
| `commit_url` | `string` |
| `published_at` | `string` |
| `error_message` | `string` |
| `created_at` | `string` |
| `required_functions` | `array` |
| `required` | `array` |
| `function_schedules` | `array` |
| `review_id` | `number` |
| `deploy_url` | `string` |
| `ssl_url` | `string` |
| `screenshot_url` | `string` |
| `commit_ref` | `string` |
| `review_url` | `string` |
| `context` | `string` |
| `draft` | `boolean` |
| `build_id` | `string` |
| `user_id` | `string` |
| `title` | `string` |
| `branch` | `string` |
| `locked` | `boolean` |
| `admin_url` | `string` |
| `site_id` | `string` |
| `updated_at` | `string` |
| `site_capabilities` | `object` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDeploy` | `SELECT` | `deploy_id` |
