---
title: statistics_contributor_activity
hide_title: false
hide_table_of_contents: false
keywords:
  - statistics_contributor_activity
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
<tr><td><b>Name</b></td><td><code>statistics_contributor_activity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.statistics_contributor_activity</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `total` | `integer` |  |
| `weeks` | `array` |  |
| `author` | `object` | Simple User |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_contributors_stats` | `SELECT` | `owner, repo` |
