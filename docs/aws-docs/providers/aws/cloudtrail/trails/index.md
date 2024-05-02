---
title: trails
hide_title: false
hide_table_of_contents: false
keywords:
  - trails
  - cloudtrail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>trails</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trails</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudtrail.trails</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>trail_name</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
trail_name
FROM aws.cloudtrail.trails
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>trails</code> resource, the following permissions are required:

### Create
```json
CloudTrail:CreateTrail,
CloudTrail:StartLogging,
CloudTrail:AddTags,
CloudTrail:PutEventSelectors,
CloudTrail:PutInsightSelectors,
iam:GetRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
organizations:DescribeOrganization,
organizations:ListAWSServiceAccessForOrganization
```

### List
```json
CloudTrail:ListTrails,
CloudTrail:GetTrail,
CloudTrail:GetTrailStatus,
CloudTrail:ListTags,
CloudTrail:GetEventSelectors,
CloudTrail:GetInsightSelectors,
CloudTrail:DescribeTrails
```

