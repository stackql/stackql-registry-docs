---
title: memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - memberships
  - cleanrooms
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


Used to retrieve a list of <code>memberships</code> in a region or to create or delete a <code>memberships</code> resource, use <code>membership</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an AWS account that is a part of a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.memberships" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
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
membership_identifier
FROM aws.cleanrooms.memberships
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
 "CollaborationIdentifier": "{{ CollaborationIdentifier }}",
 "QueryLogStatus": "{{ QueryLogStatus }}"
}
>>>
--required properties only
INSERT INTO aws.cleanrooms.memberships (
 CollaborationIdentifier,
 QueryLogStatus,
 region
)
SELECT 
{{ CollaborationIdentifier }},
 {{ QueryLogStatus }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "CollaborationIdentifier": "{{ CollaborationIdentifier }}",
 "QueryLogStatus": "{{ QueryLogStatus }}",
 "DefaultResultConfiguration": {
  "OutputConfiguration": {
   "S3": {
    "ResultFormat": "{{ ResultFormat }}",
    "Bucket": "{{ Bucket }}",
    "KeyPrefix": "{{ KeyPrefix }}"
   }
  },
  "RoleArn": "{{ RoleArn }}"
 },
 "PaymentConfiguration": {
  "QueryCompute": {
   "IsResponsible": "{{ IsResponsible }}"
  }
 }
}
>>>
--all properties
INSERT INTO aws.cleanrooms.memberships (
 Tags,
 CollaborationIdentifier,
 QueryLogStatus,
 DefaultResultConfiguration,
 PaymentConfiguration,
 region
)
SELECT 
 {{ Tags }},
 {{ CollaborationIdentifier }},
 {{ QueryLogStatus }},
 {{ DefaultResultConfiguration }},
 {{ PaymentConfiguration }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cleanrooms.memberships
WHERE data__Identifier = '<MembershipIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>memberships</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateMembership,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:DescribeLogGroups,
logs:DescribeResourcePolicies,
logs:PutResourcePolicy,
logs:CreateLogGroup,
cleanrooms:GetMembership,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:ListMemberships,
iam:PassRole
```

### Delete
```json
cleanrooms:DeleteMembership,
cleanrooms:GetMembership,
cleanrooms:ListMemberships,
cleanrooms:ListTagsForResource,
logs:ListLogDeliveries,
logs:DescribeLogGroups,
logs:DescribeResourcePolicies,
logs:GetLogDelivery
```

### List
```json
cleanrooms:ListMemberships
```

