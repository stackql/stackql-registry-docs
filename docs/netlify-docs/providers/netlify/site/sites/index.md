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
| `ssl_url` | `string` |
| `capabilities` | `object` |
| `screenshot_url` | `string` |
| `build_image` | `string` |
| `user_id` | `string` |
| `created_at` | `string` |
| `session_id` | `string` |
| `custom_domain` | `string` |
| `account_slug` | `string` |
| `deploy_hook` | `string` |
| `build_settings` | `object` |
| `notification_email` | `string` |
| `state` | `string` |
| `id_domain` | `string` |
| `domain_aliases` | `array` |
| `force_ssl` | `boolean` |
| `prerender` | `string` |
| `git_provider` | `string` |
| `password` | `string` |
| `url` | `string` |
| `plan` | `string` |
| `published_deploy` | `object` |
| `default_hooks_data` | `object` |
| `deploy_url` | `string` |
| `managed_dns` | `boolean` |
| `ssl` | `boolean` |
| `admin_url` | `string` |
| `updated_at` | `string` |
| `processing_settings` | `object` |
| `account_name` | `string` |
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
