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
| `limited_availability` | `boolean` |  |
| `active` | `boolean` |  |
| `org` | `string` |  |
| `explanation` | `string` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `org_id` | `integer` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `repo` | `string` | The name of the repository. |
| `target_login` | `string` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `repository` | `string` | The name of the repository. |
| `data` | `object` |  |
| `fingerprint` | `string` |  |
| `deploy_key_fingerprint` | `string` |  |
| `events_were` | `array` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `emoji` | `string` |  |
| `hook_id` | `integer` |  |
| `read_only` | `boolean` |  |
| `config_was` | `array` |  |
| `repository_public` | `boolean` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `events` | `array` |  |
| `previous_visibility` | `string` |  |
| `actor` | `string` | The actor who performed the action. |
| `message` | `string` |  |
| `config` | `array` |  |
| `old_user` | `string` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `active_was` | `boolean` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `business` | `string` |  |
| `actor_location` | `object` |  |
| `content_type` | `string` |  |
| `team` | `string` |  |
| `openssh_public_key` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `enterprise` |
