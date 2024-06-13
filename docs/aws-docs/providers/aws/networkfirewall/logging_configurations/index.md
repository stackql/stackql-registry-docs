---
title: logging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configurations
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>logging_configuration</code> resource or lists <code>logging_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::LoggingConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.logging_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="firewall_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td>Resource type definition for AWS::NetworkFirewall::LoggingConfiguration</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="FirewallArn, LoggingConfiguration, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>logging_configurations</code> in a region.
```sql
SELECT
region,
firewall_arn
FROM aws.networkfirewall.logging_configurations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>logging_configuration</code>.
```sql
SELECT
region,
firewall_name,
firewall_arn,
logging_configuration
FROM aws.networkfirewall.logging_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<FirewallArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>logging_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.networkfirewall.logging_configurations (
 FirewallArn,
 LoggingConfiguration,
 region
)
SELECT 
'{{ FirewallArn }}',
 '{{ LoggingConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkfirewall.logging_configurations (
 FirewallName,
 FirewallArn,
 LoggingConfiguration,
 region
)
SELECT 
 '{{ FirewallName }}',
 '{{ FirewallArn }}',
 '{{ LoggingConfiguration }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: logging_configuration
    props:
      - name: FirewallName
        value: '{{ FirewallName }}'
      - name: FirewallArn
        value: '{{ FirewallArn }}'
      - name: LoggingConfiguration
        value:
          FirewallName: '{{ FirewallName }}'
          FirewallArn: null
          LoggingConfiguration: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkfirewall.logging_configurations
WHERE data__Identifier = '<FirewallArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>logging_configurations</code> resource, the following permissions are required:

### Create
```json
logs:CreateLogDelivery,
logs:GetLogDelivery,
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

### List
```json
logs:GetLogDelivery,
logs:ListLogDeliveries,
network-firewall:DescribeLoggingConfiguration
```

