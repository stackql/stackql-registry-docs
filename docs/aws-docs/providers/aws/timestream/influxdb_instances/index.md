---
title: influxdb_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - influxdb_instances
  - timestream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>influxdb_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>influxdb_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::InfluxDBInstance resource creates an InfluxDB instance.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.timestream.influxdb_instances</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The service generated unique identifier for InfluxDB instance.</td></tr>
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
id
FROM aws.timestream.influxdb_instances
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>influxdb_instances</code> resource, the following permissions are required:

### Create
```json
s3:ListBucket,
s3:GetBucketPolicy,
timestream-influxdb:GetDbInstance,
timestream-influxdb:ListDbInstances,
timestream-influxdb:CreateDbInstance,
timestream-influxdb:TagResource,
timestream-influxdb:ListTagsForResource,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSecurityGroups,
ec2:CreateNetworkInterface,
iam:CreateServiceLinkedRole
```

### List
```json
timestream-influxdb:ListDbInstances
```

