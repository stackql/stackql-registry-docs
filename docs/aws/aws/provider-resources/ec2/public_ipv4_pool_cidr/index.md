---
title: public_ipv4_pool_cidr
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ipv4_pool_cidr
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
<tr><td><b>Name</b></td><td><code>public_ipv4_pool_cidr</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.public_ipv4_pool_cidr</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `public_ipv4_pool_cidr_Deprovision` | `EXEC` | `Cidr, PoolId` | Deprovision a CIDR from a public IPv4 pool. |
| `public_ipv4_pool_cidr_Provision` | `EXEC` | `IpamPoolId, NetmaskLength, PoolId` | &lt;p&gt;Provision a CIDR to a public IPv4 pool.&lt;/p&gt; &lt;p&gt;For more information about IPAM, see &lt;a href="/vpc/latest/ipam/what-is-it-ipam.html"&gt;What is IPAM?&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.&lt;/p&gt; |
