---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - site
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.site.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `published_deploy` | `object` |
| `plan` | `string` |
| `url` | `string` |
| `admin_url` | `string` |
| `custom_domain` | `string` |
| `build_image` | `string` |
| `deploy_url` | `string` |
| `prerender` | `string` |
| `git_provider` | `string` |
| `id_domain` | `string` |
| `managed_dns` | `boolean` |
| `session_id` | `string` |
| `ssl` | `boolean` |
| `domain_aliases` | `array` |
| `account_name` | `string` |
| `ssl_url` | `string` |
| `password` | `string` |
| `capabilities` | `object` |
| `state` | `string` |
| `updated_at` | `string` |
| `account_slug` | `string` |
| `force_ssl` | `boolean` |
| `screenshot_url` | `string` |
| `notification_email` | `string` |
| `created_at` | `string` |
| `default_hooks_data` | `object` |
| `build_settings` | `object` |
| `user_id` | `string` |
| `processing_settings` | `object` |
| `deploy_hook` | `string` |
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
