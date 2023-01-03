---
title: self_hosted_runner_applications
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
<tr><td><b>Name</b></td><td><code>self_hosted_runner_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.self_hosted_runner_applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `temp_download_token` | `string` | A short lived bearer token used to download the runner, if needed. |
| `architecture` | `string` |  |
| `download_url` | `string` |  |
| `filename` | `string` |  |
| `os` | `string` |  |
| `sha256_checksum` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_runner_applications_for_org` | `SELECT` | `org` | Lists binaries for the runner application that you can download and run.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `list_runner_applications_for_repo` | `SELECT` | `owner, repo` | Lists binaries for the runner application that you can download and run.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. |
