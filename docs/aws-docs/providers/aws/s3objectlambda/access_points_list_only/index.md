---
title: access_points_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - access_points_list_only
  - s3objectlambda
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

Lists <code>access_points</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/access_points/"><code>access_points</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_points_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3ObjectLambda::AccessPoint resource is an Amazon S3ObjectLambda resource type that you can use to add computation to S3 actions</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3objectlambda.access_points_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Object lambda Access Point.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The date and time when the Object lambda Access Point was created.</td></tr>
<tr><td><CopyableCode code="public_access_block_configuration" /></td><td><code>object</code></td><td>The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.</td></tr>
<tr><td><CopyableCode code="policy_status" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="object_lambda_configuration" /></td><td><code>object</code></td><td>The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions</td></tr>
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
Lists all <code>access_points</code> in a region.
```sql
SELECT
region,
name
FROM aws.s3objectlambda.access_points_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>access_points_list_only</code> resource, see <a href="/providers/aws/s3objectlambda/access_points/#permissions"><code>access_points</code></a>


