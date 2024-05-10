---
title: locationf_sx_ontaps
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_ontaps
  - datasync
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


Used to retrieve a list of <code>locationf_sx_ontaps</code> in a region or to create or delete a <code>locationf_sx_ontaps</code> resource, use <code>locationf_sx_ontap</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_ontaps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationFSxONTAP.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.locationf_sx_ontaps" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.</td></tr>
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
location_arn
FROM aws.datasync.locationf_sx_ontaps
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
 "StorageVirtualMachineArn": "{{ StorageVirtualMachineArn }}",
 "SecurityGroupArns": [
  "{{ SecurityGroupArns[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.datasync.locationf_sx_ontaps (
 StorageVirtualMachineArn,
 SecurityGroupArns,
 region
)
SELECT 
{{ .StorageVirtualMachineArn }},
 {{ .SecurityGroupArns }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "StorageVirtualMachineArn": "{{ StorageVirtualMachineArn }}",
 "SecurityGroupArns": [
  "{{ SecurityGroupArns[0] }}"
 ],
 "Protocol": {
  "NFS": {
   "MountOptions": {
    "Version": "{{ Version }}"
   }
  }
 },
 "Subdirectory": "{{ Subdirectory }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.datasync.locationf_sx_ontaps (
 StorageVirtualMachineArn,
 SecurityGroupArns,
 Protocol,
 Subdirectory,
 Tags,
 region
)
SELECT 
 {{ .StorageVirtualMachineArn }},
 {{ .SecurityGroupArns }},
 {{ .Protocol }},
 {{ .Subdirectory }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.datasync.locationf_sx_ontaps
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>locationf_sx_ontaps</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationFsxOntap,
datasync:DescribeLocationFsxOntap,
datasync:ListTagsForResource,
datasync:TagResource,
fsx:DescribeStorageVirtualMachines,
fsx:DescribeFileSystems,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups
```

### Delete
```json
datasync:DeleteLocation
```

### List
```json
datasync:ListLocations
```

