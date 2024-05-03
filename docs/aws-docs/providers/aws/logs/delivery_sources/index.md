---
title: delivery_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_sources
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

Used to retrieve a list of <code>delivery_sources</code> in a region or create a <code>delivery_sources</code> resource, use <code>delivery_source</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td> A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Only some AWS services support being configured as a delivery source. These services are listed as Supported &#91;V2 Permissions&#93; in the table at &#91;Enabling logging from AWS services&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonCloudWatch&#x2F;latest&#x2F;logs&#x2F;AWS-logs-and-resource-policy.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.delivery_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name of the Log source.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name
FROM aws.logs.delivery_sources
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>delivery_sources</code> resource, the following permissions are required:

### Create
```json
logs:PutDeliverySource,
logs:GetDeliverySource,
logs:ListTagsForResource,
logs:TagResource,
logs:AllowVendedLogDeliveryForResource,
codewhisperer:AllowVendedLogDeliveryForResource,
autoloop:AllowVendedLogDeliveryForResource,
workmail:AllowVendedLogDeliveryForResource
```

### List
```json
logs:DescribeDeliverySources
```

