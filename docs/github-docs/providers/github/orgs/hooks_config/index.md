---
title: hooks_config
hide_title: false
hide_table_of_contents: false
keywords:
  - hooks_config
  - orgs
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hooks_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.hooks_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `content_type` | `string` | The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`. |
| `insecure_ssl` | `` |  |
| `secret` | `string` | If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers). |
| `url` | `string` | The URL to which the payloads will be delivered. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_webhook_config_for_org` | `SELECT` | `hook_id, org` | Returns the webhook configuration for an organization. To get more information about the webhook, including the `active` state and `events`, use "[Get an organization webhook ](/rest/orgs/webhooks#get-an-organization-webhook)."<br /><br />Access tokens must have the `admin:org_hook` scope, and GitHub Apps must have the `organization_hooks:read` permission. |
| `update_webhook_config_for_org` | `EXEC` | `hook_id, org` | Updates the webhook configuration for an organization. To update more information about the webhook, including the `active` state and `events`, use "[Update an organization webhook ](/rest/orgs/webhooks#update-an-organization-webhook)."<br /><br />Access tokens must have the `admin:org_hook` scope, and GitHub Apps must have the `organization_hooks:write` permission. |
