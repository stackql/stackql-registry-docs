---
title: spot_placement_scores
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_placement_scores
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
<tr><td><b>Name</b></td><td><code>spot_placement_scores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.spot_placement_scores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availabilityZoneId" /> | `string` | The Availability Zone. |
| <CopyableCode code="region" /> | `string` | The Region. |
| <CopyableCode code="score" /> | `integer` | The placement score, on a scale from &lt;code&gt;1&lt;/code&gt; to &lt;code&gt;10&lt;/code&gt;. A score of &lt;code&gt;10&lt;/code&gt; indicates that your Spot request is highly likely to succeed in this Region or Availability Zone. A score of &lt;code&gt;1&lt;/code&gt; indicates that your Spot request is not likely to succeed.  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="spot_placement_scores_Get" /> | `SELECT` | <CopyableCode code="TargetCapacity, region" /> |
