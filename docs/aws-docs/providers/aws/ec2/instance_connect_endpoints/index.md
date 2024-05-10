---
title: instance_connect_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_connect_endpoints
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


Used to retrieve a list of <code>instance_connect_endpoints</code> in a region or to create or delete a <code>instance_connect_endpoints</code> resource, use <code>instance_connect_endpoint</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_connect_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::InstanceConnectEndpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.instance_connect_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id of the instance connect endpoint</td></tr>
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
FROM aws.ec2.instance_connect_endpoints
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
 "SubnetId": "{{ SubnetId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.instance_connect_endpoints (
 SubnetId,
 region
)
SELECT 
{{ SubnetId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "SubnetId": "{{ SubnetId }}",
 "ClientToken": "{{ ClientToken }}",
 "PreserveClientIp": "{{ PreserveClientIp }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.instance_connect_endpoints (
 SubnetId,
 ClientToken,
 PreserveClientIp,
 Tags,
 SecurityGroupIds,
 region
)
SELECT 
 {{ SubnetId }},
 {{ ClientToken }},
 {{ PreserveClientIp }},
 {{ Tags }},
 {{ SecurityGroupIds }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.instance_connect_endpoints
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>instance_connect_endpoints</code> resource, the following permissions are required:

### Create
```json
ec2:CreateInstanceConnectEndpoint,
ec2:DescribeInstanceConnectEndpoints,
ec2:CreateTags,
ec2:CreateNetworkInterface,
iam:CreateServiceLinkedRole
```

### Delete
```json
ec2:DeleteInstanceConnectEndpoint,
ec2:DescribeInstanceConnectEndpoints
```

### List
```json
ec2:DescribeInstanceConnectEndpoints
```

