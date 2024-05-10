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


Used to retrieve a list of <code>configuration_templates</code> in a region or to create or delete a <code>configuration_templates</code> resource, use <code>configuration_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticBeanstalk::ConfigurationTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.configuration_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application to associate with this configuration template. </td></tr>
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
application_name,
template_name
FROM aws.elasticbeanstalk.configuration_templates
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>configuration_template</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- configuration_template.iql (required properties only)
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
-- configuration_template.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
elasticbeanstalk:DeleteConfigurationTemplate,
elasticbeanstalk:DescribeConfigurationSettings
```

### List
```json
elasticbeanstalk:DescribeApplications
```

