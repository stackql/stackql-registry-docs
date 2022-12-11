---
title: managed_prefix_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_prefix_lists
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
<tr><td><b>Name</b></td><td><code>managed_prefix_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.managed_prefix_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `stateMessage` | `string` | The state message. |
| `state` | `string` | The current state of the prefix list. |
| `prefixListId` | `string` | The ID of the prefix list. |
| `maxEntries` | `integer` | The maximum number of entries for the prefix list. |
| `prefixListArn` | `string` | The Amazon Resource Name (ARN) for the prefix list. |
| `version` | `integer` | The version of the prefix list. |
| `prefixListName` | `string` | The name of the prefix list. |
| `ownerId` | `string` | The ID of the owner of the prefix list. |
| `tagSet` | `array` | The tags for the prefix list. |
| `addressFamily` | `string` | The IP address version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `managed_prefix_lists_Describe` | `SELECT` |  | &lt;p&gt;Describes your managed prefix lists and any Amazon Web Services-managed prefix lists.&lt;/p&gt; &lt;p&gt;To view the entries for your prefix list, use &lt;a&gt;GetManagedPrefixListEntries&lt;/a&gt;.&lt;/p&gt; |
| `managed_prefix_list_Create` | `INSERT` | `AddressFamily, MaxEntries, PrefixListName` | Creates a managed prefix list. You can specify one or more entries for the prefix list. Each entry consists of a CIDR block and an optional description. |
| `managed_prefix_list_Delete` | `DELETE` | `PrefixListId` | Deletes the specified managed prefix list. You must first remove all references to the prefix list in your resources. |
| `managed_prefix_list_Modify` | `EXEC` | `PrefixListId` | &lt;p&gt;Modifies the specified managed prefix list.&lt;/p&gt; &lt;p&gt;Adding or removing entries in a prefix list creates a new version of the prefix list. Changing the name of the prefix list does not affect the version.&lt;/p&gt; &lt;p&gt;If you specify a current version number that does not match the true current version number, the request fails.&lt;/p&gt; |
