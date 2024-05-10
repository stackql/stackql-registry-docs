---
title: directory_bucket
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_bucket
  - s3express
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


Gets or updates an individual <code>directory_bucket</code> resource, use <code>directory_buckets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_bucket</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::S3Express::DirectoryBucket.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3express.directory_bucket" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>Specifies a name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format 'bucket_base_name--az_id--x-s3' (for example, 'DOC-EXAMPLE-BUCKET--usw2-az1--x-s3'). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.</td></tr>
<tr><td><CopyableCode code="location_name" /></td><td><code>string</code></td><td>Specifies the AZ ID of the Availability Zone where the directory bucket will be created. An example AZ ID value is 'use1-az5'.</td></tr>
<tr><td><CopyableCode code="data_redundancy" /></td><td><code>string</code></td><td>Specifies the number of Availability Zone that's used for redundancy for the bucket.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Returns the Amazon Resource Name (ARN) of the specified bucket.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
bucket_name,
location_name,
data_redundancy,
arn
FROM aws.s3express.directory_bucket
WHERE region = 'us-east-1' AND data__Identifier = '<BucketName>';
```


## Permissions

To operate on the <code>directory_bucket</code> resource, the following permissions are required:

### Read
```json
s3express:ListAllMyDirectoryBuckets
```

