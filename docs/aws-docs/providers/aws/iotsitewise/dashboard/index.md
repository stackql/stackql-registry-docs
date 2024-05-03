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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>dashboard</code> resource, use <code>dashboards</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Dashboard</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.dashboard" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The ID of the project in which to create the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_id" /></td><td><code>string</code></td><td>The ID of the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_name" /></td><td><code>string</code></td><td>A friendly name for the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_description" /></td><td><code>string</code></td><td>A description for the dashboard.</td></tr>
<tr><td><CopyableCode code="dashboard_definition" /></td><td><code>string</code></td><td>The dashboard definition specified in a JSON literal.</td></tr>
<tr><td><CopyableCode code="dashboard_arn" /></td><td><code>string</code></td><td>The ARN of the dashboard.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the dashboard.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
project_id,
dashboard_id,
dashboard_name,
dashboard_description,
dashboard_definition,
dashboard_arn,
tags
FROM aws.iotsitewise.dashboard
WHERE data__Identifier = '<DashboardId>';
```

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
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels
```

### Delete
```json
iotsitewise:DescribeDashboard,
iotsitewise:DeleteDashboard
```

