---
title: search_repo
hide_title: false
hide_table_of_contents: false
keywords:
  - search_repo
  - integrations
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>search_repo</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.integrations.search_repo</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `gitAccount` | `object` |
| `repos` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `git_namespaces` | `SELECT` | `teamId` |
