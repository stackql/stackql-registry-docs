---
title: share_dashboards_outside_organization
hide_title: false
hide_table_of_contents: false
keywords:
  - share_dashboards_outside_organization
  - policies
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
<tr><td><b>Name</b></td><td><code>share_dashboards_outside_organization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.policies.share_dashboards_outside_organization</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getShareDashboardsOutsideOrganizationPolicy` | `SELECT` |  | Get the Share Dashboards Outside Organization policy. This policy allows users to share the dashboard with view only privileges outside of the organization (capability must be enabled from the Roles page). Disabling this policy will disable all dashboards that have been shared outside of the organization. [Learn More](https://help.sumologic.com/Visualizations-and-Alerts/Dashboards/Share_Dashboards/Share_a_Dashboard_Outside_Your_Org) |
| `setShareDashboardsOutsideOrganizationPolicy` | `EXEC` | `data__enabled` | Set the Share Dashboards Outside Organization policy. This policy allows users to share the dashboard with view only privileges outside of the organization (capability must be enabled from the Roles page). Disabling this policy will disable all dashboards that have been shared outside of the organization. [Learn More](https://help.sumologic.com/Visualizations-and-Alerts/Dashboards/Share_Dashboards/Share_a_Dashboard_Outside_Your_Org) |
