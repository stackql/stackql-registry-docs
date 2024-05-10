---
title: infrastructure_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_configurations
  - imagebuilder
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


Used to retrieve a list of <code>infrastructure_configurations</code> in a region or to create or delete a <code>infrastructure_configurations</code> resource, use <code>infrastructure_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>infrastructure_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::InfrastructureConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.infrastructure_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
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
arn
FROM aws.imagebuilder.infrastructure_configurations
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
 "Name": "{{ Name }}",
 "InstanceProfileName": "{{ InstanceProfileName }}"
}
>>>
--required properties only
INSERT INTO aws.imagebuilder.infrastructure_configurations (
 Name,
 InstanceProfileName,
 region
)
SELECT 
{{ Name }},
 {{ InstanceProfileName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "InstanceTypes": [
  "{{ InstanceTypes[0] }}"
 ],
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "Logging": {
  "S3Logs": {
   "S3BucketName": "{{ S3BucketName }}",
   "S3KeyPrefix": "{{ S3KeyPrefix }}"
  }
 },
 "SubnetId": "{{ SubnetId }}",
 "KeyPair": "{{ KeyPair }}",
 "TerminateInstanceOnFailure": "{{ TerminateInstanceOnFailure }}",
 "InstanceProfileName": "{{ InstanceProfileName }}",
 "InstanceMetadataOptions": {
  "HttpPutResponseHopLimit": "{{ HttpPutResponseHopLimit }}",
  "HttpTokens": "{{ HttpTokens }}"
 },
 "SnsTopicArn": "{{ SnsTopicArn }}",
 "ResourceTags": {},
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.imagebuilder.infrastructure_configurations (
 Name,
 Description,
 InstanceTypes,
 SecurityGroupIds,
 Logging,
 SubnetId,
 KeyPair,
 TerminateInstanceOnFailure,
 InstanceProfileName,
 InstanceMetadataOptions,
 SnsTopicArn,
 ResourceTags,
 Tags,
 region
)
SELECT 
 {{ Name }},
 {{ Description }},
 {{ InstanceTypes }},
 {{ SecurityGroupIds }},
 {{ Logging }},
 {{ SubnetId }},
 {{ KeyPair }},
 {{ TerminateInstanceOnFailure }},
 {{ InstanceProfileName }},
 {{ InstanceMetadataOptions }},
 {{ SnsTopicArn }},
 {{ ResourceTags }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.imagebuilder.infrastructure_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>infrastructure_configurations</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iam:GetRole,
iam:GetInstanceProfile,
iam:CreateServiceLinkedRole,
sns:Publish,
imagebuilder:TagResource,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:CreateInfrastructureConfiguration
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:DeleteInfrastructureConfiguration
```

### List
```json
imagebuilder:ListInfrastructureConfigurations
```

