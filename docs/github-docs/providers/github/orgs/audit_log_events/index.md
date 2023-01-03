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
<tr><td><b>Id</b></td><td><code>github.orgs.audit_log_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `org_id` | `integer` |  |
| `openssh_public_key` | `string` |  |
| `active` | `boolean` |  |
| `events` | `array` |  |
| `read_only` | `boolean` |  |
| `content_type` | `string` |  |
| `fingerprint` | `string` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `repo` | `string` | The name of the repository. |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `config_was` | `array` |  |
| `explanation` | `string` |  |
| `actor_location` | `object` |  |
| `old_user` | `string` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `business` | `string` |  |
| `repository_public` | `boolean` |  |
| `message` | `string` |  |
| `emoji` | `string` |  |
| `actor` | `string` | The actor who performed the action. |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `org` | `string` |  |
| `target_login` | `string` |  |
| `limited_availability` | `boolean` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `config` | `array` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `hook_id` | `integer` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `events_were` | `array` |  |
| `repository` | `string` | The name of the repository. |
| `team` | `string` |  |
| `data` | `object` |  |
| `previous_visibility` | `string` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `active_was` | `boolean` |  |
| `deploy_key_fingerprint` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `org` |
