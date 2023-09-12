---
title: orgs_billing_selected_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_billing_selected_teams
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
<tr><td><b>Name</b></td><td><code>orgs_billing_selected_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.copilot.orgs_billing_selected_teams</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `add_copilot_for_business_seats_for_teams` | `INSERT` | `org, data__selected_teams` | **Note**: This endpoint is in beta and is subject to change.<br /><br /> Purchases a GitHub Copilot for Business seat for all users within each specified team.<br /> The organization will be billed accordingly. For more information about Copilot for Business pricing, see "[About billing for GitHub Copilot for Business](https://docs.github.com/billing/managing-billing-for-github-copilot/about-billing-for-github-copilot#pricing-for-github-copilot-for-business)".<br /><br /> Only organization owners and members with admin permissions can configure GitHub Copilot in their organization. You must<br /> authenticate using an access token with the `manage_billing:copilot` scope to use this endpoint.<br /><br /> In order for an admin to use this endpoint, the organization must have a Copilot for Business subscription and a configured suggestion matching policy.<br /> For more information about setting up a Copilot for Business subscription, see "[Setting up a Copilot for Business subscription for your organization](https://docs.github.com/billing/managing-billing-for-github-copilot/managing-your-github-copilot-subscription-for-your-organization-or-enterprise#setting-up-a-copilot-for-business-subscription-for-your-organization)".<br /> For more information about setting a suggestion matching policy, see "[Configuring suggestion matching policies for GitHub Copilot in your organization](https://docs.github.com/copilot/configuring-github-copilot/configuring-github-copilot-settings-in-your-organization#configuring-suggestion-matching-policies-for-github-copilot-in-your-organization)". |
| `cancel_copilot_seat_assignment_for_teams` | `EXEC` | `org, data__selected_teams` | **Note**: This endpoint is in beta and is subject to change.<br /><br />Cancels the Copilot for Business seat assignment for all members of each team specified.<br />This will cause the members of the specified team(s) to lose access to GitHub Copilot at the end of the current billing cycle, and the organization will not be billed further for those users.<br /><br />For more information about Copilot for Business pricing, see "[About billing for GitHub Copilot for Business](https://docs.github.com/billing/managing-billing-for-github-copilot/about-billing-for-github-copilot#pricing-for-github-copilot-for-business)".<br /><br />For more information about disabling access to Copilot for Business, see "[Disabling access to GitHub Copilot for specific users in your organization](https://docs.github.com/copilot/configuring-github-copilot/configuring-github-copilot-settings-in-your-organization#disabling-access-to-github-copilot-for-specific-users-in-your-organization)".<br /><br />Only organization owners and members with admin permissions can configure GitHub Copilot in their organization. You must<br />authenticate using an access token with the `manage_billing:copilot` scope to use this endpoint. |
