---
title: dashboard
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard
  - quicksight
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
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Dashboard Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.dashboard" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dashboard_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dashboard_publish_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_published_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="link_entities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="link_sharing_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="source_entity" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="theme_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="validation_strategy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td></td></tr>
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
arn,
aws_account_id,
created_time,
dashboard_id,
dashboard_publish_options,
definition,
last_published_time,
last_updated_time,
link_entities,
link_sharing_configuration,
name,
parameters,
permissions,
source_entity,
tags,
theme_arn,
validation_strategy,
version,
version_description
FROM aws.quicksight.dashboard
WHERE data__Identifier = '<AwsAccountId>|<DashboardId>';
```

## Permissions

To operate on the <code>dashboard</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeDashboard,
quicksight:DescribeDashboardPermissions,
quicksight:ListTagsForResource
```

### Update
```json
quicksight:DescribeDashboard,
quicksight:DescribeDashboardPermissions,
quicksight:UpdateDashboard,
quicksight:UpdateDashboardLinks,
quicksight:UpdateDashboardPermissions,
quicksight:UpdateDashboardPublishedVersion,
quicksight:DescribeTemplate,
quicksight:DescribeTheme,
quicksight:PassDataSet,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### Delete
```json
quicksight:DescribeDashboard,
quicksight:DeleteDashboard
```

