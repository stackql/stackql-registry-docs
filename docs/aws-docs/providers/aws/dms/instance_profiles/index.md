---
title: instance_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_profiles
  - dms
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


Used to retrieve a list of <code>instance_profiles</code> in a region or to create or delete a <code>instance_profiles</code> resource, use <code>instance_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::InstanceProfile.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.instance_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_profile_arn" /></td><td><code>string</code></td><td>The property describes an ARN of the instance profile.</td></tr>
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
instance_profile_arn
FROM aws.dms.instance_profiles
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
 "InstanceProfileIdentifier": "{{ InstanceProfileIdentifier }}",
 "AvailabilityZone": "{{ AvailabilityZone }}",
 "Description": "{{ Description }}",
 "KmsKeyArn": "{{ KmsKeyArn }}",
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "NetworkType": "{{ NetworkType }}",
 "InstanceProfileName": "{{ InstanceProfileName }}",
 "SubnetGroupIdentifier": "{{ SubnetGroupIdentifier }}",
 "VpcSecurityGroups": [
  "{{ VpcSecurityGroups[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.dms.instance_profiles (
 InstanceProfileIdentifier,
 AvailabilityZone,
 Description,
 KmsKeyArn,
 PubliclyAccessible,
 NetworkType,
 InstanceProfileName,
 SubnetGroupIdentifier,
 VpcSecurityGroups,
 Tags,
 region
)
SELECT 
{{ .InstanceProfileIdentifier }},
 {{ .AvailabilityZone }},
 {{ .Description }},
 {{ .KmsKeyArn }},
 {{ .PubliclyAccessible }},
 {{ .NetworkType }},
 {{ .InstanceProfileName }},
 {{ .SubnetGroupIdentifier }},
 {{ .VpcSecurityGroups }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceProfileIdentifier": "{{ InstanceProfileIdentifier }}",
 "AvailabilityZone": "{{ AvailabilityZone }}",
 "Description": "{{ Description }}",
 "KmsKeyArn": "{{ KmsKeyArn }}",
 "PubliclyAccessible": "{{ PubliclyAccessible }}",
 "NetworkType": "{{ NetworkType }}",
 "InstanceProfileName": "{{ InstanceProfileName }}",
 "SubnetGroupIdentifier": "{{ SubnetGroupIdentifier }}",
 "VpcSecurityGroups": [
  "{{ VpcSecurityGroups[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.dms.instance_profiles (
 InstanceProfileIdentifier,
 AvailabilityZone,
 Description,
 KmsKeyArn,
 PubliclyAccessible,
 NetworkType,
 InstanceProfileName,
 SubnetGroupIdentifier,
 VpcSecurityGroups,
 Tags,
 region
)
SELECT 
 {{ .InstanceProfileIdentifier }},
 {{ .AvailabilityZone }},
 {{ .Description }},
 {{ .KmsKeyArn }},
 {{ .PubliclyAccessible }},
 {{ .NetworkType }},
 {{ .InstanceProfileName }},
 {{ .SubnetGroupIdentifier }},
 {{ .VpcSecurityGroups }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.dms.instance_profiles
WHERE data__Identifier = '<InstanceProfileArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>instance_profiles</code> resource, the following permissions are required:

### Create
```json
dms:CreateInstanceProfile,
dms:ListInstanceProfiles,
dms:DescribeInstanceProfiles,
dms:AddTagsToResource,
dms:ListTagsForResource
```

### Delete
```json
dms:DeleteInstanceProfile
```

### List
```json
dms:ListInstanceProfiles,
dms:DescribeInstanceProfiles,
dms:ListTagsForResource
```

