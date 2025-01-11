---
title: buckets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets_list_only
  - s3
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

Lists <code>buckets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/buckets/"><code>buckets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::S3::Bucket</code> resource creates an Amazon S3 bucket in the same AWS Region where you create the AWS CloudFormation stack.<br />To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see &#91;DeletionPolicy Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).<br />You can only delete empty buckets. Deletion fails for buckets that have contents.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.buckets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow &#91;Amazon S3 bucket restrictions and limitations&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html). For more information, see &#91;Rules for naming Amazon S3 buckets&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html#bucketnamingrules) in the *Amazon S3 User Guide*. <br />If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>buckets</code> in a region.
```sql
SELECT
region,
bucket_name
FROM aws.s3.buckets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>buckets_list_only</code> resource, see <a href="/providers/aws/s3/buckets/#permissions"><code>buckets</code></a>

