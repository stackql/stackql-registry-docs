---
title: container_recipes
hide_title: false
hide_table_of_contents: false
keywords:
  - container_recipes
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


Used to retrieve a list of <code>container_recipes</code> in a region or to create or delete a <code>container_recipes</code> resource, use <code>container_recipe</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_recipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ContainerRecipe</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.container_recipes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe.</td></tr>
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
FROM aws.imagebuilder.container_recipes
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
 "Description": "{{ Description }}",
 "Version": "{{ Version }}",
 "Components": [
  {
   "ComponentArn": "{{ ComponentArn }}",
   "Parameters": [
    {
     "Name": "{{ Name }}",
     "Value": [
      "{{ Value[0] }}"
     ]
    }
   ]
  }
 ],
 "InstanceConfiguration": {
  "Image": "{{ Image }}",
  "BlockDeviceMappings": [
   {
    "DeviceName": "{{ DeviceName }}",
    "VirtualName": "{{ VirtualName }}",
    "NoDevice": "{{ NoDevice }}",
    "Ebs": {
     "Encrypted": "{{ Encrypted }}",
     "DeleteOnTermination": "{{ DeleteOnTermination }}",
     "Iops": "{{ Iops }}",
     "KmsKeyId": "{{ KmsKeyId }}",
     "SnapshotId": "{{ SnapshotId }}",
     "Throughput": "{{ Throughput }}",
     "VolumeSize": "{{ VolumeSize }}",
     "VolumeType": "{{ VolumeType }}"
    }
   }
  ]
 },
 "DockerfileTemplateData": "{{ DockerfileTemplateData }}",
 "DockerfileTemplateUri": "{{ DockerfileTemplateUri }}",
 "PlatformOverride": "{{ PlatformOverride }}",
 "ContainerType": "{{ ContainerType }}",
 "ImageOsVersionOverride": "{{ ImageOsVersionOverride }}",
 "TargetRepository": {
  "Service": "{{ Service }}",
  "RepositoryName": "{{ RepositoryName }}"
 },
 "KmsKeyId": "{{ KmsKeyId }}",
 "ParentImage": "{{ ParentImage }}",
 "WorkingDirectory": "{{ WorkingDirectory }}",
 "Tags": {}
}
>>>
--required properties only
INSERT INTO aws.imagebuilder.container_recipes (
 Name,
 Description,
 Version,
 Components,
 InstanceConfiguration,
 DockerfileTemplateData,
 DockerfileTemplateUri,
 PlatformOverride,
 ContainerType,
 ImageOsVersionOverride,
 TargetRepository,
 KmsKeyId,
 ParentImage,
 WorkingDirectory,
 Tags,
 region
)
SELECT 
{{ .Name }},
 {{ .Description }},
 {{ .Version }},
 {{ .Components }},
 {{ .InstanceConfiguration }},
 {{ .DockerfileTemplateData }},
 {{ .DockerfileTemplateUri }},
 {{ .PlatformOverride }},
 {{ .ContainerType }},
 {{ .ImageOsVersionOverride }},
 {{ .TargetRepository }},
 {{ .KmsKeyId }},
 {{ .ParentImage }},
 {{ .WorkingDirectory }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "Version": "{{ Version }}",
 "Components": [
  {
   "ComponentArn": "{{ ComponentArn }}",
   "Parameters": [
    {
     "Name": "{{ Name }}",
     "Value": [
      "{{ Value[0] }}"
     ]
    }
   ]
  }
 ],
 "InstanceConfiguration": {
  "Image": "{{ Image }}",
  "BlockDeviceMappings": [
   {
    "DeviceName": "{{ DeviceName }}",
    "VirtualName": "{{ VirtualName }}",
    "NoDevice": "{{ NoDevice }}",
    "Ebs": {
     "Encrypted": "{{ Encrypted }}",
     "DeleteOnTermination": "{{ DeleteOnTermination }}",
     "Iops": "{{ Iops }}",
     "KmsKeyId": "{{ KmsKeyId }}",
     "SnapshotId": "{{ SnapshotId }}",
     "Throughput": "{{ Throughput }}",
     "VolumeSize": "{{ VolumeSize }}",
     "VolumeType": "{{ VolumeType }}"
    }
   }
  ]
 },
 "DockerfileTemplateData": "{{ DockerfileTemplateData }}",
 "DockerfileTemplateUri": "{{ DockerfileTemplateUri }}",
 "PlatformOverride": "{{ PlatformOverride }}",
 "ContainerType": "{{ ContainerType }}",
 "ImageOsVersionOverride": "{{ ImageOsVersionOverride }}",
 "TargetRepository": {
  "Service": "{{ Service }}",
  "RepositoryName": "{{ RepositoryName }}"
 },
 "KmsKeyId": "{{ KmsKeyId }}",
 "ParentImage": "{{ ParentImage }}",
 "WorkingDirectory": "{{ WorkingDirectory }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.imagebuilder.container_recipes (
 Name,
 Description,
 Version,
 Components,
 InstanceConfiguration,
 DockerfileTemplateData,
 DockerfileTemplateUri,
 PlatformOverride,
 ContainerType,
 ImageOsVersionOverride,
 TargetRepository,
 KmsKeyId,
 ParentImage,
 WorkingDirectory,
 Tags,
 region
)
SELECT 
 {{ .Name }},
 {{ .Description }},
 {{ .Version }},
 {{ .Components }},
 {{ .InstanceConfiguration }},
 {{ .DockerfileTemplateData }},
 {{ .DockerfileTemplateUri }},
 {{ .PlatformOverride }},
 {{ .ContainerType }},
 {{ .ImageOsVersionOverride }},
 {{ .TargetRepository }},
 {{ .KmsKeyId }},
 {{ .ParentImage }},
 {{ .WorkingDirectory }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.imagebuilder.container_recipes
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>container_recipes</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:CreateServiceLinkedRole,
imagebuilder:GetComponent,
imagebuilder:TagResource,
imagebuilder:GetContainerRecipe,
imagebuilder:CreateContainerRecipe,
imagebuilder:GetImage,
kms:Encrypt,
kms:Decrypt,
kms:ReEncryptFrom,
kms:ReEncryptTo,
kms:GenerateDataKey*,
s3:GetObject,
s3:ListBucket,
ecr:DescribeRepositories,
ec2:DescribeImages
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetContainerRecipe,
imagebuilder:DeleteContainerRecipe
```

### List
```json
imagebuilder:ListContainerRecipes
```

