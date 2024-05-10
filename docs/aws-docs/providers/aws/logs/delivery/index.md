---
title: delivery
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery
  - logs
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>delivery</code> resource, use <code>deliveries</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This structure contains information about one delivery in your account.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;A delivery is a connection between a logical delivery source and a logical delivery destination.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For more information, see &#91;CreateDelivery&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonCloudWatchLogs&#x2F;latest&#x2F;APIReference&#x2F;API_CreateDelivery.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.delivery" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="delivery_id" /></td><td><code>string</code></td><td>The unique ID that identifies this delivery in your account.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that uniquely identifies this delivery.</td></tr>
<tr><td><CopyableCode code="delivery_source_name" /></td><td><code>string</code></td><td>The name of the delivery source that is associated with this delivery.</td></tr>
<tr><td><CopyableCode code="delivery_destination_arn" /></td><td><code>string</code></td><td>The ARN of the delivery destination that is associated with this delivery.</td></tr>
<tr><td><CopyableCode code="delivery_destination_type" /></td><td><code>string</code></td><td>Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags that have been assigned to this delivery.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
delivery_id,
arn,
delivery_source_name,
delivery_destination_arn,
delivery_destination_type,
tags
FROM aws.logs.delivery
WHERE region = 'us-east-1' AND data__Identifier = '<DeliveryId>';
```


## Permissions

To operate on the <code>delivery</code> resource, the following permissions are required:

### Read
```json
logs:GetDelivery,
logs:ListTagsForResource
```

### Update
```json
logs:GetDelivery,
logs:ListTagsForResource,
logs:TagResource,
logs:UntagResource
```

