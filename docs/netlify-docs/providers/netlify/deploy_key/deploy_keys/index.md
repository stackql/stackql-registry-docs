---
title: deploy_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - deploy_keys
  - deploy_key
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deploy_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy_key.deploy_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `created_at` | `string` |
| `public_key` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDeployKey` | `SELECT` | `key_id` |
| `listDeployKeys` | `SELECT` |  |
| `createDeployKey` | `INSERT` |  |
| `deleteDeployKey` | `DELETE` | `key_id` |
