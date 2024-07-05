---
title: vpc_ingress_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_ingress_connections
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

Creates, updates, deletes or gets a <code>vpc_ingress_connection</code> resource or lists <code>vpc_ingress_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_ingress_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::VpcIngressConnection resource is an App Runner resource that specifies an App Runner VpcIngressConnection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.vpc_ingress_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vpc_ingress_connection_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the VpcIngressConnection.</td></tr>
<tr><td><CopyableCode code="vpc_ingress_connection_name" /></td><td><code>string</code></td><td>The customer-provided Vpc Ingress Connection name.</td></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the service.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The current status of the VpcIngressConnection.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The Domain name associated with the VPC Ingress Connection.</td></tr>
<tr><td><CopyableCode code="ingress_vpc_configuration" /></td><td><code>object</code></td><td>The configuration of customer’s VPC and related VPC endpoint</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="ServiceArn, IngressVpcConfiguration, region" /></td>
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
Gets all <code>vpc_ingress_connections</code> in a region.
```sql
SELECT
region,
vpc_ingress_connection_arn,
vpc_ingress_connection_name,
service_arn,
status,
domain_name,
ingress_vpc_configuration,
tags
FROM aws.apprunner.vpc_ingress_connections
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vpc_ingress_connection</code>.
```sql
SELECT
region,
vpc_ingress_connection_arn,
vpc_ingress_connection_name,
service_arn,
status,
domain_name,
ingress_vpc_configuration,
tags
FROM aws.apprunner.vpc_ingress_connections
WHERE region = 'us-east-1' AND data__Identifier = '<VpcIngressConnectionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_ingress_connection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apprunner.vpc_ingress_connections (
 ServiceArn,
 IngressVpcConfiguration,
 region
)
SELECT 
'{{ ServiceArn }}',
 '{{ IngressVpcConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apprunner.vpc_ingress_connections (
 VpcIngressConnectionName,
 ServiceArn,
 IngressVpcConfiguration,
 Tags,
 region
)
SELECT 
 '{{ VpcIngressConnectionName }}',
 '{{ ServiceArn }}',
 '{{ IngressVpcConfiguration }}',
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
  - name: vpc_ingress_connection
    props:
      - name: VpcIngressConnectionName
        value: '{{ VpcIngressConnectionName }}'
      - name: ServiceArn
        value: '{{ ServiceArn }}'
      - name: IngressVpcConfiguration
        value:
          VpcId: '{{ VpcId }}'
          VpcEndpointId: '{{ VpcEndpointId }}'
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
DELETE FROM aws.apprunner.vpc_ingress_connections
WHERE data__Identifier = '<VpcIngressConnectionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_ingress_connections</code> resource, the following permissions are required:

### Create
```json
apprunner:CreateVpcIngressConnection,
apprunner:DescribeVpcIngressConnection,
ec2:DescribeVpcs,
ec2:DescribeVpcEndpoints,
ec2:DescribeSubnets,
apprunner:TagResource
```

### Read
```json
apprunner:DescribeVpcIngressConnection
```

### Update
```json
apprunner:UpdateVpcIngressConnection
```

### Delete
```json
apprunner:DeleteVpcIngressConnection
```

### List
```json
apprunner:ListVpcIngressConnections
```

