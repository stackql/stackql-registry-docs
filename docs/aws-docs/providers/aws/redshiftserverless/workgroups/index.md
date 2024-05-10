---
title: workgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - workgroups
  - redshiftserverless
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


Used to retrieve a list of <code>workgroups</code> in a region or to create or delete a <code>workgroups</code> resource, use <code>workgroup</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RedshiftServerless::Workgroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshiftserverless.workgroups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workgroup_name" /></td><td><code>string</code></td><td>The name of the workgroup.</td></tr>
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
workgroup_name
FROM aws.redshiftserverless.workgroups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>workgroup</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- workgroup.iql (required properties only)
INSERT INTO aws.redshiftserverless.workgroups (
 WorkgroupName,
 region
)
SELECT 
'{{ WorkgroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- workgroup.iql (all properties)
INSERT INTO aws.redshiftserverless.workgroups (
 WorkgroupName,
 NamespaceName,
 BaseCapacity,
 MaxCapacity,
 EnhancedVpcRouting,
 ConfigParameters,
 SecurityGroupIds,
 SubnetIds,
 PubliclyAccessible,
 Port,
 Tags,
 region
)
SELECT 
 '{{ WorkgroupName }}',
 '{{ NamespaceName }}',
 '{{ BaseCapacity }}',
 '{{ MaxCapacity }}',
 '{{ EnhancedVpcRouting }}',
 '{{ ConfigParameters }}',
 '{{ SecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ PubliclyAccessible }}',
 '{{ Port }}',
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
  - name: workgroup
    props:
      - name: WorkgroupName
        value: '{{ WorkgroupName }}'
      - name: NamespaceName
        value: '{{ NamespaceName }}'
      - name: BaseCapacity
        value: '{{ BaseCapacity }}'
      - name: MaxCapacity
        value: '{{ MaxCapacity }}'
      - name: EnhancedVpcRouting
        value: '{{ EnhancedVpcRouting }}'
      - name: ConfigParameters
        value:
          - ParameterKey: '{{ ParameterKey }}'
            ParameterValue: '{{ ParameterValue }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: Port
        value: '{{ Port }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.redshiftserverless.workgroups
WHERE data__Identifier = '<WorkgroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>workgroups</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:CreateNamespace,
redshift-serverless:CreateWorkgroup,
redshift-serverless:GetWorkgroup
```

### Delete
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:GetWorkgroup,
redshift-serverless:DeleteWorkgroup
```

### List
```json
ec2:DescribeVpcAttribute,
ec2:DescribeSecurityGroups,
ec2:DescribeAddresses,
ec2:DescribeInternetGateways,
ec2:DescribeSubnets,
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
redshift-serverless:ListWorkgroups
```

