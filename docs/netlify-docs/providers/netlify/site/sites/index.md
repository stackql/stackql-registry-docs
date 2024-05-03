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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.site.sites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="account_name" /> | `string` |
| <CopyableCode code="account_slug" /> | `string` |
| <CopyableCode code="admin_url" /> | `string` |
| <CopyableCode code="build_image" /> | `string` |
| <CopyableCode code="build_settings" /> | `object` |
| <CopyableCode code="capabilities" /> | `object` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="custom_domain" /> | `string` |
| <CopyableCode code="default_hooks_data" /> | `object` |
| <CopyableCode code="deploy_hook" /> | `string` |
| <CopyableCode code="deploy_url" /> | `string` |
| <CopyableCode code="domain_aliases" /> | `array` |
| <CopyableCode code="force_ssl" /> | `boolean` |
| <CopyableCode code="git_provider" /> | `string` |
| <CopyableCode code="id_domain" /> | `string` |
| <CopyableCode code="managed_dns" /> | `boolean` |
| <CopyableCode code="notification_email" /> | `string` |
| <CopyableCode code="password" /> | `string` |
| <CopyableCode code="plan" /> | `string` |
| <CopyableCode code="prerender" /> | `string` |
| <CopyableCode code="processing_settings" /> | `object` |
| <CopyableCode code="published_deploy" /> | `object` |
| <CopyableCode code="screenshot_url" /> | `string` |
| <CopyableCode code="session_id" /> | `string` |
| <CopyableCode code="ssl" /> | `boolean` |
| <CopyableCode code="ssl_url" /> | `string` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="url" /> | `string` |
| <CopyableCode code="user_id" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSite" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="listSites" /> | `SELECT` |  |
| <CopyableCode code="listSitesForAccount" /> | `SELECT` | <CopyableCode code="account_slug" /> |
| <CopyableCode code="createSite" /> | `INSERT` |  |
| <CopyableCode code="createSiteInTeam" /> | `INSERT` | <CopyableCode code="account_slug" /> |
| <CopyableCode code="deleteSite" /> | `DELETE` | <CopyableCode code="site_id" /> |
| <CopyableCode code="updateSite" /> | `EXEC` | <CopyableCode code="site_id" /> |
