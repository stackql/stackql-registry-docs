---
title: orgs_runners_downloads
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_runners_downloads
  - actions
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
<tr><td><b>Name</b></td><td><code>orgs_runners_downloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.orgs_runners_downloads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `os` | `string` |  |
| `sha256_checksum` | `string` |  |
| `temp_download_token` | `string` | A short lived bearer token used to download the runner, if needed. |
| `architecture` | `string` |  |
| `download_url` | `string` |  |
| `filename` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_runner_applications_for_org` | `SELECT` | `org` |
