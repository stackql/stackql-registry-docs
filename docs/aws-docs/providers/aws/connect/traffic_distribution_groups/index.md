---
title: traffic_distribution_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_distribution_groups
  - connect
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


Used to retrieve a list of <code>traffic_distribution_groups</code> in a region or to create or delete a <code>traffic_distribution_groups</code> resource, use <code>traffic_distribution_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traffic_distribution_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TrafficDistributionGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.traffic_distribution_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="traffic_distribution_group_arn" /></td><td><code>string</code></td><td>The identifier of the traffic distribution group.</td></tr>
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
traffic_distribution_group_arn
FROM aws.connect.traffic_distribution_groups
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
 "InstanceArn": "{{ InstanceArn }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.connect.traffic_distribution_groups (
 InstanceArn,
 Name,
 region
)
SELECT 
{{ .InstanceArn }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceArn": "{{ InstanceArn }}",
 "Description": "{{ Description }}",
 "Name": "{{ Name }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.connect.traffic_distribution_groups (
 InstanceArn,
 Description,
 Name,
 Tags,
 region
)
SELECT 
 {{ .InstanceArn }},
 {{ .Description }},
 {{ .Name }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.traffic_distribution_groups
WHERE data__Identifier = '<TrafficDistributionGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>traffic_distribution_groups</code> resource, the following permissions are required:

### Create
```json
connect:CreateTrafficDistributionGroup,
connect:DescribeTrafficDistributionGroup,
connect:TagResource
```

### Delete
```json
connect:DeleteTrafficDistributionGroup,
connect:DescribeTrafficDistributionGroup,
connect:UntagResource
```

### List
```json
connect:ListTrafficDistributionGroups
```

