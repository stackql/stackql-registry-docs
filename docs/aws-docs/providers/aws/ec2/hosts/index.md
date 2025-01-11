---
title: hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - hosts
  - ec2
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

Creates, updates, deletes or gets a <code>host</code> resource or lists <code>hosts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::Host</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.hosts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="host_id" /></td><td><code>string</code></td><td>ID of the host created.</td></tr>
<tr><td><CopyableCode code="auto_placement" /></td><td><code>string</code></td><td>Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it only accepts Host tenancy instance launches that specify its unique host ID.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone in which to allocate the Dedicated Host.</td></tr>
<tr><td><CopyableCode code="host_recovery" /></td><td><code>string</code></td><td>Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default.</td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td>Specifies the instance type to be supported by the Dedicated Hosts. If you specify an instance type, the Dedicated Hosts support instances of the specified instance type only.</td></tr>
<tr><td><CopyableCode code="instance_family" /></td><td><code>string</code></td><td>Specifies the instance family to be supported by the Dedicated Hosts. If you specify an instance family, the Dedicated Hosts support multiple instance types within that instance family.</td></tr>
<tr><td><CopyableCode code="outpost_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which to allocate the Dedicated Host.</td></tr>
<tr><td><CopyableCode code="host_maintenance" /></td><td><code>string</code></td><td>Automatically allocates a new dedicated host and moves your instances on to it if a degradation is detected on your current host.</td></tr>
<tr><td><CopyableCode code="asset_id" /></td><td><code>string</code></td><td>The ID of the Outpost hardware asset.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html"><code>AWS::EC2::Host</code></a>.

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
    <td><CopyableCode code="AvailabilityZone, region" /></td>
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
Gets all <code>hosts</code> in a region.
```sql
SELECT
region,
host_id,
auto_placement,
availability_zone,
host_recovery,
instance_type,
instance_family,
outpost_arn,
host_maintenance,
asset_id
FROM aws.ec2.hosts
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>host</code>.
```sql
SELECT
region,
host_id,
auto_placement,
availability_zone,
host_recovery,
instance_type,
instance_family,
outpost_arn,
host_maintenance,
asset_id
FROM aws.ec2.hosts
WHERE region = 'us-east-1' AND data__Identifier = '<HostId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>host</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.hosts (
 AvailabilityZone,
 region
)
SELECT 
'{{ AvailabilityZone }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.hosts (
 AutoPlacement,
 AvailabilityZone,
 HostRecovery,
 InstanceType,
 InstanceFamily,
 OutpostArn,
 HostMaintenance,
 AssetId,
 region
)
SELECT 
 '{{ AutoPlacement }}',
 '{{ AvailabilityZone }}',
 '{{ HostRecovery }}',
 '{{ InstanceType }}',
 '{{ InstanceFamily }}',
 '{{ OutpostArn }}',
 '{{ HostMaintenance }}',
 '{{ AssetId }}',
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
  - name: host
    props:
      - name: AutoPlacement
        value: '{{ AutoPlacement }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: HostRecovery
        value: '{{ HostRecovery }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: InstanceFamily
        value: '{{ InstanceFamily }}'
      - name: OutpostArn
        value: '{{ OutpostArn }}'
      - name: HostMaintenance
        value: '{{ HostMaintenance }}'
      - name: AssetId
        value: '{{ AssetId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.hosts
WHERE data__Identifier = '<HostId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>hosts</code> resource, the following permissions are required:

### Create
```json
ec2:AllocateHosts,
ec2:DescribeHosts
```

### Read
```json
ec2:DescribeHosts
```

### Update
```json
ec2:ModifyHosts,
ec2:DescribeHosts
```

### Delete
```json
ec2:ReleaseHosts,
ec2:DescribeHosts
```

### List
```json
ec2:DescribeHosts
```
