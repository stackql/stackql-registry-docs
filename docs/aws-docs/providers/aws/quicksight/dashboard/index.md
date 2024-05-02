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
Gets or operates on an individual <code>dashboard</code> resource, use <code>dashboards</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Dashboard Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.quicksight.dashboard</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dashboard_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dashboard_publish_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>last_published_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>link_entities</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>link_sharing_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>source_entity</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>theme_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>validation_strategy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>version_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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

