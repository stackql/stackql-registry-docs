---
title: id_format
hide_title: false
hide_table_of_contents: false
keywords:
  - id_format
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
<tr><td><b>Name</b></td><td><code>id_format</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.id_format</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resource` | `string` | The type of resource. |
| `useLongIds` | `boolean` | Indicates whether longer IDs (17-character IDs) are enabled for the resource. |
| `deadline` | `string` | The date in UTC at which you are permanently switched over to using longer IDs. If a deadline is not yet available for this resource type, this field is not returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `id_format_Describe` | `SELECT` |  | &lt;p&gt;Describes the ID format settings for your resources on a per-Region basis, for example, to view which resource types are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types.&lt;/p&gt; &lt;p&gt;The following resource types support longer IDs: &lt;code&gt;bundle&lt;/code&gt; \| &lt;code&gt;conversion-task&lt;/code&gt; \| &lt;code&gt;customer-gateway&lt;/code&gt; \| &lt;code&gt;dhcp-options&lt;/code&gt; \| &lt;code&gt;elastic-ip-allocation&lt;/code&gt; \| &lt;code&gt;elastic-ip-association&lt;/code&gt; \| &lt;code&gt;export-task&lt;/code&gt; \| &lt;code&gt;flow-log&lt;/code&gt; \| &lt;code&gt;image&lt;/code&gt; \| &lt;code&gt;import-task&lt;/code&gt; \| &lt;code&gt;instance&lt;/code&gt; \| &lt;code&gt;internet-gateway&lt;/code&gt; \| &lt;code&gt;network-acl&lt;/code&gt; \| &lt;code&gt;network-acl-association&lt;/code&gt; \| &lt;code&gt;network-interface&lt;/code&gt; \| &lt;code&gt;network-interface-attachment&lt;/code&gt; \| &lt;code&gt;prefix-list&lt;/code&gt; \| &lt;code&gt;reservation&lt;/code&gt; \| &lt;code&gt;route-table&lt;/code&gt; \| &lt;code&gt;route-table-association&lt;/code&gt; \| &lt;code&gt;security-group&lt;/code&gt; \| &lt;code&gt;snapshot&lt;/code&gt; \| &lt;code&gt;subnet&lt;/code&gt; \| &lt;code&gt;subnet-cidr-block-association&lt;/code&gt; \| &lt;code&gt;volume&lt;/code&gt; \| &lt;code&gt;vpc&lt;/code&gt; \| &lt;code&gt;vpc-cidr-block-association&lt;/code&gt; \| &lt;code&gt;vpc-endpoint&lt;/code&gt; \| &lt;code&gt;vpc-peering-connection&lt;/code&gt; \| &lt;code&gt;vpn-connection&lt;/code&gt; \| &lt;code&gt;vpn-gateway&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;These settings apply to the IAM user who makes the request; they do not apply to the entire Amazon Web Services account. By default, an IAM user defaults to the same settings as the root user, unless they explicitly override the settings by running the &lt;a&gt;ModifyIdFormat&lt;/a&gt; command. Resources created with longer IDs are visible to all IAM users, regardless of these settings and provided that they have permission to use the relevant &lt;code&gt;Describe&lt;/code&gt; command for the resource type.&lt;/p&gt; |
| `id_format_Modify` | `EXEC` | `Resource, UseLongIds` | &lt;p&gt;Modifies the ID format for the specified resource on a per-Region basis. You can specify that resources should receive longer IDs (17-character IDs) when they are created.&lt;/p&gt; &lt;p&gt;This request can only be used to modify longer ID settings for resource types that are within the opt-in period. Resources currently in their opt-in period include: &lt;code&gt;bundle&lt;/code&gt; \| &lt;code&gt;conversion-task&lt;/code&gt; \| &lt;code&gt;customer-gateway&lt;/code&gt; \| &lt;code&gt;dhcp-options&lt;/code&gt; \| &lt;code&gt;elastic-ip-allocation&lt;/code&gt; \| &lt;code&gt;elastic-ip-association&lt;/code&gt; \| &lt;code&gt;export-task&lt;/code&gt; \| &lt;code&gt;flow-log&lt;/code&gt; \| &lt;code&gt;image&lt;/code&gt; \| &lt;code&gt;import-task&lt;/code&gt; \| &lt;code&gt;internet-gateway&lt;/code&gt; \| &lt;code&gt;network-acl&lt;/code&gt; \| &lt;code&gt;network-acl-association&lt;/code&gt; \| &lt;code&gt;network-interface&lt;/code&gt; \| &lt;code&gt;network-interface-attachment&lt;/code&gt; \| &lt;code&gt;prefix-list&lt;/code&gt; \| &lt;code&gt;route-table&lt;/code&gt; \| &lt;code&gt;route-table-association&lt;/code&gt; \| &lt;code&gt;security-group&lt;/code&gt; \| &lt;code&gt;subnet&lt;/code&gt; \| &lt;code&gt;subnet-cidr-block-association&lt;/code&gt; \| &lt;code&gt;vpc&lt;/code&gt; \| &lt;code&gt;vpc-cidr-block-association&lt;/code&gt; \| &lt;code&gt;vpc-endpoint&lt;/code&gt; \| &lt;code&gt;vpc-peering-connection&lt;/code&gt; \| &lt;code&gt;vpn-connection&lt;/code&gt; \| &lt;code&gt;vpn-gateway&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;This setting applies to the IAM user who makes the request; it does not apply to the entire Amazon Web Services account. By default, an IAM user defaults to the same settings as the root user. If you're using this action as the root user, then these settings apply to the entire account, unless an IAM user explicitly overrides these settings for themselves. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html"&gt;Resource IDs&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Resources created with longer IDs are visible to all IAM roles and users, regardless of these settings and provided that they have permission to use the relevant &lt;code&gt;Describe&lt;/code&gt; command for the resource type.&lt;/p&gt; |
