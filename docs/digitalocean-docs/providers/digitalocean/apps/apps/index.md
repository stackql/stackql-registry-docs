---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="active_deployment" /> | `object` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="default_ingress" /> | `string` |  |
| <CopyableCode code="domains" /> | `array` |  |
| <CopyableCode code="in_progress_deployment" /> | `object` |  |
| <CopyableCode code="last_deployment_created_at" /> | `string` |  |
| <CopyableCode code="live_domain" /> | `string` |  |
| <CopyableCode code="live_url" /> | `string` |  |
| <CopyableCode code="live_url_base" /> | `string` |  |
| <CopyableCode code="owner_uuid" /> | `string` |  |
| <CopyableCode code="pending_deployment" /> | `object` | The most recent pending deployment. For CreateApp and UpdateApp transactions this is guaranteed to reflect the associated deployment. |
| <CopyableCode code="pinned_deployment" /> | `object` | The deployment that the app is pinned to. |
| <CopyableCode code="project_id" /> | `string` |  |
| <CopyableCode code="region" /> | `object` |  |
| <CopyableCode code="spec" /> | `object` | The desired configuration of an application. |
| <CopyableCode code="tier_slug" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id" /> | Retrieve details about an existing app by either its ID or name. To retrieve an app by its name, do not include an ID in the request path. Information about the current active deployment as well as any in progress ones will also be included in the response. |
| <CopyableCode code="list" /> | `SELECT` |  | List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="data__spec" /> | Create a new app by submitting an app specification. For documentation on app specifications (`AppSpec` objects), please refer to [the product documentation](https://docs.digitalocean.com/products/app-platform/reference/app-spec/). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id" /> | Delete an existing app. Once deleted, all active deployments will be permanently shut down and the app deleted. If needed, be sure to back up your app specification so that you may re-create it at a later time. |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="id" /> | Retrieve details about an existing app by either its ID or name. To retrieve an app by its name, do not include an ID in the request path. Information about the current active deployment as well as any in progress ones will also be included in the response. |
| <CopyableCode code="_list" /> | `EXEC` |  | List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="id, data__spec" /> | Update an existing app by submitting a new app specification. For documentation on app specifications (`AppSpec` objects), please refer to [the product documentation](https://docs.digitalocean.com/products/app-platform/reference/app-spec/). |
| <CopyableCode code="validate_appSpec" /> | `EXEC` | <CopyableCode code="data__spec" /> | To propose and validate a spec for a new or existing app, send a POST request to the `/v2/apps/propose` endpoint. The request returns some information about the proposed app, including app cost and upgrade cost. If an existing app ID is specified, the app spec is treated as a proposed update to the existing app. |
