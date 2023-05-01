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
| `force_ssl` | `boolean` |
| `password` | `string` |
| `updated_at` | `string` |
| `id_domain` | `string` |
| `prerender` | `string` |
| `processing_settings` | `object` |
| `deploy_hook` | `string` |
| `managed_dns` | `boolean` |
| `deploy_url` | `string` |
| `screenshot_url` | `string` |
| `state` | `string` |
| `ssl_url` | `string` |
| `domain_aliases` | `array` |
| `plan` | `string` |
| `notification_email` | `string` |
| `capabilities` | `object` |
| `session_id` | `string` |
| `default_hooks_data` | `object` |
| `build_settings` | `object` |
| `url` | `string` |
| `created_at` | `string` |
| `ssl` | `boolean` |
| `user_id` | `string` |
| `git_provider` | `string` |
| `build_image` | `string` |
| `account_name` | `string` |
| `account_slug` | `string` |
| `admin_url` | `string` |
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
