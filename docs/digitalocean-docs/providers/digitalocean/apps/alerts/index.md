---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - apps
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="component_name" /> | `string` |
| <CopyableCode code="emails" /> | `array` |
| <CopyableCode code="phase" /> | `string` |
| <CopyableCode code="progress" /> | `object` |
| <CopyableCode code="slack_webhooks" /> | `array` |
| <CopyableCode code="spec" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_alerts" /> | `SELECT` | <CopyableCode code="app_id" /> | List alerts associated to the app and any components. This includes configuration information about the alerts including emails, slack webhooks, and triggering events or conditions. |
| <CopyableCode code="_list_alerts" /> | `EXEC` | <CopyableCode code="app_id" /> | List alerts associated to the app and any components. This includes configuration information about the alerts including emails, slack webhooks, and triggering events or conditions. |
| <CopyableCode code="assign_alertDestinations" /> | `EXEC` | <CopyableCode code="alert_id, app_id" /> | Updates the emails and slack webhook destinations for app alerts. Emails must be associated to a user with access to the app. |
