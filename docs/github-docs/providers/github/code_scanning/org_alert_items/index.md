---
title: org_alert_items
hide_title: false
hide_table_of_contents: false
keywords:
  - org_alert_items
  - code_scanning
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
<tr><td><b>Name</b></td><td><code>org_alert_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.code_scanning.org_alert_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_at" /> | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="dismissed_at" /> | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="dismissed_by" /> | `object` | A GitHub user. |
| <CopyableCode code="dismissed_comment" /> | `string` | The dismissal comment associated with the dismissal of the alert. |
| <CopyableCode code="dismissed_reason" /> | `string` | **Required when the state is dismissed.** The reason for dismissing or closing the alert. |
| <CopyableCode code="fixed_at" /> | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="html_url" /> | `string` | The GitHub URL of the alert resource. |
| <CopyableCode code="instances_url" /> | `string` | The REST API URL for fetching the list of instances for an alert. |
| <CopyableCode code="most_recent_instance" /> | `object` |  |
| <CopyableCode code="number" /> | `integer` | The security alert number. |
| <CopyableCode code="repository" /> | `object` | A GitHub repository. |
| <CopyableCode code="rule" /> | `object` |  |
| <CopyableCode code="state" /> | `string` | State of a code scanning alert. |
| <CopyableCode code="tool" /> | `object` |  |
| <CopyableCode code="updated_at" /> | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| <CopyableCode code="url" /> | `string` | The REST API URL of the alert resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_alerts_for_org" /> | `SELECT` | <CopyableCode code="org" /> |
