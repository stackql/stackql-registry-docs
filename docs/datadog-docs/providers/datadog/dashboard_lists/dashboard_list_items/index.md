---
title: dashboard_list_items
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard_list_items
  - dashboard_lists
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard_list_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.dashboard_lists.dashboard_list_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the dashboard. |
| <CopyableCode code="author" /> | `object` | Creator of the object. |
| <CopyableCode code="created" /> | `string` | Date of creation of the dashboard. |
| <CopyableCode code="icon" /> | `string` | URL to the icon of the dashboard. |
| <CopyableCode code="integration_id" /> | `string` | The short name of the integration. |
| <CopyableCode code="is_favorite" /> | `boolean` | Whether or not the dashboard is in the favorites. |
| <CopyableCode code="is_read_only" /> | `boolean` | Whether or not the dashboard is read only. |
| <CopyableCode code="is_shared" /> | `boolean` | Whether the dashboard is publicly shared or not. |
| <CopyableCode code="modified" /> | `string` | Date of last edition of the dashboard. |
| <CopyableCode code="popularity" /> | `integer` | Popularity of the dashboard. |
| <CopyableCode code="tags" /> | `array` | List of team names representing ownership of a dashboard. |
| <CopyableCode code="title" /> | `string` | Title of the dashboard. |
| <CopyableCode code="type" /> | `string` | The type of the dashboard. |
| <CopyableCode code="url" /> | `string` | URL path to the dashboard. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_dashboard_list_items" /> | `SELECT` | <CopyableCode code="dashboard_list_id, dd_site" /> | Fetch the dashboard list’s dashboard definitions. |
| <CopyableCode code="create_dashboard_list_items" /> | `INSERT` | <CopyableCode code="dashboard_list_id, dd_site" /> | Add dashboards to an existing dashboard list. |
| <CopyableCode code="delete_dashboard_list_items" /> | `DELETE` | <CopyableCode code="dashboard_list_id, dd_site" /> | Delete dashboards from an existing dashboard list. |
| <CopyableCode code="_get_dashboard_list_items" /> | `EXEC` | <CopyableCode code="dashboard_list_id, dd_site" /> | Fetch the dashboard list’s dashboard definitions. |
| <CopyableCode code="update_dashboard_list_items" /> | `EXEC` | <CopyableCode code="dashboard_list_id, dd_site" /> | Update dashboards of an existing dashboard list. |
