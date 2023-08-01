---
title: audit_log_events
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_log_events
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
<tr><td><b>Name</b></td><td><code>audit_log_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.audit_log_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `openssh_public_key` | `string` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `deploy_key_fingerprint` | `string` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `hook_id` | `integer` |  |
| `repository_public` | `boolean` |  |
| `previous_visibility` | `string` |  |
| `config_was` | `array` |  |
| `target_login` | `string` |  |
| `active_was` | `boolean` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `old_user` | `string` |  |
| `repo` | `string` | The name of the repository. |
| `limited_availability` | `boolean` |  |
| `actor` | `string` | The actor who performed the action. |
| `actor_location` | `object` |  |
| `active` | `boolean` |  |
| `org` | `string` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `fingerprint` | `string` |  |
| `events_were` | `array` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `org_id` | `integer` |  |
| `config` | `array` |  |
| `repository` | `string` | The name of the repository. |
| `read_only` | `boolean` |  |
| `content_type` | `string` |  |
| `events` | `array` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `emoji` | `string` |  |
| `business` | `string` |  |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `explanation` | `string` |  |
| `team` | `string` |  |
| `data` | `object` |  |
| `message` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `org` |
