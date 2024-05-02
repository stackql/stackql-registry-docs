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
Gets an individual <code>network_insights_path</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_path</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EC2::NetworkInsightsPath</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_insights_path</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>network_insights_path_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_insights_path_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_ip</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>filter_at_source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>filter_at_destination</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>destination_ip</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>destination</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>destination_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>protocol</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>destination_port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
WHERE data__Identifier = '<NetworkInsightsPathId>';
```

## Permissions

To operate on the <code>network_insights_path</code> resource, the following permissions are required:

### Delete
```json
ec2:DeleteNetworkInsightsPath,
ec2:DeleteTags
```

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

