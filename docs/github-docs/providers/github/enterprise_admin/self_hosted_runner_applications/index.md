---
title: self_hosted_runner_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - self_hosted_runner_applications
  - enterprise_admin
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
<tr><td><b>Name</b></td><td><code>self_hosted_runner_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.self_hosted_runner_applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `filename` | `string` |  |
| `os` | `string` |  |
| `sha256_checksum` | `string` |  |
| `temp_download_token` | `string` | A short lived bearer token used to download the runner, if needed. |
| `architecture` | `string` |  |
| `download_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_runner_applications_for_enterprise` | `SELECT` | `enterprise` |
