---
title: orgs_enabled_for_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orgs_enabled_for_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.orgs_enabled_for_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `organizations` | `array` |
| `total_count` | `number` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_selected_organizations_enabled_github_actions_enterprise` | `SELECT` | `enterprise` | Lists the organizations that are selected to have GitHub Actions enabled in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."<br /><br />You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint. |
| `disable_selected_organization_github_actions_enterprise` | `EXEC` | `enterprise, org_id` | Removes an organization from the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."<br /><br />You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint. |
| `enable_selected_organization_github_actions_enterprise` | `EXEC` | `enterprise, org_id` | Adds an organization to the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."<br /><br />You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint. |
| `set_selected_organizations_enabled_github_actions_enterprise` | `EXEC` | `enterprise, data__selected_organization_ids` | Replaces the list of selected organizations that are enabled for GitHub Actions in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."<br /><br />You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint. |
