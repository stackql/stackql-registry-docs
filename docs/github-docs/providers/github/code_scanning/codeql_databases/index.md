---
title: codeql_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - codeql_databases
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
<tr><td><b>Name</b></td><td><code>codeql_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.codeql_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the CodeQL database. |
| `name` | `string` | The name of the CodeQL database. |
| `content_type` | `string` | The MIME type of the CodeQL database file. |
| `updated_at` | `string` | The date and time at which the CodeQL database was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `created_at` | `string` | The date and time at which the CodeQL database was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `language` | `string` | The language of the CodeQL database. |
| `size` | `integer` | The size of the CodeQL database file in bytes. |
| `uploader` | `object` | A GitHub user. |
| `url` | `string` | The URL at which to download the CodeQL database. The `Accept` header must be set to the value of the `content_type` property. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_codeql_database` | `SELECT` | `language, owner, repo` | Gets a CodeQL database for a language in a repository.<br /><br />By default this endpoint returns JSON metadata about the CodeQL database. To<br />download the CodeQL database binary content, set the `Accept` header of the request<br />to [`application/zip`](https://docs.github.com/rest/overview/media-types), and make sure<br />your HTTP client is configured to follow redirects or use the `Location` header<br />to make a second request to get the redirect URL.<br /><br />For private repositories, you must use an access token with the `security_events` scope.<br />For public repositories, you can use tokens with the `security_events` or `public_repo` scope.<br />GitHub Apps must have the `contents` read permission to use this endpoint. |
| `list_codeql_databases` | `SELECT` | `owner, repo` | Lists the CodeQL databases that are available in a repository.<br /><br />For private repositories, you must use an access token with the `security_events` scope.<br />For public repositories, you can use tokens with the `security_events` or `public_repo` scope.<br />GitHub Apps must have the `contents` read permission to use this endpoint. |
