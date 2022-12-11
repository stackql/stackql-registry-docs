---
title: network_insights_access_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scopes
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
<tr><td><b>Name</b></td><td><code>network_insights_access_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_insights_access_scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `networkInsightsAccessScopeArn` | `string` | The Amazon Resource Name (ARN) of the Network Access Scope. |
| `networkInsightsAccessScopeId` | `string` | The ID of the Network Access Scope. |
| `tagSet` | `array` | The tags. |
| `updatedDate` | `string` | The last updated date. |
| `createdDate` | `string` | The creation date. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `network_insights_access_scopes_Describe` | `SELECT` |  | Describes the specified Network Access Scopes. |
| `network_insights_access_scope_Create` | `INSERT` | `ClientToken` | &lt;p&gt;Creates a Network Access Scope.&lt;/p&gt; &lt;p&gt;Amazon Web Services Network Access Analyzer enables cloud networking and cloud operations teams to verify that their networks on Amazon Web Services conform to their network security and governance objectives. For more information, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/"&gt;Amazon Web Services Network Access Analyzer Guide&lt;/a&gt;.&lt;/p&gt; |
| `network_insights_access_scope_Delete` | `DELETE` | `NetworkInsightsAccessScopeId` | Deletes the specified Network Access Scope. |
