---
title: vpc_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connectors
  - apprunner
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


Used to retrieve a list of <code>vpc_connectors</code> in a region or to create or delete a <code>vpc_connectors</code> resource, use <code>vpc_connector</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.vpc_connectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="vpc_connector_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this VPC connector.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
vpc_connector_arn
FROM aws.apprunner.vpc_connectors
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>vpc_connector</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- vpc_connector.iql (required properties only)
INSERT INTO aws.apprunner.vpc_connectors (
 Subnets,
 region
)
SELECT 
'{{ Subnets }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- vpc_connector.iql (all properties)
INSERT INTO aws.apprunner.vpc_connectors (
 VpcConnectorName,
 Subnets,
 SecurityGroups,
 Tags,
 region
)
SELECT 
 '{{ VpcConnectorName }}',
 '{{ Subnets }}',
 '{{ SecurityGroups }}',
 '{{ Tags }}',
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
  - name: vpc_connector
    props:
      - name: VpcConnectorName
        value: '{{ VpcConnectorName }}'
      - name: Subnets
        value:
          - '{{ Subnets[0] }}'
      - name: SecurityGroups
        value:
          - '{{ SecurityGroups[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.apprunner.vpc_connectors
WHERE data__Identifier = '<VpcConnectorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_connectors</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
apprunner:CreateVpcConnector,
apprunner:DescribeVpcConnector,
apprunner:TagResource,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups
```

### Delete
```json
apprunner:DeleteVpcConnector
```

### List
```json
apprunner:ListVpcConnectors
```

