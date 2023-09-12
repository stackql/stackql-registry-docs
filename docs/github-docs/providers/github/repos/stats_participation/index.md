---
title: stats_participation
hide_title: false
hide_table_of_contents: false
keywords:
  - stats_participation
  - repos
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
<tr><td><b>Name</b></td><td><code>stats_participation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.stats_participation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `all` | `array` |
| `owner` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_participation_stats` | `SELECT` | `owner, repo` |
