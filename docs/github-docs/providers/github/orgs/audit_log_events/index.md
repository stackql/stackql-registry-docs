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
| `hook_id` | `integer` |  |
| `events` | `array` |  |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `message` | `string` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `org_id` | `integer` |  |
| `repository` | `string` | The name of the repository. |
| `explanation` | `string` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `actor_location` | `object` |  |
| `content_type` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `actor` | `string` | The actor who performed the action. |
| `repository_public` | `boolean` |  |
| `team` | `string` |  |
| `deploy_key_fingerprint` | `string` |  |
| `emoji` | `string` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `blocked_user` | `string` | The username of the account being blocked. |
| `config` | `array` |  |
| `openssh_public_key` | `string` |  |
| `repo` | `string` | The name of the repository. |
| `previous_visibility` | `string` |  |
| `target_login` | `string` |  |
| `business` | `string` |  |
| `old_user` | `string` |  |
| `org` | `string` |  |
| `events_were` | `array` |  |
| `read_only` | `boolean` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `active_was` | `boolean` |  |
| `fingerprint` | `string` |  |
| `active` | `boolean` |  |
| `limited_availability` | `boolean` |  |
| `data` | `object` |  |
| `config_was` | `array` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `actor_id` | `integer` | The id of the actor who performed the action. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `org` |
