---
title: spot_datafeed_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_datafeed_subscription
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
<tr><td><b>Name</b></td><td><code>spot_datafeed_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.spot_datafeed_subscription" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bucket" /> | `string` | The name of the Amazon S3 bucket where the Spot Instance data feed is located. |
| <CopyableCode code="fault" /> | `object` | Describes a Spot Instance state change. |
| <CopyableCode code="ownerId" /> | `string` | The Amazon Web Services account ID of the account. |
| <CopyableCode code="prefix" /> | `string` | The prefix for the data feed files. |
| <CopyableCode code="state" /> | `string` | The state of the Spot Instance data feed subscription. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="spot_datafeed_subscription_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the data feed for Spot Instances. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html"&gt;Spot Instance data feed&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;. |
| <CopyableCode code="spot_datafeed_subscription_Create" /> | `INSERT` | <CopyableCode code="Bucket, region" /> | Creates a data feed for Spot Instances, enabling you to view Spot Instance usage logs. You can create one data feed per Amazon Web Services account. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html"&gt;Spot Instance data feed&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;. |
| <CopyableCode code="spot_datafeed_subscription_Delete" /> | `DELETE` | <CopyableCode code="region" /> | Deletes the data feed for Spot Instances. |
