---
title: dependency_review
hide_title: false
hide_table_of_contents: false
keywords:
  - dependency_review
  - dependency_graph
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
<tr><td><b>Name</b></td><td><code>dependency_review</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.dependency_graph.dependency_review</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` |  |
| `package_url` | `string` |  |
| `scope` | `string` | Where the dependency is utilized. `development` means that the dependency is only utilized in the development environment. `runtime` means that the dependency is utilized at runtime and in the development environment. |
| `license` | `string` |  |
| `manifest` | `string` |  |
| `vulnerabilities` | `array` |  |
| `source_repository_url` | `string` |  |
| `change_type` | `string` |  |
| `ecosystem` | `string` |  |
| `version` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `diff_range` | `SELECT` | `basehead, owner, repo` |
