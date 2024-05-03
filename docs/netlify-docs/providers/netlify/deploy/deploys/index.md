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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deploys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.deploy.deploys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="admin_url" /> | `string` |
| <CopyableCode code="branch" /> | `string` |
| <CopyableCode code="build_id" /> | `string` |
| <CopyableCode code="commit_ref" /> | `string` |
| <CopyableCode code="commit_url" /> | `string` |
| <CopyableCode code="context" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="deploy_ssl_url" /> | `string` |
| <CopyableCode code="deploy_url" /> | `string` |
| <CopyableCode code="draft" /> | `boolean` |
| <CopyableCode code="error_message" /> | `string` |
| <CopyableCode code="framework" /> | `string` |
| <CopyableCode code="function_schedules" /> | `array` |
| <CopyableCode code="locked" /> | `boolean` |
| <CopyableCode code="published_at" /> | `string` |
| <CopyableCode code="required" /> | `array` |
| <CopyableCode code="required_functions" /> | `array` |
| <CopyableCode code="review_id" /> | `number` |
| <CopyableCode code="review_url" /> | `string` |
| <CopyableCode code="screenshot_url" /> | `string` |
| <CopyableCode code="site_capabilities" /> | `object` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="skipped" /> | `boolean` |
| <CopyableCode code="ssl_url" /> | `string` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="title" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="url" /> | `string` |
| <CopyableCode code="user_id" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getDeploy" /> | `SELECT` | <CopyableCode code="deploy_id" /> |
