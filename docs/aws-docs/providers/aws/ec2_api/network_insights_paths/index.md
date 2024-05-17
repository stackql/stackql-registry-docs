---
title: network_insights_paths
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_paths
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_insights_paths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createdDate" /> | `string` | The time stamp when the path was created. |
| <CopyableCode code="destination" /> | `string` | The Amazon Web Services resource that is the destination of the path. |
| <CopyableCode code="destinationIp" /> | `string` | The IP address of the Amazon Web Services resource that is the destination of the path. |
| <CopyableCode code="destinationPort" /> | `integer` | The destination port. |
| <CopyableCode code="networkInsightsPathArn" /> | `string` | The Amazon Resource Name (ARN) of the path. |
| <CopyableCode code="networkInsightsPathId" /> | `string` | The ID of the path. |
| <CopyableCode code="protocol" /> | `string` | The protocol. |
| <CopyableCode code="source" /> | `string` | The Amazon Web Services resource that is the source of the path. |
| <CopyableCode code="sourceIp" /> | `string` | The IP address of the Amazon Web Services resource that is the source of the path. |
| <CopyableCode code="tagSet" /> | `array` | The tags associated with the path. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="network_insights_paths_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more of your paths. |
| <CopyableCode code="network_insights_path_Create" /> | `INSERT` | <CopyableCode code="ClientToken, Destination, Protocol, Source, region" /> | &lt;p&gt;Creates a path to analyze for reachability.&lt;/p&gt; &lt;p&gt;Reachability Analyzer enables you to analyze and debug network reachability between two resources in your virtual private cloud (VPC). For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/reachability/"&gt;What is Reachability Analyzer&lt;/a&gt;.&lt;/p&gt; |
| <CopyableCode code="network_insights_path_Delete" /> | `DELETE` | <CopyableCode code="NetworkInsightsPathId, region" /> | Deletes the specified path. |
