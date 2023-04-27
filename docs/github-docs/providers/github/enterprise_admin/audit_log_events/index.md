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
| `blocked_user` | `string` | The username of the account being blocked. |
| `data` | `object` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `team` | `string` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `emoji` | `string` |  |
| `content_type` | `string` |  |
| `org_id` | `integer` |  |
| `repository` | `string` | The name of the repository. |
| `target_login` | `string` |  |
| `business` | `string` |  |
| `events_were` | `array` |  |
| `actor` | `string` | The actor who performed the action. |
| `previous_visibility` | `string` |  |
| `openssh_public_key` | `string` |  |
| `message` | `string` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `explanation` | `string` |  |
| `old_user` | `string` |  |
| `config` | `array` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `actor_location` | `object` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `hook_id` | `integer` |  |
| `fingerprint` | `string` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `read_only` | `boolean` |  |
| `repository_public` | `boolean` |  |
| `config_was` | `array` |  |
| `events` | `array` |  |
| `active_was` | `boolean` |  |
| `repo` | `string` | The name of the repository. |
| `active` | `boolean` |  |
| `limited_availability` | `boolean` |  |
| `org` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `enterprise` |
