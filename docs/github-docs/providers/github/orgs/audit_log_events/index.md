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
| `active` | `boolean` |  |
| `business` | `string` |  |
| `team` | `string` |  |
| `fingerprint` | `string` |  |
| `emoji` | `string` |  |
| `actor_location` | `object` |  |
| `events_were` | `array` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `old_user` | `string` |  |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `content_type` | `string` |  |
| `explanation` | `string` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `deploy_key_fingerprint` | `string` |  |
| `active_was` | `boolean` |  |
| `read_only` | `boolean` |  |
| `repository_public` | `boolean` |  |
| `repository` | `string` | The name of the repository. |
| `events` | `array` |  |
| `actor` | `string` | The actor who performed the action. |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `config` | `array` |  |
| `openssh_public_key` | `string` |  |
| `hook_id` | `integer` |  |
| `message` | `string` |  |
| `limited_availability` | `boolean` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `target_login` | `string` |  |
| `previous_visibility` | `string` |  |
| `data` | `object` |  |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `config_was` | `array` |  |
| `org_id` | `integer` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `repo` | `string` | The name of the repository. |
| `org` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `org` |
