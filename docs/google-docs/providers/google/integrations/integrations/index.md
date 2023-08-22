---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - integrations
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.integrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the integration. |
| `description` | `string` | Optional. |
| `active` | `boolean` | Required. If any integration version is published. |
| `updateTime` | `string` | Output only. Auto-generated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_integrations_list` | `SELECT` | `locationsId, projectsId` | Returns the list of all integrations in the specified project. |
| `projects_locations_products_integrations_list` | `SELECT` | `locationsId, productsId, projectsId` | Returns the list of all integrations in the specified project. |
| `projects_locations_integrations_delete` | `DELETE` | `integrationsId, locationsId, projectsId` | Delete the selected integration and all versions inside |
| `projects_locations_products_integrations_delete` | `DELETE` | `integrationsId, locationsId, productsId, projectsId` | Delete the selected integration and all versions inside |
| `_projects_locations_integrations_list` | `EXEC` | `locationsId, projectsId` | Returns the list of all integrations in the specified project. |
| `_projects_locations_products_integrations_list` | `EXEC` | `locationsId, productsId, projectsId` | Returns the list of all integrations in the specified project. |
| `projects_locations_integrations_execute` | `EXEC` | `integrationsId, locationsId, projectsId` | Executes integrations synchronously by passing the trigger id in the request body. The request is not returned until the requested executions are either fulfilled or experienced an error. If the integration name is not specified (passing `-`), all of the associated integration under the given trigger_id will be executed. Otherwise only the specified integration for the given `trigger_id` is executed. This is helpful for execution the integration from UI. |
| `projects_locations_integrations_schedule` | `EXEC` | `integrationsId, locationsId, projectsId` | Schedules an integration for execution by passing the trigger id and the scheduled time in the request body. |
| `projects_locations_products_integrations_execute` | `EXEC` | `integrationsId, locationsId, productsId, projectsId` | Executes integrations synchronously by passing the trigger id in the request body. The request is not returned until the requested executions are either fulfilled or experienced an error. If the integration name is not specified (passing `-`), all of the associated integration under the given trigger_id will be executed. Otherwise only the specified integration for the given `trigger_id` is executed. This is helpful for execution the integration from UI. |
| `projects_locations_products_integrations_schedule` | `EXEC` | `integrationsId, locationsId, productsId, projectsId` | Schedules an integration for execution by passing the trigger id and the scheduled time in the request body. |
