---
title: spot_datafeed_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_datafeed_subscription
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
<tr><td><b>Name</b></td><td><code>spot_datafeed_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.spot_datafeed_subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | The state of the Spot Instance data feed subscription. |
| `bucket` | `string` | The name of the Amazon S3 bucket where the Spot Instance data feed is located. |
| `fault` | `object` | Describes a Spot Instance state change. |
| `ownerId` | `string` | The Amazon Web Services account ID of the account. |
| `prefix` | `string` | The prefix for the data feed files. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `spot_datafeed_subscription_Describe` | `SELECT` |  | Describes the data feed for Spot Instances. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html"&gt;Spot Instance data feed&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;. |
| `spot_datafeed_subscription_Create` | `INSERT` | `Bucket` | Creates a data feed for Spot Instances, enabling you to view Spot Instance usage logs. You can create one data feed per Amazon Web Services account. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html"&gt;Spot Instance data feed&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;. |
| `spot_datafeed_subscription_Delete` | `DELETE` |  | Deletes the data feed for Spot Instances. |
