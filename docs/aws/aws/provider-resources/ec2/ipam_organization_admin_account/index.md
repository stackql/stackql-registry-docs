---
title: ipam_organization_admin_account
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_organization_admin_account
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
<tr><td><b>Name</b></td><td><code>ipam_organization_admin_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipam_organization_admin_account</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ipam_organization_admin_account_Disable` | `EXEC` | `DelegatedAdminAccountId` | Disable the IPAM account. For more information, see &lt;a href="/vpc/latest/ipam/enable-integ-ipam.html"&gt;Enable integration with Organizations&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.  |
| `ipam_organization_admin_account_Enable` | `EXEC` | `DelegatedAdminAccountId` | Enable an Organizations member account as the IPAM admin account. You cannot select the Organizations management account as the IPAM admin account. For more information, see &lt;a href="/vpc/latest/ipam/enable-integ-ipam.html"&gt;Enable integration with Organizations&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.  |
