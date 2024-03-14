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
Gets an individual <code>traffic_distribution_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traffic_distribution_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>traffic_distribution_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.traffic_distribution_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance that has been replicated.</td></tr>
<tr><td><code>traffic_distribution_group_arn</code></td><td><code>string</code></td><td>The identifier of the traffic distribution group.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the traffic distribution group.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name for the traffic distribution group.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the traffic distribution group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>is_default</code></td><td><code>boolean</code></td><td>If this is the default traffic distribution group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.connect.traffic_distribution_group
WHERE data__Identifier = '<TrafficDistributionGroupArn>';
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

### Delete
```json
connect:DeleteTrafficDistributionGroup,
connect:DescribeTrafficDistributionGroup,
connect:UntagResource
```

