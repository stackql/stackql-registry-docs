---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - certificates
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.certificates.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `createdAt` | `string` | Date action created |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `certificate_action_retrieve` | `SELECT` | `certificate_id` |
