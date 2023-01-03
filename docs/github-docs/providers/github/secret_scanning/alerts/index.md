---
title: alerts
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.secret_scanning.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resolved_by` | `object` | Simple User |
| `resolved_at` | `string` | The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `url` | `string` | The REST API URL of the alert resource. |
| `resolution` | `string` | **Required when the `state` is `resolved`.** The reason for resolving the alert. Can be one of `false_positive`, `wont_fix`, `revoked`, or `used_in_tests`. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `number` | `integer` | The security alert number. |
| `locations_url` | `string` | The REST API URL of the code locations for this alert. |
| `state` | `string` | Sets the state of the secret scanning alert. Can be either `open` or `resolved`. You must provide `resolution` when you set the state to `resolved`. |
| `secret_type` | `string` | The type of secret that secret scanning detected. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `secret` | `string` | The secret that was detected. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_alert` | `SELECT` | `alert_number, owner, repo` | Gets a single secret scanning alert detected in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. |
| `list_alerts_for_enterprise` | `SELECT` | `enterprise` | Lists secret scanning alerts for eligible repositories in an enterprise, from newest to oldest.<br />To use this endpoint, you must be a member of the enterprise, and you must use an access token with the `repo` scope or `security_events` scope. Alerts are only returned for organizations in the enterprise for which you are an organization owner or a [security manager](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization). |
| `list_alerts_for_org` | `SELECT` | `org` | Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest.<br />To use this endpoint, you must be an administrator or security manager for the organization, and you must use an access token with the `repo` scope or `security_events` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. |
| `list_alerts_for_repo` | `SELECT` | `owner, repo` | Lists secret scanning alerts for a private repository, from newest to oldest. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. |
| `update_alert` | `EXEC` | `alert_number, owner, repo, data__state` | Updates the status of a secret scanning alert in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` write permission to use this endpoint. |
