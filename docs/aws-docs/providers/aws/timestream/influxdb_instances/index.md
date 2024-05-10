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


Used to retrieve a list of <code>influxdb_instances</code> in a region or to create or delete a <code>influxdb_instances</code> resource, use <code>influxdb_instance</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>influxdb_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::InfluxDBInstance resource creates an InfluxDB instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.influxdb_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The service generated unique identifier for InfluxDB instance.</td></tr>
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
id
FROM aws.timestream.influxdb_instances
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Username": "{{ Username }}",
 "Password": "{{ Password }}",
 "Organization": "{{ Organization }}",
 "Bucket": "{{ Bucket }}",
 "DbInstanceType": "{{ DbInstanceType }}",
 "VpcSubnetIds": [
  "{{ VpcSubnetIds[0] }}"
 ],
 "VpcSecurityGroupIds": [
  "{{ VpcSecurityGroupIds[0] }}"
 ],
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "DbStorageType": "{{ DbStorageType }}",
 "AllocatedStorage": "{{ AllocatedStorage }}",
 "DbParameterGroupIdentifier": "{{ DbParameterGroupIdentifier }}",
 "LogDeliveryConfiguration": {
  "S3Configuration": {
   "BucketName": "{{ BucketName }}",
   "Enabled": "{{ Enabled }}"
  }
 },
 "Name": "{{ Name }}",
 "DeploymentType": "{{ DeploymentType }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
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
{{ .Username }},
 {{ .Password }},
 {{ .Organization }},
 {{ .Bucket }},
 {{ .DbInstanceType }},
 {{ .VpcSubnetIds }},
 {{ .VpcSecurityGroupIds }},
 {{ .PubliclyAccessible }},
 {{ .DbStorageType }},
 {{ .AllocatedStorage }},
 {{ .DbParameterGroupIdentifier }},
 {{ .LogDeliveryConfiguration }},
 {{ .Name }},
 {{ .DeploymentType }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Username": "{{ Username }}",
 "Password": "{{ Password }}",
 "Organization": "{{ Organization }}",
 "Bucket": "{{ Bucket }}",
 "DbInstanceType": "{{ DbInstanceType }}",
 "VpcSubnetIds": [
  "{{ VpcSubnetIds[0] }}"
 ],
 "VpcSecurityGroupIds": [
  "{{ VpcSecurityGroupIds[0] }}"
 ],
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "DbStorageType": "{{ DbStorageType }}",
 "AllocatedStorage": "{{ AllocatedStorage }}",
 "DbParameterGroupIdentifier": "{{ DbParameterGroupIdentifier }}",
 "LogDeliveryConfiguration": {
  "S3Configuration": {
   "BucketName": "{{ BucketName }}",
   "Enabled": "{{ Enabled }}"
  }
 },
 "Name": "{{ Name }}",
 "DeploymentType": "{{ DeploymentType }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ .Username }},
 {{ .Password }},
 {{ .Organization }},
 {{ .Bucket }},
 {{ .DbInstanceType }},
 {{ .VpcSubnetIds }},
 {{ .VpcSecurityGroupIds }},
 {{ .PubliclyAccessible }},
 {{ .DbStorageType }},
 {{ .AllocatedStorage }},
 {{ .DbParameterGroupIdentifier }},
 {{ .LogDeliveryConfiguration }},
 {{ .Name }},
 {{ .DeploymentType }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

