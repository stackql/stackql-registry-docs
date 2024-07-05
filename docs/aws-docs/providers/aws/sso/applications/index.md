---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - sso
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
<tr><td><b>Description</b></td><td>Resource Type definition for Identity Center (SSO) Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Identity Center (SSO) Application</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description information for the Identity Center (SSO) Application</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The ARN of the instance of IAM Identity Center under which the operation will run</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The Application ARN that is returned upon creation of the Identity Center (SSO) Application</td></tr>
<tr><td><CopyableCode code="application_provider_arn" /></td><td><code>string</code></td><td>The ARN of the application provider under which the operation will run</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Specifies whether the application is enabled or disabled</td></tr>
<tr><td><CopyableCode code="portal_options" /></td><td><code>object</code></td><td>A structure that describes the options for the portal associated with an application</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, InstanceArn, ApplicationProviderArn, region" /></td>
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
name,
description,
instance_arn,
application_arn,
application_provider_arn,
status,
portal_options,
tags
FROM aws.sso.applications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application</code>.
```sql
SELECT
region,
name,
description,
instance_arn,
application_arn,
application_provider_arn,
status,
portal_options,
tags
FROM aws.sso.applications
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationArn>';
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
INSERT INTO aws.sso.applications (
 Name,
 InstanceArn,
 ApplicationProviderArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ InstanceArn }}',
 '{{ ApplicationProviderArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sso.applications (
 Name,
 Description,
 InstanceArn,
 ApplicationProviderArn,
 Status,
 PortalOptions,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ InstanceArn }}',
 '{{ ApplicationProviderArn }}',
 '{{ Status }}',
 '{{ PortalOptions }}',
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
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: ApplicationProviderArn
        value: '{{ ApplicationProviderArn }}'
      - name: Status
        value: '{{ Status }}'
      - name: PortalOptions
        value:
          Visibility: '{{ Visibility }}'
          SignInOptions:
            Origin: '{{ Origin }}'
            ApplicationUrl: '{{ ApplicationUrl }}'
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
DELETE FROM aws.sso.applications
WHERE data__Identifier = '<ApplicationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
sso:CreateApplication,
sso:DescribeApplication,
sso:TagResource
```

### Read
```json
sso:DescribeApplication,
sso:ListTagsForResource
```

### Update
```json
sso:UpdateApplication,
sso:TagResource,
sso:UntagResource,
sso:ListTagsForResource,
sso:DescribeApplication
```

### Delete
```json
sso:DeleteApplication
```

### List
```json
sso:ListApplications
```

