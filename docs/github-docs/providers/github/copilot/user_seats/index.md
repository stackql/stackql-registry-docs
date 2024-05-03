---
title: user_seats
hide_title: false
hide_table_of_contents: false
keywords:
  - user_seats
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_seats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.copilot.user_seats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assignee" /> | `object` | The assignee that has been granted access to GitHub Copilot. |
| <CopyableCode code="assigning_team" /> | `object` | The team that granted access to GitHub Copilot to the assignee. This will be null if the user was assigned a seat individually. |
| <CopyableCode code="created_at" /> | `string` | Timestamp of when the assignee was last granted access to GitHub Copilot, in ISO 8601 format. |
| <CopyableCode code="last_activity_at" /> | `string` | Timestamp of user's last GitHub Copilot activity, in ISO 8601 format. |
| <CopyableCode code="last_activity_editor" /> | `string` | Last editor that was used by the user for a GitHub Copilot completion. |
| <CopyableCode code="pending_cancellation_date" /> | `string` | The pending cancellation date for the seat, in `YYYY-MM-DD` format. This will be null unless the assignee's Copilot access has been canceled during the current billing cycle. If the seat has been cancelled, this corresponds to the start of the organization's next billing cycle. |
| <CopyableCode code="updated_at" /> | `string` | Timestamp of when the assignee's GitHub Copilot access was last updated, in ISO 8601 format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_copilot_seat_assignment_details_for_user" /> | `SELECT` | <CopyableCode code="org, username" /> | **Note**: This endpoint is in beta and is subject to change.<br /><br />Gets the GitHub Copilot for Business seat assignment details for a member of an organization who currently has access to GitHub Copilot.<br /><br />Organization owners and members with admin permissions can view GitHub Copilot seat assignment details for members in their organization. You must authenticate using an access token with the `manage_billing:copilot` scope to use this endpoint. |
| <CopyableCode code="add_copilot_for_business_seats_for_users" /> | `INSERT` | <CopyableCode code="org, data__selected_usernames" /> | **Note**: This endpoint is in beta and is subject to change.<br /><br />Purchases a GitHub Copilot for Business seat for each user specified.<br />The organization will be billed accordingly. For more information about Copilot for Business pricing, see "[About billing for GitHub Copilot for Business](https://docs.github.com/billing/managing-billing-for-github-copilot/about-billing-for-github-copilot#pricing-for-github-copilot-for-business)".<br /><br />Only organization owners and members with admin permissions can configure GitHub Copilot in their organization. You must<br />authenticate using an access token with the `manage_billing:copilot` scope to use this endpoint.<br /><br />In order for an admin to use this endpoint, the organization must have a Copilot for Business subscription and a configured suggestion matching policy.<br />For more information about setting up a Copilot for Business subscription, see "[Setting up a Copilot for Business subscription for your organization](https://docs.github.com/billing/managing-billing-for-github-copilot/managing-your-github-copilot-subscription-for-your-organization-or-enterprise#setting-up-a-copilot-for-business-subscription-for-your-organization)".<br />For more information about setting a suggestion matching policy, see "[Configuring suggestion matching policies for GitHub Copilot in your organization](https://docs.github.com/copilot/configuring-github-copilot/configuring-github-copilot-settings-in-your-organization#configuring-suggestion-matching-policies-for-github-copilot-in-your-organization)". |
| <CopyableCode code="cancel_copilot_seat_assignment_for_users" /> | `EXEC` | <CopyableCode code="org, data__selected_usernames" /> | **Note**: This endpoint is in beta and is subject to change.<br /><br />Cancels the Copilot for Business seat assignment for each user specified.<br />This will cause the specified users to lose access to GitHub Copilot at the end of the current billing cycle, and the organization will not be billed further for those users.<br /><br />For more information about Copilot for Business pricing, see "[About billing for GitHub Copilot for Business](https://docs.github.com/billing/managing-billing-for-github-copilot/about-billing-for-github-copilot#pricing-for-github-copilot-for-business)"<br /><br />For more information about disabling access to Copilot for Business, see "[Disabling access to GitHub Copilot for specific users in your organization](https://docs.github.com/copilot/configuring-github-copilot/configuring-github-copilot-settings-in-your-organization#disabling-access-to-github-copilot-for-specific-users-in-your-organization)".<br /><br />Only organization owners and members with admin permissions can configure GitHub Copilot in their organization. You must<br />authenticate using an access token with the `manage_billing:copilot` scope to use this endpoint. |
