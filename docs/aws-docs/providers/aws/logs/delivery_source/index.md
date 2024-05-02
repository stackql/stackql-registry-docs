---
title: delivery_source
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_source
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
Gets an individual <code>delivery_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td> A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Only some AWS services support being configured as a delivery source. These services are listed as Supported &#91;V2 Permissions&#93; in the table at &#91;Enabling logging from AWS services&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonCloudWatch&#x2F;latest&#x2F;logs&#x2F;AWS-logs-and-resource-policy.html).</td></tr>
<tr><td><b>Id</b></td><td><code>aws.logs.delivery_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The unique name of the Log source.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that uniquely identifies this delivery source.</td></tr>
<tr><td><code>resource_arns</code></td><td><code>array</code></td><td>This array contains the ARN of the AWS resource that sends logs and is represented by this delivery source. Currently, only one ARN can be in the array.</td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td>The ARN of the resource that will be sending the logs.</td></tr>
<tr><td><code>service</code></td><td><code>string</code></td><td>The AWS service that is sending logs.</td></tr>
<tr><td><code>log_type</code></td><td><code>string</code></td><td>The type of logs being delivered. Only mandatory when the resourceArn could match more than one. In such a case, the error message will contain all the possible options.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags that have been assigned to this delivery source.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
arn,
resource_arns,
resource_arn,
service,
log_type,
tags
FROM aws.logs.delivery_source
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>delivery_source</code> resource, the following permissions are required:

### Read
```json
logs:GetDeliverySource,
logs:ListTagsForResource
```

### Update
```json
logs:PutDeliverySource,
logs:GetDeliverySource,
logs:ListTagsForResource,
logs:TagResource,
logs:UntagResource
```

### Delete
```json
logs:DeleteDeliverySource
```

