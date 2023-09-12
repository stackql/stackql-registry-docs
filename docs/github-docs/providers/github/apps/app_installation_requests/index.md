---
title: app_installation_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - app_installation_requests
  - apps
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
<tr><td><b>Name</b></td><td><code>app_installation_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.app_installation_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the request installation. |
| `requester` | `object` | A GitHub user. |
| `account` | `object` | A GitHub user. |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_installation_requests_for_authenticated_app` | `SELECT` |  |
