---
title: codes_of_conduct
hide_title: false
hide_table_of_contents: false
keywords:
  - codes_of_conduct
  - codes_of_conduct
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
<tr><td><b>Name</b></td><td><code>codes_of_conduct</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codes_of_conduct.codes_of_conduct</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `body` | `string` |
| `html_url` | `string` |
| `key` | `string` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_all_codes_of_conduct` | `SELECT` |  | Returns array of all GitHub's codes of conduct. |
| `get_conduct_code` | `SELECT` | `key` | Returns information about the specified GitHub code of conduct. |
