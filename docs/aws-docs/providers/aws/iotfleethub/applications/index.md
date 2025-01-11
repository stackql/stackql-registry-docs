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

Creates, updates, deletes or gets an <code>application</code> resource or lists <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTFleetHub::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleethub.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The ID of the application.</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the application.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>Application Name, should be between 1 and 256 characters.</td></tr>
<tr><td><CopyableCode code="application_description" /></td><td><code>string</code></td><td>Application Description, should be between 1 and 2048 characters.</td></tr>
<tr><td><CopyableCode code="application_url" /></td><td><code>string</code></td><td>The URL of the application.</td></tr>
<tr><td><CopyableCode code="application_state" /></td><td><code>string</code></td><td>The current state of the application.</td></tr>
<tr><td><CopyableCode code="application_creation_date" /></td><td><code>integer</code></td><td>When the Application was created</td></tr>
<tr><td><CopyableCode code="application_last_update_date" /></td><td><code>integer</code></td><td>When the Application was last updated</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax</td></tr>
<tr><td><CopyableCode code="sso_client_id" /></td><td><code>string</code></td><td>The AWS SSO application generated client ID (used with AWS SSO APIs).</td></tr>
<tr><td><CopyableCode code="error_message" /></td><td><code>string</code></td><td>A message indicating why Create or Delete Application failed.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the application.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleethub-application.html"><code>AWS::IoTFleetHub::Application</code></a>.

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
    <td><CopyableCode code="ApplicationName, RoleArn, region" /></td>
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
Gets all <code>applications</code> in a region.
```sql
SELECT
region,
application_id,
application_arn,
application_name,
application_description,
application_url,
application_state,
application_creation_date,
application_last_update_date,
role_arn,
sso_client_id,
error_message,
tags
FROM aws.iotfleethub.applications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application</code>.
```sql
SELECT
region,
application_id,
application_arn,
application_name,
application_description,
application_url,
application_state,
application_creation_date,
application_last_update_date,
role_arn,
sso_client_id,
error_message,
tags
FROM aws.iotfleethub.applications
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iotfleethub:DescribeApplication
```

### Update
```json
iotfleethub:UpdateApplication,
iotfleethub:DescribeApplication,
iotfleethub:TagResource,
iotfleethub:UntagResource
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
