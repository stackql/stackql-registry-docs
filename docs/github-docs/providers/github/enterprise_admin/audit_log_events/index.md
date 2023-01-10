---
title: audit_log_events
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_log_events
  - enterprise_admin
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
<tr><td><b>Name</b></td><td><code>audit_log_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.audit_log_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `deploy_key_fingerprint` | `string` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `explanation` | `string` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `events_were` | `array` |  |
| `hook_id` | `integer` |  |
| `fingerprint` | `string` |  |
| `repository` | `string` | The name of the repository. |
| `openssh_public_key` | `string` |  |
| `org` | `string` |  |
| `active_was` | `boolean` |  |
| `message` | `string` |  |
| `emoji` | `string` |  |
| `target_login` | `string` |  |
| `content_type` | `string` |  |
| `config` | `array` |  |
| `business` | `string` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `previous_visibility` | `string` |  |
| `repository_public` | `boolean` |  |
| `data` | `object` |  |
| `actor_location` | `object` |  |
| `repo` | `string` | The name of the repository. |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `active` | `boolean` |  |
| `events` | `array` |  |
| `team` | `string` |  |
| `old_user` | `string` |  |
| `limited_availability` | `boolean` |  |
| `read_only` | `boolean` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `blocked_user` | `string` | The username of the account being blocked. |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `org_id` | `integer` |  |
| `config_was` | `array` |  |
| `actor` | `string` | The actor who performed the action. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `enterprise` |
