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
| `site_capabilities` | `object` |
| `ssl_url` | `string` |
| `site_id` | `string` |
| `review_url` | `string` |
| `title` | `string` |
| `skipped` | `boolean` |
| `state` | `string` |
| `branch` | `string` |
| `required` | `array` |
| `user_id` | `string` |
| `screenshot_url` | `string` |
| `required_functions` | `array` |
| `published_at` | `string` |
| `framework` | `string` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `error_message` | `string` |
| `admin_url` | `string` |
| `commit_url` | `string` |
| `locked` | `boolean` |
| `url` | `string` |
| `review_id` | `number` |
| `deploy_url` | `string` |
| `deploy_ssl_url` | `string` |
| `function_schedules` | `array` |
| `build_id` | `string` |
| `draft` | `boolean` |
| `commit_ref` | `string` |
| `context` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDeploy` | `SELECT` | `deploy_id` |
