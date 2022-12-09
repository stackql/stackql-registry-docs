---
title: ipam_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_scopes
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
<tr><td><b>Name</b></td><td><code>ipam_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the scope. |
| `ipamArn` | `string` | The ARN of the IPAM. |
| `ownerId` | `string` | The Amazon Web Services account ID of the owner of the scope. |
| `ipamRegion` | `string` | The Amazon Web Services Region of the IPAM scope. |
| `isDefault` | `boolean` | Defines if the scope is the default scope or not. |
| `state` | `string` | The state of the IPAM scope. |
| `ipamScopeArn` | `string` | The ARN of the scope. |
| `ipamScopeId` | `string` | The ID of the scope. |
| `ipamScopeType` | `string` | The type of the scope. |
| `poolCount` | `integer` | The number of pools in the scope. |
| `tagSet` | `array` | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key &lt;code&gt;Owner&lt;/code&gt; and the value &lt;code&gt;TeamA&lt;/code&gt;, specify &lt;code&gt;tag:Owner&lt;/code&gt; for the filter name and &lt;code&gt;TeamA&lt;/code&gt; for the filter value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ipam_scopes_Describe` | `SELECT` |  | Get information about your IPAM scopes. |
| `ipam_scope_Create` | `INSERT` | `IpamId` | &lt;p&gt;Create an IPAM scope. In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/add-scope-ipam.html"&gt;Add a scope&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ipam_scope_Delete` | `DELETE` | `IpamScopeId` | &lt;p&gt;Delete the scope for an IPAM. You cannot delete the default scopes.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/delete-scope-ipam.html"&gt;Delete a scope&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| `ipam_scope_Modify` | `EXEC` | `IpamScopeId` | Modify an IPAM scope. |
