---
title: managed_prefix_list_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_prefix_list_entries
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_prefix_list_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.managed_prefix_list_entries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description. |
| `cidr` | `string` | The CIDR block. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `managed_prefix_list_entries_Get` | `SELECT` | `PrefixListId` |
