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
| `message` | `string` |  |
| `repository` | `string` | The name of the repository. |
| `transport_protocol` | `integer` | The type of protocol (for example, HTTP or SSH) used to transfer Git data. |
| `visibility` | `string` | The repository visibility, for example `public` or `private`. |
| `_document_id` | `string` | A unique identifier for an audit event. |
| `@timestamp` | `integer` | The time the audit log event occurred, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `org_id` | `integer` |  |
| `old_user` | `string` |  |
| `read_only` | `boolean` |  |
| `target_login` | `string` |  |
| `config_was` | `array` |  |
| `explanation` | `string` |  |
| `fingerprint` | `string` |  |
| `org` | `string` |  |
| `repo` | `string` | The name of the repository. |
| `content_type` | `string` |  |
| `action` | `string` | The name of the action that was performed, for example `user.login` or `repo.create`. |
| `deploy_key_fingerprint` | `string` |  |
| `actor_location` | `object` |  |
| `actor_id` | `integer` | The id of the actor who performed the action. |
| `actor` | `string` | The actor who performed the action. |
| `emoji` | `string` |  |
| `transport_protocol_name` | `string` | A human readable name for the protocol (for example, HTTP or SSH) used to transfer Git data. |
| `hook_id` | `integer` |  |
| `blocked_user` | `string` | The username of the account being blocked. |
| `events_were` | `array` |  |
| `config` | `array` |  |
| `openssh_public_key` | `string` |  |
| `limited_availability` | `boolean` |  |
| `team` | `string` |  |
| `events` | `array` |  |
| `repository_public` | `boolean` |  |
| `active` | `boolean` |  |
| `created_at` | `integer` | The time the audit log event was recorded, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). |
| `business` | `string` |  |
| `active_was` | `boolean` |  |
| `user` | `string` | The user that was affected by the action performed (if available). |
| `data` | `object` |  |
| `previous_visibility` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_audit_log` | `SELECT` | `org` |
