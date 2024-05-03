---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - dependabot
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.dependabot.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_dismissed_at" /> | `string` | The time that the alert was auto-dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="created_at" /> | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="dependency" /> | `object` | Details for the vulnerable dependency. |
| <CopyableCode code="dismissed_at" /> | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="dismissed_by" /> | `object` | A GitHub user. |
| <CopyableCode code="dismissed_comment" /> | `string` | An optional comment associated with the alert's dismissal. |
| <CopyableCode code="dismissed_reason" /> | `string` | The reason that the alert was dismissed. |
| <CopyableCode code="fixed_at" /> | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="html_url" /> | `string` | The GitHub URL of the alert resource. |
| <CopyableCode code="number" /> | `integer` | The security alert number. |
| <CopyableCode code="security_advisory" /> | `object` | Details for the GitHub Security Advisory. |
| <CopyableCode code="security_vulnerability" /> | `object` | Details pertaining to one vulnerable version range for the advisory. |
| <CopyableCode code="state" /> | `string` | The state of the Dependabot alert. |
| <CopyableCode code="updated_at" /> | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="url" /> | `string` | The REST API URL of the alert resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_alert" /> | `SELECT` | <CopyableCode code="alert_number, owner, repo" /> | You must use an access token with the `security_events` scope to use this endpoint with private repositories.<br />You can also use tokens with the `public_repo` scope for public repositories only.<br />GitHub Apps must have **Dependabot alerts** read permission to use this endpoint. |
| <CopyableCode code="list_alerts_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | You must use an access token with the `security_events` scope to use this endpoint with private repositories.<br />You can also use tokens with the `public_repo` scope for public repositories only.<br />GitHub Apps must have **Dependabot alerts** read permission to use this endpoint. |
| <CopyableCode code="update_alert" /> | `EXEC` | <CopyableCode code="alert_number, owner, repo, data__state" /> | You must use an access token with the `security_events` scope to use this endpoint with private repositories.<br />You can also use tokens with the `public_repo` scope for public repositories only.<br />GitHub Apps must have **Dependabot alerts** write permission to use this endpoint.<br /><br />To use this endpoint, you must have access to security alerts for the repository. For more information, see "[Granting access to security alerts](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts)." |
