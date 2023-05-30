---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - dashboards
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.dashboards.dashboards</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the dashboard. This id is used to get detailed information about the dashboard, such as panels, variables and the layout.<br /> |
| `description` | `string` | Description of the dashboard. |
| `panels` | `array` | Panels in the dashboard. |
| `folderId` | `string` | The identifier of the folder to save the dashboard in. By default it is saved in your personal folder.<br /> |
| `theme` | `string` | Theme for the dashboard. Either `Light` or `Dark`. |
| `topologyLabelMap` | `object` | Map of the topology labels. Each label has a key and a list of values. If a value is `*`, it means the label will match content for all values of its key.<br /> |
| `title` | `string` | Title of the dashboard. |
| `refreshInterval` | `integer` | Interval of time (in seconds) to automatically refresh the dashboard. A value of 0 means we never automatically refresh the dashboard. Allowed values are `0`, `30`, `60`, 120`, `300`, `900`, `3600`, `86400`.<br /> |
| `hierarchies` | `array` | If set to non-empty array denotes that the dashboard concerns given hierarchies. |
| `layout` | `object` |  |
| `contentId` | `string` | Content identifier for the dashboard. This id is used to connect to the Sumo Content Library and get general metadata about the dashboard. Use this id if you want to search for dashboards in Sumo folders.<br /> |
| `domain` | `string` | If set denotes that the dashboard concerns a given domain (e.g. `aws`, `k8s`, `app`). |
| `variables` | `array` | Variables to apply to the panels. |
| `timeRange` | `object` |  |
| `scheduleId` | `string` | Scheduled report identifier for the dashboard. Only most recently modified report schedule is rerun per dashboard. This id is used to manage the schedule details through the scheduled report API.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDashboard` | `SELECT` | `id, region` | Get a dashboard by the given identifier. |
| `listDashboards` | `SELECT` | `region` | List all dashboards under the Personal folder created by the user or under folders viewable by user. |
| `createDashboard` | `INSERT` | `data__timeRange, data__title, region` | Creates a new dashboard. |
| `deleteDashboard` | `DELETE` | `id, region` | Delete a dashboard by the given identifier. |
| `updateDashboard` | `EXEC` | `id, data__timeRange, data__title, region` | Update a dashboard by the given identifier. |
