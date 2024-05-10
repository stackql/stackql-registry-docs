---
title: network_insights_path
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_path
  - ec2
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


Gets or updates an individual <code>network_insights_path</code> resource, use <code>network_insights_paths</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_path</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsPath</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_insights_path" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="network_insights_path_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_insights_path_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_ip" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="filter_at_source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="filter_at_destination" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_ip" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="destination" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_port" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
network_insights_path_id,
network_insights_path_arn,
created_date,
source_ip,
filter_at_source,
filter_at_destination,
destination_ip,
source,
destination,
source_arn,
destination_arn,
protocol,
destination_port,
tags
FROM aws.ec2.network_insights_path
WHERE region = 'us-east-1' AND data__Identifier = '<NetworkInsightsPathId>';
```


## Permissions

To operate on the <code>network_insights_path</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeNetworkInsightsPaths
```

### Update
```json
ec2:DescribeNetworkInsightsPaths,
ec2:CreateTags,
ec2:DeleteTags
```

