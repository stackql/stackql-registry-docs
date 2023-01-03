---
title: deploys
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
<tr><td><b>Name</b></td><td><code>deploys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.deploys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `framework` | `string` |
| `title` | `string` |
| `published_at` | `string` |
| `locked` | `boolean` |
| `branch` | `string` |
| `admin_url` | `string` |
| `error_message` | `string` |
| `required_functions` | `array` |
| `deploy_ssl_url` | `string` |
| `skipped` | `boolean` |
| `build_id` | `string` |
| `ssl_url` | `string` |
| `deploy_url` | `string` |
| `user_id` | `string` |
| `required` | `array` |
| `updated_at` | `string` |
| `screenshot_url` | `string` |
| `created_at` | `string` |
| `draft` | `boolean` |
| `commit_url` | `string` |
| `site_capabilities` | `object` |
| `state` | `string` |
| `review_id` | `number` |
| `review_url` | `string` |
| `site_id` | `string` |
| `commit_ref` | `string` |
| `function_schedules` | `array` |
| `context` | `string` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDeploy` | `SELECT` | `deploy_id` |
