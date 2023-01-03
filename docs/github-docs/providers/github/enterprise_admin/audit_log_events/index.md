---
title: audit_log_events
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `message` | `string` |  |
| `target_login` | `string` |  |
| `previous_visibility` | `string` |  |
| `explanation` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `config` | `array` |  |
| `openssh_public_key` | `string` |  |
| `read_only` | `boolean` |  |
| `deploy_key_fingerprint` | `string` |  |
| `org_id` | `integer` |  |
| `hook_id` | `integer` |  |
| `data` | `object` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `business` | `string` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `repository_public` | `boolean` |  |
| `events` | `array` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `config_was` | `array` |  |
| `repository` | `string` | The name of the repository. |
| `active` | `boolean` |  |
| `active_was` | `boolean` |  |
| `events_were` | `array` |  |
| `org` | `string` |  |
| `fingerprint` | `string` |  |
| `emoji` | `string` |  |
| `actor_location` | `object` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `actor` | `string` | The actor who performed the action. |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `limited_availability` | `boolean` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `repo` | `string` | The name of the repository. |
| `content_type` | `string` |  |
| `team` | `string` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `old_user` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `enterprise` |
