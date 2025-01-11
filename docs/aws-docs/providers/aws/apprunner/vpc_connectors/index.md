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

Creates, updates, deletes or gets a <code>vpc_connector</code> resource or lists <code>vpc_connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.vpc_connectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vpc_connector_name" /></td><td><code>string</code></td><td>A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.</td></tr>
<tr><td><CopyableCode code="vpc_connector_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this VPC connector.</td></tr>
<tr><td><CopyableCode code="vpc_connector_revision" /></td><td><code>integer</code></td><td>The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name.</td></tr>
<tr><td><CopyableCode code="subnets" /></td><td><code>array</code></td><td>A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html"><code>AWS::AppRunner::VpcConnector</code></a>.

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
    <td><CopyableCode code="Subnets, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>vpc_connectors</code> in a region.
```sql
SELECT
region,
vpc_connector_name,
vpc_connector_arn,
vpc_connector_revision,
subnets,
security_groups,
tags
FROM aws.apprunner.vpc_connectors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpc_connector</code>.
```sql
SELECT
region,
vpc_connector_name,
vpc_connector_arn,
vpc_connector_revision,
subnets,
security_groups,
tags
FROM aws.apprunner.vpc_connectors
WHERE region = 'us-east-1' AND data__Identifier = '<VpcConnectorArn>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
apprunner:DescribeVpcConnector
```

### Delete
```json
apprunner:DeleteVpcConnector
```

### List
```json
apprunner:ListVpcConnectors
```
