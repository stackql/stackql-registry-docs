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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.apps.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `functions` | `array` |  |
| `static_sites` | `array` |  |
| `jobs` | `array` |  |
| `phase_last_updated_at` | `string` |  |
| `phase` | `string` |  |
| `spec` | `object` | The desired configuration of an application. |
| `progress` | `object` |  |
| `updated_at` | `string` |  |
| `tier_slug` | `string` |  |
| `services` | `array` |  |
| `cause` | `string` |  |
| `created_at` | `string` |  |
| `workers` | `array` |  |
| `cloned_from` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_deployment` | `SELECT` | `app_id, deployment_id` | Retrieve information about an app deployment. |
| `list_deployments` | `SELECT` | `app_id` | List all deployments of an app. |
| `create_deployment` | `INSERT` | `app_id` | Creating an app deployment will pull the latest changes from your repository and schedule a new deployment for your app. |
| `_get_deployment` | `EXEC` | `app_id, deployment_id` | Retrieve information about an app deployment. |
| `_list_deployments` | `EXEC` | `app_id` | List all deployments of an app. |
| `cancel_deployment` | `EXEC` | `app_id, deployment_id` | Immediately cancel an in-progress deployment. |
