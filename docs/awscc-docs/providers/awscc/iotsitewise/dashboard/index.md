---
title: dashboard
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard
  - iotsitewise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dashboard</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dashboard</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotsitewise.dashboard</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>project_id</code></td><td><code>string</code></td><td>The ID of the project in which to create the dashboard.</td></tr>
<tr><td><code>dashboard_id</code></td><td><code>string</code></td><td>The ID of the dashboard.</td></tr>
<tr><td><code>dashboard_name</code></td><td><code>string</code></td><td>A friendly name for the dashboard.</td></tr>
<tr><td><code>dashboard_description</code></td><td><code>string</code></td><td>A description for the dashboard.</td></tr>
<tr><td><code>dashboard_definition</code></td><td><code>string</code></td><td>The dashboard definition specified in a JSON literal.</td></tr>
<tr><td><code>dashboard_arn</code></td><td><code>string</code></td><td>The ARN of the dashboard.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the dashboard.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>dashboard</code> resource, the following permissions are required:

### Read
```json
iotsitewise:DescribeDashboard,
iotsitewise:ListTagsForResource
```

### Update
```json
iotsitewise:DescribeDashboard,
iotsitewise:UpdateDashboard,
iotsitewise:TagResource,
iotsitewise:UntagResource,
iotsitewise:ListTagsForResource,
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel
```

### Delete
```json
iotsitewise:DescribeDashboard,
iotsitewise:DeleteDashboard
```


## Example
```sql
SELECT
region,
project_id,
dashboard_id,
dashboard_name,
dashboard_description,
dashboard_definition,
dashboard_arn,
tags
FROM awscc.iotsitewise.dashboard
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DashboardId&gt;'
```
