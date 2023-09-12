---
title: repos_default_setup
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_default_setup
  - code_scanning
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
<tr><td><b>Name</b></td><td><code>repos_default_setup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.repos_default_setup</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | Code scanning default setup has been configured or not. |
| `updated_at` | `string` | Timestamp of latest configuration update. |
| `languages` | `array` | Languages to be analysed. |
| `query_suite` | `string` | CodeQL query suite to be used. |
| `schedule` | `string` | The frequency of the periodic analysis. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_default_setup` | `SELECT` | `owner, repo` | Gets a code scanning default setup configuration.<br />You must use an access token with the `repo` scope to use this endpoint with private repos or the `public_repo`<br />scope for public repos. GitHub Apps must have the `repo` write permission to use this endpoint. |
| `update_default_setup` | `EXEC` | `owner, repo, data__state` | Updates a code scanning default setup configuration.<br />You must use an access token with the `repo` scope to use this endpoint with private repos or the `public_repo`<br />scope for public repos. GitHub Apps must have the `repo` write permission to use this endpoint. |
