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

Creates, updates, deletes or gets an <code>environment</code> resource or lists <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticBeanstalk::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="platform_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom platform to use with the environment.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application that is associated with this environment.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Your description for this environment.</td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td>A unique name for the environment.</td></tr>
<tr><td><CopyableCode code="operations_role" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>object</code></td><td>Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.</td></tr>
<tr><td><CopyableCode code="version_label" /></td><td><code>string</code></td><td>The name of the application version to deploy.</td></tr>
<tr><td><CopyableCode code="endpoint_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="option_settings" /></td><td><code>array</code></td><td>Key-value pairs defining configuration options for this environment, such as the instance type.</td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td>The name of the Elastic Beanstalk configuration template to use with the environment.</td></tr>
<tr><td><CopyableCode code="solution_stack_name" /></td><td><code>string</code></td><td>The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.</td></tr>
<tr><td><CopyableCode code="cname_prefix" /></td><td><code>string</code></td><td>If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Specifies the tags applied to resources in the environment.</td></tr>
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
    <td><CopyableCode code="ApplicationName, region" /></td>
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
Gets all <code>environments</code> in a region.
```sql
SELECT
region,
platform_arn,
application_name,
description,
environment_name,
operations_role,
tier,
version_label,
endpoint_url,
option_settings,
template_name,
solution_stack_name,
cname_prefix,
tags
FROM aws.elasticbeanstalk.environments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>environment</code>.
```sql
SELECT
region,
platform_arn,
application_name,
description,
environment_name,
operations_role,
tier,
version_label,
endpoint_url,
option_settings,
template_name,
solution_stack_name,
cname_prefix,
tags
FROM aws.elasticbeanstalk.environments
WHERE region = 'us-east-1' AND data__Identifier = '<EnvironmentName>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticbeanstalk.environments
WHERE data__Identifier = '<EnvironmentName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Read
```json
elasticbeanstalk:DescribeEnvironments,
elasticbeanstalk:DescribeConfigurationSettings,
elasticbeanstalk:ListTagsForResource
```

### Create
```json
elasticbeanstalk:DescribeEnvironments,
elasticbeanstalk:CreateEnvironment,
iam:PassRole
```

### Update
```json
elasticbeanstalk:DescribeEnvironments,
elasticbeanstalk:UpdateEnvironment,
elasticbeanstalk:UpdateTagsForResource,
elasticbeanstalk:AssociateEnvironmentOperationsRole,
elasticbeanstalk:DisassociateEnvironmentOperationsRole,
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

