---
title: default_workflow_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - actions
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>default_workflow_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.default_workflow_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `default_workflow_permissions` | `string` | The default workflow permissions granted to the GITHUB_TOKEN when running workflows in an organization. |
| `can_approve_pull_request_reviews` | `boolean` | Whether GitHub Actions can submit approving pull request reviews. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_github_actions_default_workflow_permissions_organization` | `SELECT` | `org` | Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an organization,<br />as well if GitHub Actions can submit approving pull request reviews.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `set_github_actions_default_workflow_permissions_organization` | `EXEC` | `org` | Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an organization, and sets if GitHub Actions<br />can submit approving pull request reviews.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
