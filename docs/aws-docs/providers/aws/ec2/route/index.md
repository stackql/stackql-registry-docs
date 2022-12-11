---
title: route
hide_title: false
hide_table_of_contents: false
keywords:
  - route
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
<tr><td><b>Name</b></td><td><code>route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.route</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `route_Create` | `INSERT` | `RouteTableId` | &lt;p&gt;Creates a route in a route table within a VPC.&lt;/p&gt; &lt;p&gt;You must specify one of the following targets: internet gateway or virtual private gateway, NAT instance, NAT gateway, VPC peering connection, network interface, egress-only internet gateway, or transit gateway.&lt;/p&gt; &lt;p&gt;When determining how to route traffic, we use the route with the most specific match. For example, traffic is destined for the IPv4 address &lt;code&gt;192.0.2.3&lt;/code&gt;, and the route table includes the following two IPv4 routes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;192.0.2.0/24&lt;/code&gt; (goes to some target A)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;192.0.2.0/28&lt;/code&gt; (goes to some target B)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Both routes apply to the traffic destined for &lt;code&gt;192.0.2.3&lt;/code&gt;. However, the second route in the list covers a smaller number of IP addresses and is therefore more specific, so we use that route to determine where to target the traffic.&lt;/p&gt; &lt;p&gt;For more information about route tables, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"&gt;Route tables&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `route_Delete` | `DELETE` | `RouteTableId` | Deletes the specified route from the specified route table. |
| `route_Replace` | `EXEC` | `RouteTableId` | &lt;p&gt;Replaces an existing route within a route table in a VPC. You must provide only one of the following: internet gateway, virtual private gateway, NAT instance, NAT gateway, VPC peering connection, network interface, egress-only internet gateway, or transit gateway.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"&gt;Route tables&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
