---
title: route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - route_tables
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
<tr><td><b>Name</b></td><td><code>route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.route_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the route table. |
| `propagatingVgwSet` | `array` | Any virtual private gateway (VGW) propagating routes. |
| `routeSet` | `array` | The routes in the route table. |
| `routeTableId` | `string` | The ID of the route table. |
| `tagSet` | `array` | Any tags assigned to the route table. |
| `vpcId` | `string` | The ID of the VPC. |
| `associationSet` | `array` | The associations between the route table and one or more subnets or a gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `route_tables_Describe` | `SELECT` |  | &lt;p&gt;Describes one or more of your route tables.&lt;/p&gt; &lt;p&gt;Each subnet in your VPC must be associated with a route table. If a subnet is not explicitly associated with any route table, it is implicitly associated with the main route table. This command does not return the subnet ID for implicit associations.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"&gt;Route tables&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `route_table_Create` | `INSERT` | `VpcId` | &lt;p&gt;Creates a route table for the specified VPC. After you create a route table, you can add routes and associate the table with a subnet.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"&gt;Route tables&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `route_table_Delete` | `DELETE` | `RouteTableId` | Deletes the specified route table. You must disassociate the route table from any subnets before you can delete it. You can't delete the main route table. |
| `route_table_Associate` | `EXEC` | `RouteTableId` | &lt;p&gt;Associates a subnet in your VPC or an internet gateway or virtual private gateway attached to your VPC with a route table in your VPC. This association causes traffic from the subnet or gateway to be routed according to the routes in the route table. The action returns an association ID, which you need in order to disassociate the route table later. A route table can be associated with multiple subnets.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"&gt;Route tables&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `route_table_Disassociate` | `EXEC` | `AssociationId` | &lt;p&gt;Disassociates a subnet or gateway from a route table.&lt;/p&gt; &lt;p&gt;After you perform this action, the subnet no longer uses the routes in the route table. Instead, it uses the routes in the VPC's main route table. For more information about route tables, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"&gt;Route tables&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
