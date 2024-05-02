---
title: logging_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configuration
  - networkfirewall
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>logging_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::LoggingConfiguration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkfirewall.logging_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>firewall_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>logging_configuration</code></td><td><code>object</code></td><td></td></tr>
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
firewall_name,
firewall_arn,
logging_configuration
FROM aws.networkfirewall.logging_configuration
WHERE data__Identifier = '<FirewallArn>';
```

## Permissions

To operate on the <code>logging_configuration</code> resource, the following permissions are required:

### Read
```json
logs:GetLogDelivery,
logs:ListLogDeliveries,
network-firewall:DescribeLoggingConfiguration
```

### Update
```json
logs:CreateLogDelivery,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:ListLogDeliveries,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
iam:CreateServiceLinkedRole,
firehose:TagDeliveryStream,
network-firewall:UpdateLoggingConfiguration,
network-firewall:DescribeLoggingConfiguration
```

### Delete
```json
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:GetLogDelivery,
network-firewall:UpdateLoggingConfiguration,
network-firewall:DescribeLoggingConfiguration
```

