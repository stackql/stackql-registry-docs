---
title: fleet_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet_instances
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
<tr><td><b>Name</b></td><td><code>fleet_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.fleet_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="instanceHealth" /> | `string` | The health status of the instance. If the status of either the instance status check or the system status check is &lt;code&gt;impaired&lt;/code&gt;, the health status of the instance is &lt;code&gt;unhealthy&lt;/code&gt;. Otherwise, the health status is &lt;code&gt;healthy&lt;/code&gt;. |
| <CopyableCode code="instanceId" /> | `string` | The ID of the instance. |
| <CopyableCode code="instanceType" /> | `string` | The instance type. |
| <CopyableCode code="spotInstanceRequestId" /> | `string` | The ID of the Spot Instance request. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="fleet_instances_Describe" /> | `SELECT` | <CopyableCode code="FleetId, region" /> |
