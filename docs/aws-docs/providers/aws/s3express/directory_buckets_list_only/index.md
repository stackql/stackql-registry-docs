---
title: directory_buckets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_buckets_list_only
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

Lists <code>directory_buckets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/directory_buckets/"><code>directory_buckets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_buckets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::S3Express::DirectoryBucket.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3express.directory_buckets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>Specifies a name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format 'bucket_base_name--az_id--x-s3' (for example, 'DOC-EXAMPLE-BUCKET--usw2-az1--x-s3'). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>directory_buckets</code> in a region.
```sql
SELECT
region,
bucket_name
FROM aws.s3express.directory_buckets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>directory_buckets_list_only</code> resource, see <a href="/providers/aws/s3express/directory_buckets/#permissions"><code>directory_buckets</code></a>


