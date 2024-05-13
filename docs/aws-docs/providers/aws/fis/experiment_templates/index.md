---
title: experiment_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment_templates
  - fis
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


Used to retrieve a list of <code>experiment_templates</code> in a region or to create or delete a <code>experiment_templates</code> resource, use <code>experiment_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::FIS::ExperimentTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fis.experiment_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="Description, StopConditions, Targets, RoleArn, Tags, region" /></td>
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
id
FROM aws.fis.experiment_templates
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>experiment_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.fis.experiment_templates (
 Description,
 Targets,
 StopConditions,
 RoleArn,
 Tags,
 region
)
SELECT 
'{{ Description }}',
 '{{ Targets }}',
 '{{ StopConditions }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.fis.experiment_templates (
 Description,
 Targets,
 Actions,
 StopConditions,
 LogConfiguration,
 RoleArn,
 Tags,
 ExperimentOptions,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Targets }}',
 '{{ Actions }}',
 '{{ StopConditions }}',
 '{{ LogConfiguration }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ ExperimentOptions }}',
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
  - name: experiment_template
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Targets
        value: {}
      - name: Actions
        value: {}
      - name: StopConditions
        value:
          - Source: '{{ Source }}'
            Value: '{{ Value }}'
      - name: LogConfiguration
        value:
          CloudWatchLogsConfiguration:
            LogGroupArn: '{{ LogGroupArn }}'
          S3Configuration:
            BucketName: '{{ BucketName }}'
            Prefix: '{{ Prefix }}'
          LogSchemaVersion: '{{ LogSchemaVersion }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value: {}
      - name: ExperimentOptions
        value:
          AccountTargeting: '{{ AccountTargeting }}'
          EmptyTargetResolutionMode: '{{ EmptyTargetResolutionMode }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.fis.experiment_templates
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>experiment_templates</code> resource, the following permissions are required:

### Create
```json
fis:CreateExperimentTemplate,
fis:TagResource,
iam:PassRole
```

### Delete
```json
fis:DeleteExperimentTemplate
```

### List
```json
fis:ListExperimentTemplates,
fis:ListTagsForResource
```

