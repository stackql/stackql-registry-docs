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


Used to retrieve a list of <code>hosts</code> in a region or to create or delete a <code>hosts</code> resource, use <code>host</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::Host</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.hosts" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="host_id" /></td><td><code>string</code></td><td>ID of the host created.</td></tr>
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
host_id
FROM aws.ec2.hosts
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
 "AvailabilityZone": "{{ AvailabilityZone }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.hosts (
 AvailabilityZone,
 region
)
SELECT 
{{ .AvailabilityZone }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AutoPlacement": "{{ AutoPlacement }}",
 "AvailabilityZone": "{{ AvailabilityZone }}",
 "HostRecovery": "{{ HostRecovery }}",
 "InstanceType": "{{ InstanceType }}",
 "InstanceFamily": "{{ InstanceFamily }}",
 "OutpostArn": "{{ OutpostArn }}",
 "HostMaintenance": "{{ HostMaintenance }}",
 "AssetId": "{{ AssetId }}"
}
>>>
--all properties
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
 {{ .AutoPlacement }},
 {{ .AvailabilityZone }},
 {{ .HostRecovery }},
 {{ .InstanceType }},
 {{ .InstanceFamily }},
 {{ .OutpostArn }},
 {{ .HostMaintenance }},
 {{ .AssetId }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
ec2:ReleaseHosts,
ec2:DescribeHosts
```

### List
```json
ec2:DescribeHosts
```

