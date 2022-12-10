---
title: identity_id_format
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_id_format
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
<tr><td><b>Name</b></td><td><code>identity_id_format</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.identity_id_format</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `useLongIds` | `boolean` | Indicates whether longer IDs (17-character IDs) are enabled for the resource. |
| `deadline` | `string` | The date in UTC at which you are permanently switched over to using longer IDs. If a deadline is not yet available for this resource type, this field is not returned. |
| `resource` | `string` | The type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `identity_id_format_Describe` | `SELECT` | `PrincipalArn` | &lt;p&gt;Describes the ID format settings for resources for the specified IAM user, IAM role, or root user. For example, you can view the resource types that are enabled for longer IDs. This request only returns information about resource types whose ID formats can be modified; it does not return information about other resource types. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html"&gt;Resource IDs&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;The following resource types support longer IDs: &lt;code&gt;bundle&lt;/code&gt; \| &lt;code&gt;conversion-task&lt;/code&gt; \| &lt;code&gt;customer-gateway&lt;/code&gt; \| &lt;code&gt;dhcp-options&lt;/code&gt; \| &lt;code&gt;elastic-ip-allocation&lt;/code&gt; \| &lt;code&gt;elastic-ip-association&lt;/code&gt; \| &lt;code&gt;export-task&lt;/code&gt; \| &lt;code&gt;flow-log&lt;/code&gt; \| &lt;code&gt;image&lt;/code&gt; \| &lt;code&gt;import-task&lt;/code&gt; \| &lt;code&gt;instance&lt;/code&gt; \| &lt;code&gt;internet-gateway&lt;/code&gt; \| &lt;code&gt;network-acl&lt;/code&gt; \| &lt;code&gt;network-acl-association&lt;/code&gt; \| &lt;code&gt;network-interface&lt;/code&gt; \| &lt;code&gt;network-interface-attachment&lt;/code&gt; \| &lt;code&gt;prefix-list&lt;/code&gt; \| &lt;code&gt;reservation&lt;/code&gt; \| &lt;code&gt;route-table&lt;/code&gt; \| &lt;code&gt;route-table-association&lt;/code&gt; \| &lt;code&gt;security-group&lt;/code&gt; \| &lt;code&gt;snapshot&lt;/code&gt; \| &lt;code&gt;subnet&lt;/code&gt; \| &lt;code&gt;subnet-cidr-block-association&lt;/code&gt; \| &lt;code&gt;volume&lt;/code&gt; \| &lt;code&gt;vpc&lt;/code&gt; \| &lt;code&gt;vpc-cidr-block-association&lt;/code&gt; \| &lt;code&gt;vpc-endpoint&lt;/code&gt; \| &lt;code&gt;vpc-peering-connection&lt;/code&gt; \| &lt;code&gt;vpn-connection&lt;/code&gt; \| &lt;code&gt;vpn-gateway&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;These settings apply to the principal specified in the request. They do not apply to the principal that makes the request.&lt;/p&gt; |
| `identity_id_format_Modify` | `EXEC` | `PrincipalArn, Resource, UseLongIds` | &lt;p&gt;Modifies the ID format of a resource for a specified IAM user, IAM role, or the root user for an account; or all IAM users, IAM roles, and the root user for an account. You can specify that resources should receive longer IDs (17-character IDs) when they are created. &lt;/p&gt; &lt;p&gt;This request can only be used to modify longer ID settings for resource types that are within the opt-in period. Resources currently in their opt-in period include: &lt;code&gt;bundle&lt;/code&gt; \| &lt;code&gt;conversion-task&lt;/code&gt; \| &lt;code&gt;customer-gateway&lt;/code&gt; \| &lt;code&gt;dhcp-options&lt;/code&gt; \| &lt;code&gt;elastic-ip-allocation&lt;/code&gt; \| &lt;code&gt;elastic-ip-association&lt;/code&gt; \| &lt;code&gt;export-task&lt;/code&gt; \| &lt;code&gt;flow-log&lt;/code&gt; \| &lt;code&gt;image&lt;/code&gt; \| &lt;code&gt;import-task&lt;/code&gt; \| &lt;code&gt;internet-gateway&lt;/code&gt; \| &lt;code&gt;network-acl&lt;/code&gt; \| &lt;code&gt;network-acl-association&lt;/code&gt; \| &lt;code&gt;network-interface&lt;/code&gt; \| &lt;code&gt;network-interface-attachment&lt;/code&gt; \| &lt;code&gt;prefix-list&lt;/code&gt; \| &lt;code&gt;route-table&lt;/code&gt; \| &lt;code&gt;route-table-association&lt;/code&gt; \| &lt;code&gt;security-group&lt;/code&gt; \| &lt;code&gt;subnet&lt;/code&gt; \| &lt;code&gt;subnet-cidr-block-association&lt;/code&gt; \| &lt;code&gt;vpc&lt;/code&gt; \| &lt;code&gt;vpc-cidr-block-association&lt;/code&gt; \| &lt;code&gt;vpc-endpoint&lt;/code&gt; \| &lt;code&gt;vpc-peering-connection&lt;/code&gt; \| &lt;code&gt;vpn-connection&lt;/code&gt; \| &lt;code&gt;vpn-gateway&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resource-ids.html"&gt;Resource IDs&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;This setting applies to the principal specified in the request; it does not apply to the principal that makes the request. &lt;/p&gt; &lt;p&gt;Resources created with longer IDs are visible to all IAM roles and users, regardless of these settings and provided that they have permission to use the relevant &lt;code&gt;Describe&lt;/code&gt; command for the resource type.&lt;/p&gt; |
