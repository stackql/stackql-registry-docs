---
title: network_insights_paths
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_paths
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_insights_paths</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `destinationIp` | `string` | The IP address of the Amazon Web Services resource that is the destination of the path. |
| `createdDate` | `string` | The time stamp when the path was created. |
| `sourceIp` | `string` | The IP address of the Amazon Web Services resource that is the source of the path. |
| `destinationPort` | `integer` | The destination port. |
| `destination` | `string` | The Amazon Web Services resource that is the destination of the path. |
| `networkInsightsPathId` | `string` | The ID of the path. |
| `source` | `string` | The Amazon Web Services resource that is the source of the path. |
| `networkInsightsPathArn` | `string` | The Amazon Resource Name (ARN) of the path. |
| `tagSet` | `array` | The tags associated with the path. |
| `protocol` | `string` | The protocol. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `network_insights_paths_Describe` | `SELECT` | `region` | Describes one or more of your paths. |
| `network_insights_path_Create` | `INSERT` | `ClientToken, Destination, Protocol, Source, region` | &lt;p&gt;Creates a path to analyze for reachability.&lt;/p&gt; &lt;p&gt;Reachability Analyzer enables you to analyze and debug network reachability between two resources in your virtual private cloud (VPC). For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/reachability/"&gt;What is Reachability Analyzer&lt;/a&gt;.&lt;/p&gt; |
| `network_insights_path_Delete` | `DELETE` | `NetworkInsightsPathId, region` | Deletes the specified path. |
