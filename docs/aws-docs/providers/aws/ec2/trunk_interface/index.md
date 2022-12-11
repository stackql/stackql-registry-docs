---
title: trunk_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - trunk_interface
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
<tr><td><b>Name</b></td><td><code>trunk_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.trunk_interface</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `trunk_interface_Associate` | `EXEC` | `BranchInterfaceId, TrunkInterfaceId` | &lt;note&gt; &lt;p&gt;This API action is currently in &lt;b&gt;limited preview only&lt;/b&gt;. If you are interested in using this feature, contact your account manager.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Associates a branch network interface with a trunk network interface.&lt;/p&gt; &lt;p&gt;Before you create the association, run the &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html"&gt;create-network-interface&lt;/a&gt; command and set &lt;code&gt;--interface-type&lt;/code&gt; to &lt;code&gt;trunk&lt;/code&gt;. You must also create a network interface for each branch network interface that you want to associate with the trunk network interface.&lt;/p&gt; |
| `trunk_interface_Disassociate` | `EXEC` | `AssociationId` | &lt;note&gt; &lt;p&gt;This API action is currently in &lt;b&gt;limited preview only&lt;/b&gt;. If you are interested in using this feature, contact your account manager.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Removes an association between a branch network interface with a trunk network interface.&lt;/p&gt; |
