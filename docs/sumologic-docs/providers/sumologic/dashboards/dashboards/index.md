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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.dashboards.dashboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the dashboard. This id is used to get detailed information about the dashboard, such as panels, variables and the layout.<br /> |
| <CopyableCode code="description" /> | `string` | Description of the dashboard. |
| <CopyableCode code="contentId" /> | `string` | Content identifier for the dashboard. This id is used to connect to the Sumo Content Library and get general metadata about the dashboard. Use this id if you want to search for dashboards in Sumo folders.<br /> |
| <CopyableCode code="domain" /> | `string` | If set denotes that the dashboard concerns a given domain (e.g. `aws`, `k8s`, `app`). |
| <CopyableCode code="folderId" /> | `string` | The identifier of the folder to save the dashboard in. By default it is saved in your personal folder.<br /> |
| <CopyableCode code="hierarchies" /> | `array` | If set to non-empty array denotes that the dashboard concerns given hierarchies. |
| <CopyableCode code="layout" /> | `object` |  |
| <CopyableCode code="panels" /> | `array` | Panels in the dashboard. |
| <CopyableCode code="refreshInterval" /> | `integer` | Interval of time (in seconds) to automatically refresh the dashboard. A value of 0 means we never automatically refresh the dashboard. Allowed values are `0`, `30`, `60`, 120`, `300`, `900`, `3600`, `86400`.<br /> |
| <CopyableCode code="scheduleId" /> | `string` | Scheduled report identifier for the dashboard. Only most recently modified report schedule is rerun per dashboard. This id is used to manage the schedule details through the scheduled report API.<br /> |
| <CopyableCode code="theme" /> | `string` | Theme for the dashboard. Either `Light` or `Dark`. |
| <CopyableCode code="timeRange" /> | `object` |  |
| <CopyableCode code="title" /> | `string` | Title of the dashboard. |
| <CopyableCode code="topologyLabelMap" /> | `object` | Map of the topology labels. Each label has a key and a list of values. If a value is `*`, it means the label will match content for all values of its key.<br /> |
| <CopyableCode code="variables" /> | `array` | Variables to apply to the panels. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDashboard" /> | `SELECT` | <CopyableCode code="id, region" /> | Get a dashboard by the given identifier. |
| <CopyableCode code="listDashboards" /> | `SELECT` | <CopyableCode code="region" /> | List all dashboards under the Personal folder created by the user or under folders viewable by user. |
| <CopyableCode code="createDashboard" /> | `INSERT` | <CopyableCode code="data__timeRange, data__title, region" /> | Creates a new dashboard. |
| <CopyableCode code="deleteDashboard" /> | `DELETE` | <CopyableCode code="id, region" /> | Delete a dashboard by the given identifier. |
| <CopyableCode code="updateDashboard" /> | `EXEC` | <CopyableCode code="id, data__timeRange, data__title, region" /> | Update a dashboard by the given identifier. |
