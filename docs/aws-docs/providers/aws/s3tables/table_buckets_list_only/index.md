---
title: table_buckets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - table_buckets_list_only
  - s3tables
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

Lists <code>table_buckets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/table_buckets/"><code>table_buckets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_buckets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon S3 Tables table bucket in the same AWS Region where you create the AWS CloudFormation stack.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3tables.table_buckets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="table_bucket_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the table bucket to which the policy applies.</td></tr>
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
Lists all <code>table_buckets</code> in a region.
```sql
SELECT
region,
table_bucket_arn
FROM aws.s3tables.table_buckets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>table_buckets_list_only</code> resource, see <a href="/providers/aws/s3tables/table_buckets/#permissions"><code>table_buckets</code></a>

