---
title: git_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - git_namespaces
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
<tr><td><b>Name</b></td><td><code>git_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.integrations.git_namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `` |
| `name` | `string` |
| `installationId` | `number` |
| `isAccessRestricted` | `boolean` |
| `ownerType` | `string` |
| `provider` | `string` |
| `requireReauth` | `boolean` |
| `slug` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `git_namespaces` | `SELECT` | `teamId` |
