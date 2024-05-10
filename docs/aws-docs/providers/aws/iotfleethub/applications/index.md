---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - iotfleethub
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


Used to retrieve a list of <code>applications</code> in a region or to create or delete a <code>applications</code> resource, use <code>application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTFleetHub::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleethub.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The ID of the application.</td></tr>
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
application_id
FROM aws.iotfleethub.applications
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- application.iql (required properties only)
INSERT INTO aws.iotfleethub.applications (
 ApplicationName,
 RoleArn,
 region
)
SELECT 
'{{ ApplicationName }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- application.iql (all properties)
INSERT INTO aws.iotfleethub.applications (
 ApplicationName,
 ApplicationDescription,
 RoleArn,
 Tags,
 region
)
SELECT 
 '{{ ApplicationName }}',
 '{{ ApplicationDescription }}',
 '{{ RoleArn }}',
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
  - name: application
    props:
      - name: ApplicationName
        value: '{{ ApplicationName }}'
      - name: ApplicationDescription
        value: '{{ ApplicationDescription }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotfleethub.applications
WHERE data__Identifier = '<ApplicationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
iotfleethub:CreateApplication,
iotfleethub:TagResource,
iam:PassRole,
sso:CreateManagedApplicationInstance,
sso:DescribeRegisteredRegions
```

### Delete
```json
iotfleethub:DeleteApplication,
iotfleethub:DescribeApplication,
sso:DeleteManagedApplicationInstance
```

### List
```json
iotfleethub:ListApplications
```

