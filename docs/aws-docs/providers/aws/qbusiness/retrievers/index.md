---
title: retrievers
hide_title: false
hide_table_of_contents: false
keywords:
  - retrievers
  - qbusiness
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

Creates, updates, deletes or gets a <code>retriever</code> resource or lists <code>retrievers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>retrievers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::Retriever Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.retrievers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="retriever_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="retriever_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html"><code>AWS::QBusiness::Retriever</code></a>.

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
    <td><CopyableCode code="ApplicationId, Configuration, DisplayName, Type, region" /></td>
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
Gets all <code>retrievers</code> in a region.
```sql
SELECT
region,
application_id,
configuration,
created_at,
display_name,
retriever_arn,
retriever_id,
role_arn,
status,
tags,
type,
updated_at
FROM aws.qbusiness.retrievers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>retriever</code>.
```sql
SELECT
region,
application_id,
configuration,
created_at,
display_name,
retriever_arn,
retriever_id,
role_arn,
status,
tags,
type,
updated_at
FROM aws.qbusiness.retrievers
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<RetrieverId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>retriever</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.qbusiness.retrievers (
 ApplicationId,
 Configuration,
 DisplayName,
 Type,
 region
)
SELECT 
'{{ ApplicationId }}',
 '{{ Configuration }}',
 '{{ DisplayName }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.qbusiness.retrievers (
 ApplicationId,
 Configuration,
 DisplayName,
 RoleArn,
 Tags,
 Type,
 region
)
SELECT 
 '{{ ApplicationId }}',
 '{{ Configuration }}',
 '{{ DisplayName }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ Type }}',
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
  - name: retriever
    props:
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: Configuration
        value: null
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.qbusiness.retrievers
WHERE data__Identifier = '<ApplicationId|RetrieverId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>retrievers</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
qbusiness:CreateRetriever,
qbusiness:GetRetriever,
qbusiness:ListTagsForResource,
qbusiness:TagResource
```

### Read
```json
qbusiness:GetRetriever,
qbusiness:ListTagsForResource
```

### Update
```json
iam:PassRole,
qbusiness:GetRetriever,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UntagResource,
qbusiness:UpdateRetriever
```

### Delete
```json
qbusiness:DeleteRetriever,
qbusiness:GetRetriever
```

### List
```json
qbusiness:ListRetrievers
```
