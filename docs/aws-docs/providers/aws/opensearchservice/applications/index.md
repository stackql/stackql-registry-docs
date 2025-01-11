---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - opensearchservice
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
<tr><td><b>Description</b></td><td>Amazon OpenSearchService application resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchservice.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="iam_identity_center_options" /></td><td><code>object</code></td><td>Options for configuring IAM Identity Center</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) format.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the application.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The endpoint for the application.</td></tr>
<tr><td><CopyableCode code="app_configs" /></td><td><code>array</code></td><td>List of application configurations.</td></tr>
<tr><td><CopyableCode code="data_sources" /></td><td><code>array</code></td><td>List of data sources.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this application.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-application.html"><code>AWS::OpenSearchService::Application</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
iam_identity_center_options,
arn,
id,
name,
endpoint,
app_configs,
data_sources,
tags
FROM aws.opensearchservice.applications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application</code>.
```sql
SELECT
region,
iam_identity_center_options,
arn,
id,
name,
endpoint,
app_configs,
data_sources,
tags
FROM aws.opensearchservice.applications
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
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
INSERT INTO aws.opensearchservice.applications (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.opensearchservice.applications (
 IamIdentityCenterOptions,
 Name,
 Endpoint,
 AppConfigs,
 DataSources,
 Tags,
 region
)
SELECT 
 '{{ IamIdentityCenterOptions }}',
 '{{ Name }}',
 '{{ Endpoint }}',
 '{{ AppConfigs }}',
 '{{ DataSources }}',
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
      - name: IamIdentityCenterOptions
        value:
          Enabled: '{{ Enabled }}'
          IamIdentityCenterInstanceArn: '{{ IamIdentityCenterInstanceArn }}'
          IamRoleForIdentityCenterApplicationArn: '{{ IamRoleForIdentityCenterApplicationArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Endpoint
        value: '{{ Endpoint }}'
      - name: AppConfigs
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: DataSources
        value:
          - DataSourceArn: '{{ DataSourceArn }}'
            DataSourceDescription: '{{ DataSourceDescription }}'
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
DELETE FROM aws.opensearchservice.applications
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
es:CreateApplication,
es:GetApplication,
es:AddTags,
es:ListTags,
iam:CreateServiceLinkedRole
```

### Read
```json
es:GetApplication,
es:ListTags
```

### Update
```json
es:UpdateApplication,
es:GetApplication,
es:AddTags,
es:RemoveTags,
es:ListTags
```

### Delete
```json
es:GetApplication,
es:DeleteApplication
```

### List
```json
es:ListApplications
```
