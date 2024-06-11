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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>influxdb_instance</code> resource or lists <code>influxdb_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>influxdb_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::InfluxDBInstance resource creates an InfluxDB instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.influxdb_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td>The username for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="password" /></td><td><code>string</code></td><td>The password for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="organization" /></td><td><code>string</code></td><td>The organization for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="bucket" /></td><td><code>string</code></td><td>The bucket for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="db_instance_type" /></td><td><code>string</code></td><td>The compute instance of the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="vpc_subnet_ids" /></td><td><code>array</code></td><td>A list of EC2 subnet IDs for this InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>A list of Amazon EC2 VPC security groups to associate with this InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>Attach a public IP to the customer ENI.</td></tr>
<tr><td><CopyableCode code="db_storage_type" /></td><td><code>string</code></td><td>The storage type of the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="allocated_storage" /></td><td><code>integer</code></td><td>The allocated storage for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="db_parameter_group_identifier" /></td><td><code>string</code></td><td>The name of an existing InfluxDB parameter group.</td></tr>
<tr><td><CopyableCode code="log_delivery_configuration" /></td><td><code>object</code></td><td>Configuration for sending logs to customer account from the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Status of the InfluxDB Instance.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is associated with the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name that is associated with the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone (AZ) where the InfluxDB instance is created.</td></tr>
<tr><td><CopyableCode code="secondary_availability_zone" /></td><td><code>string</code></td><td>The Secondary Availability Zone (AZ) where the InfluxDB instance is created, if DeploymentType is set as WITH_MULTIAZ_STANDBY.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The connection endpoint for the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="influx_auth_parameters_secret_arn" /></td><td><code>string</code></td><td>The Auth parameters secret Amazon Resource name (ARN) that is associated with the InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The service generated unique identifier for InfluxDB instance.</td></tr>
<tr><td><CopyableCode code="deployment_type" /></td><td><code>string</code></td><td>Deployment type of the InfluxDB Instance.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this DB instance.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>influxdb_instances</code> in a region.
```sql
SELECT
region,
id
FROM aws.timestream.influxdb_instances
WHERE region = 'us-east-1';
```
Gets all properties from an <code>influxdb_instance</code>.
```sql
SELECT
region,
username,
password,
organization,
bucket,
db_instance_type,
vpc_subnet_ids,
vpc_security_group_ids,
publicly_accessible,
db_storage_type,
allocated_storage,
db_parameter_group_identifier,
log_delivery_configuration,
status,
arn,
name,
availability_zone,
secondary_availability_zone,
endpoint,
influx_auth_parameters_secret_arn,
id,
deployment_type,
tags
FROM aws.timestream.influxdb_instances
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>influxdb_instance</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.timestream.influxdb_instances (
 Username,
 Password,
 Organization,
 Bucket,
 DbInstanceType,
 VpcSubnetIds,
 VpcSecurityGroupIds,
 PubliclyAccessible,
 DbStorageType,
 AllocatedStorage,
 DbParameterGroupIdentifier,
 LogDeliveryConfiguration,
 Name,
 DeploymentType,
 Tags,
 region
)
SELECT 
'{{ Username }}',
 '{{ Password }}',
 '{{ Organization }}',
 '{{ Bucket }}',
 '{{ DbInstanceType }}',
 '{{ VpcSubnetIds }}',
 '{{ VpcSecurityGroupIds }}',
 '{{ PubliclyAccessible }}',
 '{{ DbStorageType }}',
 '{{ AllocatedStorage }}',
 '{{ DbParameterGroupIdentifier }}',
 '{{ LogDeliveryConfiguration }}',
 '{{ Name }}',
 '{{ DeploymentType }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.timestream.influxdb_instances (
 Username,
 Password,
 Organization,
 Bucket,
 DbInstanceType,
 VpcSubnetIds,
 VpcSecurityGroupIds,
 PubliclyAccessible,
 DbStorageType,
 AllocatedStorage,
 DbParameterGroupIdentifier,
 LogDeliveryConfiguration,
 Name,
 DeploymentType,
 Tags,
 region
)
SELECT 
 '{{ Username }}',
 '{{ Password }}',
 '{{ Organization }}',
 '{{ Bucket }}',
 '{{ DbInstanceType }}',
 '{{ VpcSubnetIds }}',
 '{{ VpcSecurityGroupIds }}',
 '{{ PubliclyAccessible }}',
 '{{ DbStorageType }}',
 '{{ AllocatedStorage }}',
 '{{ DbParameterGroupIdentifier }}',
 '{{ LogDeliveryConfiguration }}',
 '{{ Name }}',
 '{{ DeploymentType }}',
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
  - name: influxdb_instance
    props:
      - name: Username
        value: '{{ Username }}'
      - name: Password
        value: '{{ Password }}'
      - name: Organization
        value: '{{ Organization }}'
      - name: Bucket
        value: '{{ Bucket }}'
      - name: DbInstanceType
        value: '{{ DbInstanceType }}'
      - name: VpcSubnetIds
        value:
          - '{{ VpcSubnetIds[0] }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: DbStorageType
        value: '{{ DbStorageType }}'
      - name: AllocatedStorage
        value: '{{ AllocatedStorage }}'
      - name: DbParameterGroupIdentifier
        value: '{{ DbParameterGroupIdentifier }}'
      - name: LogDeliveryConfiguration
        value:
          S3Configuration:
            BucketName: '{{ BucketName }}'
            Enabled: '{{ Enabled }}'
      - name: Name
        value: '{{ Name }}'
      - name: DeploymentType
        value: '{{ DeploymentType }}'
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
DELETE FROM aws.timestream.influxdb_instances
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
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

### Read
```json
timestream-influxdb:GetDbInstance,
timestream-influxdb:ListTagsForResource
```

### Update
```json
s3:ListBucket,
s3:GetBucketPolicy,
timestream-influxdb:GetDbInstance,
timestream-influxdb:ListDbInstances,
timestream-influxdb:UpdateDbInstance,
timestream-influxdb:TagResource,
timestream-influxdb:UntagResource,
timestream-influxdb:ListTagsForResource
```

### Delete
```json
timestream-influxdb:GetDbInstance,
timestream-influxdb:ListDbInstances,
timestream-influxdb:DeleteDbInstance
```

### List
```json
timestream-influxdb:ListDbInstances
```

