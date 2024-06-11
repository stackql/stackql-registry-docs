---
title: configuration_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_templates
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

Creates, updates, deletes or gets a <code>configuration_template</code> resource or lists <code>configuration_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticBeanstalk::ConfigurationTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.configuration_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application to associate with this configuration template. </td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description for this configuration.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration. </td></tr>
<tr><td><CopyableCode code="option_settings" /></td><td><code>array</code></td><td>Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see &#91;Option Values&#93;(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide. </td></tr>
<tr><td><CopyableCode code="platform_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom platform. For more information, see &#91;Custom Platforms&#93;(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide. </td></tr>
<tr><td><CopyableCode code="solution_stack_name" /></td><td><code>string</code></td><td>The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see &#91;Supported Platforms&#93;(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide. You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration. Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks. </td></tr>
<tr><td><CopyableCode code="source_configuration" /></td><td><code>object</code></td><td>An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration. Values specified in OptionSettings override any values obtained from the SourceConfiguration. You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName. Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name. </td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td>The name of the configuration template</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>configuration_templates</code> in a region.
```sql
SELECT
region,
application_name,
template_name
FROM aws.elasticbeanstalk.configuration_templates
WHERE region = 'us-east-1';
```
Gets all properties from a <code>configuration_template</code>.
```sql
SELECT
region,
application_name,
description,
environment_id,
option_settings,
platform_arn,
solution_stack_name,
source_configuration,
template_name
FROM aws.elasticbeanstalk.configuration_templates
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationName>|<TemplateName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticbeanstalk.configuration_templates (
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
INSERT INTO aws.elasticbeanstalk.configuration_templates (
 ApplicationName,
 Description,
 EnvironmentId,
 OptionSettings,
 PlatformArn,
 SolutionStackName,
 SourceConfiguration,
 region
)
SELECT 
 '{{ ApplicationName }}',
 '{{ Description }}',
 '{{ EnvironmentId }}',
 '{{ OptionSettings }}',
 '{{ PlatformArn }}',
 '{{ SolutionStackName }}',
 '{{ SourceConfiguration }}',
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
  - name: configuration_template
    props:
      - name: ApplicationName
        value: '{{ ApplicationName }}'
      - name: Description
        value: '{{ Description }}'
      - name: EnvironmentId
        value: '{{ EnvironmentId }}'
      - name: OptionSettings
        value:
          - Namespace: '{{ Namespace }}'
            OptionName: '{{ OptionName }}'
            ResourceName: '{{ ResourceName }}'
            Value: '{{ Value }}'
      - name: PlatformArn
        value: '{{ PlatformArn }}'
      - name: SolutionStackName
        value: '{{ SolutionStackName }}'
      - name: SourceConfiguration
        value:
          ApplicationName: '{{ ApplicationName }}'
          TemplateName: '{{ TemplateName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticbeanstalk.configuration_templates
WHERE data__Identifier = '<ApplicationName|TemplateName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configuration_templates</code> resource, the following permissions are required:

### Create
```json
elasticbeanstalk:CreateConfigurationTemplate
```

### Read
```json
elasticbeanstalk:DescribeConfigurationSettings
```

### Update
```json
elasticbeanstalk:UpdateConfigurationTemplate
```

### Delete
```json
elasticbeanstalk:DeleteConfigurationTemplate,
elasticbeanstalk:DescribeConfigurationSettings
```

### List
```json
elasticbeanstalk:DescribeApplications
```

