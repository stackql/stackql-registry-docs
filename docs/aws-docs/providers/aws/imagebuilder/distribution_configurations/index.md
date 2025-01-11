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

Creates, updates, deletes or gets a <code>distribution_configuration</code> resource or lists <code>distribution_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distribution_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::DistributionConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.distribution_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the distribution configuration.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the distribution configuration.</td></tr>
<tr><td><CopyableCode code="distributions" /></td><td><code>array</code></td><td>The distributions of the distribution configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the component.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html"><code>AWS::ImageBuilder::DistributionConfiguration</code></a>.

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
    <td><CopyableCode code="Name, Distributions, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>distribution_configurations</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
distributions,
tags
FROM aws.imagebuilder.distribution_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>distribution_configuration</code>.
```sql
SELECT
region,
arn,
name,
description,
distributions,
tags
FROM aws.imagebuilder.distribution_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>distribution_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.imagebuilder.distribution_configurations (
 Name,
 Distributions,
 region
)
SELECT 
'{{ Name }}',
 '{{ Distributions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.imagebuilder.distribution_configurations (
 Name,
 Description,
 Distributions,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Distributions }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: distribution_configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Distributions
        value:
          - Region: '{{ Region }}'
            AmiDistributionConfiguration:
              Name: '{{ Name }}'
              KmsKeyId: '{{ KmsKeyId }}'
              Description: '{{ Description }}'
              AmiTags: {}
              TargetAccountIds:
                - '{{ TargetAccountIds[0] }}'
              LaunchPermissionConfiguration:
                UserIds:
                  - '{{ UserIds[0] }}'
                UserGroups:
                  - '{{ UserGroups[0] }}'
                OrganizationArns:
                  - '{{ OrganizationArns[0] }}'
                OrganizationalUnitArns:
                  - '{{ OrganizationalUnitArns[0] }}'
            ContainerDistributionConfiguration:
              Description: '{{ Description }}'
              ContainerTags:
                - '{{ ContainerTags[0] }}'
              TargetRepository:
                Service: '{{ Service }}'
                RepositoryName: '{{ RepositoryName }}'
            LicenseConfigurationArns:
              - '{{ LicenseConfigurationArns[0] }}'
            LaunchTemplateConfigurations:
              - LaunchTemplateId: '{{ LaunchTemplateId }}'
                AccountId: '{{ AccountId }}'
                SetDefaultVersion: '{{ SetDefaultVersion }}'
            FastLaunchConfigurations:
              - AccountId: '{{ AccountId }}'
                Enabled: '{{ Enabled }}'
                LaunchTemplate:
                  LaunchTemplateId: '{{ LaunchTemplateId }}'
                  LaunchTemplateName: '{{ LaunchTemplateName }}'
                  LaunchTemplateVersion: '{{ LaunchTemplateVersion }}'
                MaxParallelLaunches: '{{ MaxParallelLaunches }}'
                SnapshotConfiguration:
                  TargetResourceCount: '{{ TargetResourceCount }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Update
```json
ec2:DescribeLaunchTemplates,
ec2:CreateLaunchTemplateVersion,
ec2:ModifyLaunchTemplate,
imagebuilder:GetDistributionConfiguration,
imagebuilder:UpdateDistributionConfiguration
```

### Read
```json
imagebuilder:GetDistributionConfiguration
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
