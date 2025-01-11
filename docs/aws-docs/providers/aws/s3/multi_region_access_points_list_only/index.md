---
title: multi_region_access_points_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - multi_region_access_points_list_only
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

Lists <code>multi_region_access_points</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/multi_region_access_points/"><code>multi_region_access_points</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multi_region_access_points_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::S3::MultiRegionAccessPoint is an Amazon S3 resource type that dynamically routes S3 requests to easily satisfy geographic compliance requirements based on customer-defined routing policies.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.multi_region_access_points_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Multi Region Access Point.</td></tr>
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
Lists all <code>multi_region_access_points</code> in a region.
```sql
SELECT
region,
name
FROM aws.s3.multi_region_access_points_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>multi_region_access_points_list_only</code> resource, see <a href="/providers/aws/s3/multi_region_access_points/#permissions"><code>multi_region_access_points</code></a>

