---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - m2
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

Creates, updates, deletes or gets an <code>environment</code> resource or lists <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a runtime environment that can run migrated mainframe applications.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.m2.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the environment.</td></tr>
<tr><td><CopyableCode code="engine_type" /></td><td><code>string</code></td><td>The target platform for the environment.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The version of the runtime engine for the environment.</td></tr>
<tr><td><CopyableCode code="environment_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the runtime environment.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The unique identifier of the environment.</td></tr>
<tr><td><CopyableCode code="high_availability_config" /></td><td><code>object</code></td><td>Defines the details of a high availability configuration.</td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td>The type of instance underlying the environment.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the environment.</td></tr>
<tr><td><CopyableCode code="network_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td>Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>Specifies whether the environment is publicly accessible.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The list of security groups for the VPC associated with this environment.</td></tr>
<tr><td><CopyableCode code="storage_configurations" /></td><td><code>array</code></td><td>The storage configurations defined for the runtime environment.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The unique identifiers of the subnets assigned to this runtime environment.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Tags associated to this environment.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-m2-environment.html"><code>AWS::M2::Environment</code></a>.

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
    <td><CopyableCode code="EngineType, InstanceType, Name, region" /></td>
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
Gets all <code>environments</code> in a region.
```sql
SELECT
region,
description,
engine_type,
engine_version,
environment_arn,
environment_id,
high_availability_config,
instance_type,
kms_key_id,
name,
network_type,
preferred_maintenance_window,
publicly_accessible,
security_group_ids,
storage_configurations,
subnet_ids,
tags
FROM aws.m2.environments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>environment</code>.
```sql
SELECT
region,
description,
engine_type,
engine_version,
environment_arn,
environment_id,
high_availability_config,
instance_type,
kms_key_id,
name,
network_type,
preferred_maintenance_window,
publicly_accessible,
security_group_ids,
storage_configurations,
subnet_ids,
tags
FROM aws.m2.environments
WHERE region = 'us-east-1' AND data__Identifier = '<EnvironmentArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.m2.environments (
 EngineType,
 InstanceType,
 Name,
 region
)
SELECT 
'{{ EngineType }}',
 '{{ InstanceType }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.m2.environments (
 Description,
 EngineType,
 EngineVersion,
 HighAvailabilityConfig,
 InstanceType,
 KmsKeyId,
 Name,
 NetworkType,
 PreferredMaintenanceWindow,
 PubliclyAccessible,
 SecurityGroupIds,
 StorageConfigurations,
 SubnetIds,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ EngineType }}',
 '{{ EngineVersion }}',
 '{{ HighAvailabilityConfig }}',
 '{{ InstanceType }}',
 '{{ KmsKeyId }}',
 '{{ Name }}',
 '{{ NetworkType }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ PubliclyAccessible }}',
 '{{ SecurityGroupIds }}',
 '{{ StorageConfigurations }}',
 '{{ SubnetIds }}',
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
  - name: environment
    props:
      - name: Description
        value: '{{ Description }}'
      - name: EngineType
        value: '{{ EngineType }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: HighAvailabilityConfig
        value:
          DesiredCapacity: '{{ DesiredCapacity }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: Name
        value: '{{ Name }}'
      - name: NetworkType
        value: '{{ NetworkType }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: StorageConfigurations
        value:
          - {}
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.m2.environments
WHERE data__Identifier = '<EnvironmentArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInterface,
ec2:CreateNetworkInterfacePermission,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
ec2:ModifyNetworkInterfaceAttribute,
elasticfilesystem:DescribeMountTargets,
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:DeleteLoadBalancer,
elasticloadbalancing:AddTags,
fsx:DescribeFileSystems,
iam:CreateServiceLinkedRole,
kms:DescribeKey,
kms:CreateGrant,
m2:CreateEnvironment,
m2:GetEnvironment,
m2:ListTagsForResource,
m2:TagResource
```

### Read
```json
m2:ListTagsForResource,
m2:GetEnvironment
```

### Update
```json
m2:TagResource,
m2:UntagResource,
m2:ListTagsForResource,
m2:GetEnvironment,
m2:UpdateEnvironment,
kms:DescribeKey
```

### Delete
```json
elasticloadbalancing:DeleteLoadBalancer,
m2:DeleteEnvironment,
m2:GetEnvironment
```

### List
```json
m2:ListEnvironments
```
