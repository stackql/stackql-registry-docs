---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - appconfig
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The environment ID.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the environment.</td></tr>
<tr><td><CopyableCode code="monitors" /></td><td><code>array</code></td><td>Amazon CloudWatch alarms to monitor during the deployment process.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the environment.</td></tr>
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
    <td><CopyableCode code="Name, ApplicationId, region" /></td>
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
List all <code>environments</code> in a region.
```sql
SELECT
region,
application_id,
environment_id
FROM aws.appconfig.environments
WHERE region = 'us-east-1';
```
Gets all properties from an <code>environment</code>.
```sql
SELECT
region,
environment_id,
description,
monitors,
application_id,
tags,
name
FROM aws.appconfig.environments
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<EnvironmentId>';
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
INSERT INTO aws.appconfig.environments (
 ApplicationId,
 Name,
 region
)
SELECT 
'{{ ApplicationId }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appconfig.environments (
 Description,
 Monitors,
 ApplicationId,
 Tags,
 Name,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Monitors }}',
 '{{ ApplicationId }}',
 '{{ Tags }}',
 '{{ Name }}',
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
      - name: Description
        value: '{{ Description }}'
      - name: Monitors
        value:
          - AlarmArn: '{{ AlarmArn }}'
            AlarmRoleArn: '{{ AlarmRoleArn }}'
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appconfig.environments
WHERE data__Identifier = '<ApplicationId|EnvironmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Read
```json
appconfig:GetEnvironment,
appconfig:ListTagsForResource
```

### Create
```json
appconfig:CreateEnvironment,
appconfig:GetEnvironment,
appconfig:ListTagsForResource,
appconfig:TagResource,
iam:PassRole
```

### Update
```json
appconfig:UpdateEnvironment,
appconfig:TagResource,
appconfig:UntagResource,
iam:PassRole
```

### List
```json
appconfig:ListEnvironments
```

### Delete
```json
appconfig:GetEnvironment,
appconfig:DeleteEnvironment
```

