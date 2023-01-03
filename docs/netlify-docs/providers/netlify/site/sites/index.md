---
title: sites
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.site.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `state` | `string` |
| `capabilities` | `object` |
| `created_at` | `string` |
| `build_settings` | `object` |
| `git_provider` | `string` |
| `id_domain` | `string` |
| `url` | `string` |
| `password` | `string` |
| `domain_aliases` | `array` |
| `build_image` | `string` |
| `published_deploy` | `object` |
| `user_id` | `string` |
| `screenshot_url` | `string` |
| `prerender` | `string` |
| `account_slug` | `string` |
| `ssl_url` | `string` |
| `plan` | `string` |
| `deploy_url` | `string` |
| `managed_dns` | `boolean` |
| `force_ssl` | `boolean` |
| `deploy_hook` | `string` |
| `account_name` | `string` |
| `ssl` | `boolean` |
| `session_id` | `string` |
| `notification_email` | `string` |
| `admin_url` | `string` |
| `processing_settings` | `object` |
| `updated_at` | `string` |
| `default_hooks_data` | `object` |
| `custom_domain` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSite` | `SELECT` | `site_id` |
| `listSites` | `SELECT` |  |
| `listSitesForAccount` | `SELECT` | `account_slug` |
| `createSite` | `INSERT` |  |
| `createSiteInTeam` | `INSERT` | `account_slug` |
| `deleteSite` | `DELETE` | `site_id` |
| `updateSite` | `EXEC` | `site_id` |
