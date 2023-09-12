---
title: hooks_config
hide_title: false
hide_table_of_contents: false
keywords:
  - hooks_config
  - repos
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
<tr><td><b>Id</b></td><td><code>github.repos.hooks_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` | The URL to which the payloads will be delivered. |
| `content_type` | `string` | The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`. |
| `insecure_ssl` | `` |  |
| `secret` | `string` | If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_webhook_config_for_repo` | `SELECT` | `hook_id, owner, repo` | Returns the webhook configuration for a repository. To get more information about the webhook, including the `active` state and `events`, use "[Get a repository webhook](/rest/webhooks/repos#get-a-repository-webhook)."<br /><br />Access tokens must have the `read:repo_hook` or `repo` scope, and GitHub Apps must have the `repository_hooks:read` permission. |
| `update_webhook_config_for_repo` | `EXEC` | `hook_id, owner, repo` | Updates the webhook configuration for a repository. To update more information about the webhook, including the `active` state and `events`, use "[Update a repository webhook](/rest/webhooks/repos#update-a-repository-webhook)."<br /><br />Access tokens must have the `write:repo_hook` or `repo` scope, and GitHub Apps must have the `repository_hooks:write` permission. |
