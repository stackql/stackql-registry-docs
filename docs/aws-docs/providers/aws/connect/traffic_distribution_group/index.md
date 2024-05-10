---
title: traffic_distribution_group
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_distribution_group
  - connect
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


Gets or updates an individual <code>traffic_distribution_group</code> resource, use <code>traffic_distribution_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traffic_distribution_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TrafficDistributionGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.traffic_distribution_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance that has been replicated.</td></tr>
<tr><td><CopyableCode code="traffic_distribution_group_arn" /></td><td><code>string</code></td><td>The identifier of the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>If this is the default traffic distribution group.</td></tr>
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
instance_arn,
traffic_distribution_group_arn,
description,
name,
status,
tags,
is_default
FROM aws.connect.traffic_distribution_group
WHERE region = 'us-east-1' AND data__Identifier = '<TrafficDistributionGroupArn>';
```


## Permissions

To operate on the <code>traffic_distribution_group</code> resource, the following permissions are required:

### Read
```json
connect:DescribeTrafficDistributionGroup
```

### Update
```json
connect:TagResource,
connect:UntagResource
```

