---
title: configured_table_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - configured_table_associations
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


Used to retrieve a list of <code>configured_table_associations</code> in a region or to create or delete a <code>configured_table_associations</code> resource, use <code>configured_table_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_table_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a table that can be queried within a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.configured_table_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configured_table_association_identifier" /></td><td><code>string</code></td><td></td></tr>
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
configured_table_association_identifier,
membership_identifier
FROM aws.cleanrooms.configured_table_associations
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
 "ConfiguredTableIdentifier": "{{ ConfiguredTableIdentifier }}",
 "MembershipIdentifier": "{{ MembershipIdentifier }}",
 "Name": "{{ Name }}",
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.cleanrooms.configured_table_associations (
 ConfiguredTableIdentifier,
 MembershipIdentifier,
 Name,
 RoleArn,
 region
)
SELECT 
{{ .ConfiguredTableIdentifier }},
 {{ .MembershipIdentifier }},
 {{ .Name }},
 {{ .RoleArn }},
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
 "ConfiguredTableIdentifier": "{{ ConfiguredTableIdentifier }}",
 "Description": "{{ Description }}",
 "MembershipIdentifier": "{{ MembershipIdentifier }}",
 "Name": "{{ Name }}",
 "RoleArn": "{{ RoleArn }}"
}
>>>
--all properties
INSERT INTO aws.cleanrooms.configured_table_associations (
 Tags,
 ConfiguredTableIdentifier,
 Description,
 MembershipIdentifier,
 Name,
 RoleArn,
 region
)
SELECT 
 {{ .Tags }},
 {{ .ConfiguredTableIdentifier }},
 {{ .Description }},
 {{ .MembershipIdentifier }},
 {{ .Name }},
 {{ .RoleArn }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cleanrooms.configured_table_associations
WHERE data__Identifier = '<ConfiguredTableAssociationIdentifier|MembershipIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configured_table_associations</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateConfiguredTableAssociation,
iam:PassRole,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetConfiguredTableAssociation,
cleanrooms:ListConfiguredTableAssociations
```

### Delete
```json
cleanrooms:DeleteConfiguredTableAssociation,
cleanrooms:GetConfiguredTableAssociation,
cleanrooms:ListConfiguredTableAssociations,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource
```

### List
```json
cleanrooms:ListConfiguredTableAssociations
```

