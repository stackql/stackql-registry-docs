---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - elasticbeanstalk
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


Used to retrieve a list of <code>environments</code> in a region or to create or delete a <code>environments</code> resource, use <code>environment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticBeanstalk::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td>A unique name for the environment.</td></tr>
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
environment_name
FROM aws.elasticbeanstalk.environments
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>environment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- environment.iql (required properties only)
INSERT INTO aws.elasticbeanstalk.environments (
 ApplicationName,
 region
)
SELECT 
'{{ ApplicationName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- environment.iql (all properties)
INSERT INTO aws.elasticbeanstalk.environments (
 PlatformArn,
 ApplicationName,
 Description,
 EnvironmentName,
 OperationsRole,
 Tier,
 VersionLabel,
 OptionSettings,
 TemplateName,
 SolutionStackName,
 CNAMEPrefix,
 Tags,
 region
)
SELECT 
 '{{ PlatformArn }}',
 '{{ ApplicationName }}',
 '{{ Description }}',
 '{{ EnvironmentName }}',
 '{{ OperationsRole }}',
 '{{ Tier }}',
 '{{ VersionLabel }}',
 '{{ OptionSettings }}',
 '{{ TemplateName }}',
 '{{ SolutionStackName }}',
 '{{ CNAMEPrefix }}',
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
  - name: environment
    props:
      - name: PlatformArn
        value: '{{ PlatformArn }}'
      - name: ApplicationName
        value: '{{ ApplicationName }}'
      - name: Description
        value: '{{ Description }}'
      - name: EnvironmentName
        value: '{{ EnvironmentName }}'
      - name: OperationsRole
        value: '{{ OperationsRole }}'
      - name: Tier
        value:
          Type: '{{ Type }}'
          Version: '{{ Version }}'
          Name: '{{ Name }}'
      - name: VersionLabel
        value: '{{ VersionLabel }}'
      - name: OptionSettings
        value:
          - ResourceName: '{{ ResourceName }}'
            Value: '{{ Value }}'
            Namespace: '{{ Namespace }}'
            OptionName: '{{ OptionName }}'
      - name: TemplateName
        value: '{{ TemplateName }}'
      - name: SolutionStackName
        value: '{{ SolutionStackName }}'
      - name: CNAMEPrefix
        value: '{{ CNAMEPrefix }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.elasticbeanstalk.environments
WHERE data__Identifier = '<EnvironmentName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
elasticbeanstalk:DescribeEnvironments,
elasticbeanstalk:CreateEnvironment,
iam:PassRole
```

### List
```json
elasticbeanstalk:DescribeEnvironments
```

### Delete
```json
elasticbeanstalk:DescribeEnvironments,
elasticbeanstalk:TerminateEnvironment
```

