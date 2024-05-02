---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - kinesisanalyticsv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see &#91;Creating an Application&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kinesisanalytics&#x2F;latest&#x2F;java&#x2F;getting-started.html).</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesisanalyticsv2.applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td>The name of the application.</td></tr>
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
application_name
FROM aws.kinesisanalyticsv2.applications
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
kinesisanalytics:CreateApplication,
kinesisanalytics:DescribeApplication,
kinesisanalytics:ListTagsForResource,
kinesisanalytics:UpdateApplicationMaintenanceConfiguration
```

### List
```json
kinesisanalytics:ListApplications
```

