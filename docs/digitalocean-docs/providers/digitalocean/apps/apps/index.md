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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.apps.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `project_id` | `string` |  |
| `owner_uuid` | `string` |  |
| `live_url_base` | `string` |  |
| `live_url` | `string` |  |
| `updated_at` | `string` |  |
| `live_domain` | `string` |  |
| `pending_deployment` | `object` | The most recent pending deployment. For CreateApp and UpdateApp transactions this is guaranteed to reflect the associated deployment. |
| `default_ingress` | `string` |  |
| `in_progress_deployment` | `object` |  |
| `region` | `object` |  |
| `pinned_deployment` | `object` | The deployment that the app is pinned to. |
| `active_deployment` | `object` |  |
| `last_deployment_created_at` | `string` |  |
| `tier_slug` | `string` |  |
| `spec` | `object` | The desired configuration of an application. |
| `created_at` | `string` |  |
| `domains` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id` | Retrieve details about an existing app by either its ID or name. To retrieve an app by its name, do not include an ID in the request path. Information about the current active deployment as well as any in progress ones will also be included in the response. |
| `list` | `SELECT` |  | List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app. |
| `create` | `INSERT` | `data__spec` | Create a new app by submitting an app specification. For documentation on app specifications (`AppSpec` objects), please refer to [the product documentation](https://docs.digitalocean.com/products/app-platform/reference/app-spec/). |
| `delete` | `DELETE` | `id` | Delete an existing app. Once deleted, all active deployments will be permanently shut down and the app deleted. If needed, be sure to back up your app specification so that you may re-create it at a later time. |
| `_get` | `EXEC` | `id` | Retrieve details about an existing app by either its ID or name. To retrieve an app by its name, do not include an ID in the request path. Information about the current active deployment as well as any in progress ones will also be included in the response. |
| `_list` | `EXEC` |  | List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app. |
| `update` | `EXEC` | `id, data__spec` | Update an existing app by submitting a new app specification. For documentation on app specifications (`AppSpec` objects), please refer to [the product documentation](https://docs.digitalocean.com/products/app-platform/reference/app-spec/). |
| `validate_appSpec` | `EXEC` | `data__spec` | To propose and validate a spec for a new or existing app, send a POST request to the `/v2/apps/propose` endpoint. The request returns some information about the proposed app, including app cost and upgrade cost. If an existing app ID is specified, the app spec is treated as a proposed update to the existing app. |
