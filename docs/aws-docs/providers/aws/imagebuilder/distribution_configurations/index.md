---
title: distribution_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - distribution_configurations
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


Used to retrieve a list of <code>distribution_configurations</code> in a region or to create or delete a <code>distribution_configurations</code> resource, use <code>distribution_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distribution_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::DistributionConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.distribution_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration.</td></tr>
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
FROM aws.imagebuilder.distribution_configurations
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
 "Distributions": [
  {
   "Region": "{{ Region }}",
   "AmiDistributionConfiguration": {
    "Name": "{{ Name }}",
    "KmsKeyId": "{{ KmsKeyId }}",
    "Description": "{{ Description }}",
    "AmiTags": {},
    "TargetAccountIds": [
     "{{ TargetAccountIds[0] }}"
    ],
    "LaunchPermissionConfiguration": {
     "UserIds": [
      "{{ UserIds[0] }}"
     ],
     "UserGroups": [
      "{{ UserGroups[0] }}"
     ],
     "OrganizationArns": [
      "{{ OrganizationArns[0] }}"
     ],
     "OrganizationalUnitArns": [
      "{{ OrganizationalUnitArns[0] }}"
     ]
    }
   },
   "ContainerDistributionConfiguration": {
    "Description": "{{ Description }}",
    "ContainerTags": [
     "{{ ContainerTags[0] }}"
    ],
    "TargetRepository": {
     "Service": "{{ Service }}",
     "RepositoryName": "{{ RepositoryName }}"
    }
   },
   "LicenseConfigurationArns": [
    "{{ LicenseConfigurationArns[0] }}"
   ],
   "LaunchTemplateConfigurations": [
    {
     "LaunchTemplateId": "{{ LaunchTemplateId }}",
     "AccountId": "{{ AccountId }}",
     "SetDefaultVersion": "{{ SetDefaultVersion }}"
    }
   ],
   "FastLaunchConfigurations": [
    {
     "AccountId": "{{ AccountId }}",
     "Enabled": "{{ Enabled }}",
     "LaunchTemplate": {
      "LaunchTemplateId": "{{ LaunchTemplateId }}",
      "LaunchTemplateName": "{{ LaunchTemplateName }}",
      "LaunchTemplateVersion": "{{ LaunchTemplateVersion }}"
     },
     "MaxParallelLaunches": "{{ MaxParallelLaunches }}",
     "SnapshotConfiguration": {
      "TargetResourceCount": "{{ TargetResourceCount }}"
     }
    }
   ]
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.imagebuilder.distribution_configurations (
 Name,
 Distributions,
 region
)
SELECT 
{{ .Name }},
 {{ .Distributions }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "Distributions": [
  {
   "Region": "{{ Region }}",
   "AmiDistributionConfiguration": {
    "Name": "{{ Name }}",
    "KmsKeyId": "{{ KmsKeyId }}",
    "Description": "{{ Description }}",
    "AmiTags": {},
    "TargetAccountIds": [
     "{{ TargetAccountIds[0] }}"
    ],
    "LaunchPermissionConfiguration": {
     "UserIds": [
      "{{ UserIds[0] }}"
     ],
     "UserGroups": [
      "{{ UserGroups[0] }}"
     ],
     "OrganizationArns": [
      "{{ OrganizationArns[0] }}"
     ],
     "OrganizationalUnitArns": [
      "{{ OrganizationalUnitArns[0] }}"
     ]
    }
   },
   "ContainerDistributionConfiguration": {
    "Description": "{{ Description }}",
    "ContainerTags": [
     "{{ ContainerTags[0] }}"
    ],
    "TargetRepository": {
     "Service": "{{ Service }}",
     "RepositoryName": "{{ RepositoryName }}"
    }
   },
   "LicenseConfigurationArns": [
    "{{ LicenseConfigurationArns[0] }}"
   ],
   "LaunchTemplateConfigurations": [
    {
     "LaunchTemplateId": "{{ LaunchTemplateId }}",
     "AccountId": "{{ AccountId }}",
     "SetDefaultVersion": "{{ SetDefaultVersion }}"
    }
   ],
   "FastLaunchConfigurations": [
    {
     "AccountId": "{{ AccountId }}",
     "Enabled": "{{ Enabled }}",
     "LaunchTemplate": {
      "LaunchTemplateId": "{{ LaunchTemplateId }}",
      "LaunchTemplateName": "{{ LaunchTemplateName }}",
      "LaunchTemplateVersion": "{{ LaunchTemplateVersion }}"
     },
     "MaxParallelLaunches": "{{ MaxParallelLaunches }}",
     "SnapshotConfiguration": {
      "TargetResourceCount": "{{ TargetResourceCount }}"
     }
    }
   ]
  }
 ],
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.imagebuilder.distribution_configurations (
 Name,
 Description,
 Distributions,
 Tags,
 region
)
SELECT 
 {{ .Name }},
 {{ .Description }},
 {{ .Distributions }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.imagebuilder.distribution_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>distribution_configurations</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:CreateServiceLinkedRole,
ec2:DescribeLaunchTemplates,
ec2:CreateLaunchTemplateVersion,
ec2:ModifyLaunchTemplate,
imagebuilder:TagResource,
imagebuilder:GetDistributionConfiguration,
imagebuilder:CreateDistributionConfiguration
```

### Delete
```json
imagebuilder:GetDistributionConfiguration,
imagebuilder:UnTagResource,
imagebuilder:DeleteDistributionConfiguration
```

### List
```json
imagebuilder:ListDistributionConfigurations
```

