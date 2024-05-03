---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="cause" /> | `string` |  |
| <CopyableCode code="cloned_from" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="functions" /> | `array` |  |
| <CopyableCode code="jobs" /> | `array` |  |
| <CopyableCode code="phase" /> | `string` |  |
| <CopyableCode code="phase_last_updated_at" /> | `string` |  |
| <CopyableCode code="progress" /> | `object` |  |
| <CopyableCode code="services" /> | `array` |  |
| <CopyableCode code="spec" /> | `object` | The desired configuration of an application. |
| <CopyableCode code="static_sites" /> | `array` |  |
| <CopyableCode code="tier_slug" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="workers" /> | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_deployment" /> | `SELECT` | <CopyableCode code="app_id, deployment_id" /> | Retrieve information about an app deployment. |
| <CopyableCode code="list_deployments" /> | `SELECT` | <CopyableCode code="app_id" /> | List all deployments of an app. |
| <CopyableCode code="create_deployment" /> | `INSERT` | <CopyableCode code="app_id" /> | Creating an app deployment will pull the latest changes from your repository and schedule a new deployment for your app. |
| <CopyableCode code="_get_deployment" /> | `EXEC` | <CopyableCode code="app_id, deployment_id" /> | Retrieve information about an app deployment. |
| <CopyableCode code="_list_deployments" /> | `EXEC` | <CopyableCode code="app_id" /> | List all deployments of an app. |
| <CopyableCode code="cancel_deployment" /> | `EXEC` | <CopyableCode code="app_id, deployment_id" /> | Immediately cancel an in-progress deployment. |
