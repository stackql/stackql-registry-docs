---
title: vpc_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connections
  - quicksight
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


Used to retrieve a list of <code>vpc_connections</code> in a region or to create or delete a <code>vpc_connections</code> resource, use <code>vpc_connection</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::VPCConnection Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.vpc_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_connection_id" /></td><td><code>undefined</code></td><td></td></tr>
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
aws_account_id,
vpc_connection_id
FROM aws.quicksight.vpc_connections
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
 "AwsAccountId": "{{ AwsAccountId }}",
 "Name": "{{ Name }}",
 "VPCConnectionId": "{{ VPCConnectionId }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ],
 "DnsResolvers": [
  "{{ DnsResolvers[0] }}"
 ],
 "AvailabilityStatus": "{{ AvailabilityStatus }}",
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.quicksight.vpc_connections (
 AwsAccountId,
 Name,
 VPCConnectionId,
 SecurityGroupIds,
 SubnetIds,
 DnsResolvers,
 AvailabilityStatus,
 RoleArn,
 Tags,
 region
)
SELECT 
{{ .AwsAccountId }},
 {{ .Name }},
 {{ .VPCConnectionId }},
 {{ .SecurityGroupIds }},
 {{ .SubnetIds }},
 {{ .DnsResolvers }},
 {{ .AvailabilityStatus }},
 {{ .RoleArn }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AwsAccountId": "{{ AwsAccountId }}",
 "Name": "{{ Name }}",
 "VPCConnectionId": "{{ VPCConnectionId }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ],
 "DnsResolvers": [
  "{{ DnsResolvers[0] }}"
 ],
 "AvailabilityStatus": "{{ AvailabilityStatus }}",
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.quicksight.vpc_connections (
 AwsAccountId,
 Name,
 VPCConnectionId,
 SecurityGroupIds,
 SubnetIds,
 DnsResolvers,
 AvailabilityStatus,
 RoleArn,
 Tags,
 region
)
SELECT 
 {{ .AwsAccountId }},
 {{ .Name }},
 {{ .VPCConnectionId }},
 {{ .SecurityGroupIds }},
 {{ .SubnetIds }},
 {{ .DnsResolvers }},
 {{ .AvailabilityStatus }},
 {{ .RoleArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.quicksight.vpc_connections
WHERE data__Identifier = '<AwsAccountId|VPCConnectionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_connections</code> resource, the following permissions are required:

### Create
```json
quicksight:CreateVPCConnection,
quicksight:DescribeVPCConnection,
quicksight:ListTagsForResource,
quicksight:TagResource,
iam:PassRole
```

### Delete
```json
quicksight:DescribeVPCConnection,
quicksight:DeleteVPCConnection,
quicksight:ListTagsForResource,
iam:PassRole
```

### List
```json
quicksight:ListVPCConnections
```

