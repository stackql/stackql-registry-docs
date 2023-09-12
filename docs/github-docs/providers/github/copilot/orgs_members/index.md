---
title: orgs_members
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_members
  - copilot
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orgs_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.copilot.orgs_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `created_at` | `string` | Timestamp of when the assignee was last granted access to GitHub Copilot, in ISO 8601 format. |
| `last_activity_at` | `string` | Timestamp of user's last GitHub Copilot activity, in ISO 8601 format. |
| `last_activity_editor` | `string` | Last editor that was used by the user for a GitHub Copilot completion. |
| `pending_cancellation_date` | `string` | The pending cancellation date for the seat, in `YYYY-MM-DD` format. This will be null unless the assignee's Copilot access has been canceled during the current billing cycle. If the seat has been cancelled, this corresponds to the start of the organization's next billing cycle. |
| `updated_at` | `string` | Timestamp of when the assignee's GitHub Copilot access was last updated, in ISO 8601 format. |
| `assignee` | `object` | The assignee that has been granted access to GitHub Copilot. |
| `assigning_team` | `object` | The team that granted access to GitHub Copilot to the assignee. This will be null if the user was assigned a seat individually. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_copilot_seat_assignment_details_for_user` | `SELECT` | `org, username` |
