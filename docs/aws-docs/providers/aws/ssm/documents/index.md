---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - ssm
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

Creates, updates, deletes or gets a <code>document</code> resource or lists <code>documents</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.documents" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The content for the Systems Manager document in JSON, YAML or String format.</td></tr>
<tr><td><CopyableCode code="attachments" /></td><td><code>array</code></td><td>A list of key and value pairs that describe attachments to a version of a document.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the Systems Manager document.</td></tr>
<tr><td><CopyableCode code="version_name" /></td><td><code>string</code></td><td>An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.</td></tr>
<tr><td><CopyableCode code="document_type" /></td><td><code>string</code></td><td>The type of document to create.</td></tr>
<tr><td><CopyableCode code="document_format" /></td><td><code>string</code></td><td>Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.</td></tr>
<tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td>Specify a target type to define the kinds of resources the document can run on.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.</td></tr>
<tr><td><CopyableCode code="requires" /></td><td><code>array</code></td><td>A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.</td></tr>
<tr><td><CopyableCode code="update_method" /></td><td><code>string</code></td><td>Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html"><code>AWS::SSM::Document</code></a>.

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
    <td><CopyableCode code="Content, region" /></td>
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
Gets all <code>documents</code> in a region.
```sql
SELECT
region,
content,
attachments,
name,
version_name,
document_type,
document_format,
target_type,
tags,
requires,
update_method
FROM aws.ssm.documents
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>document</code>.
```sql
SELECT
region,
content,
attachments,
name,
version_name,
document_type,
document_format,
target_type,
tags,
requires,
update_method
FROM aws.ssm.documents
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>document</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ssm.documents (
 Content,
 region
)
SELECT 
'{{ Content }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ssm.documents (
 Content,
 Attachments,
 Name,
 VersionName,
 DocumentType,
 DocumentFormat,
 TargetType,
 Tags,
 Requires,
 UpdateMethod,
 region
)
SELECT 
 '{{ Content }}',
 '{{ Attachments }}',
 '{{ Name }}',
 '{{ VersionName }}',
 '{{ DocumentType }}',
 '{{ DocumentFormat }}',
 '{{ TargetType }}',
 '{{ Tags }}',
 '{{ Requires }}',
 '{{ UpdateMethod }}',
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
  - name: document
    props:
      - name: Content
        value: {}
      - name: Attachments
        value:
          - Key: '{{ Key }}'
            Values:
              - '{{ Values[0] }}'
            Name: '{{ Name }}'
      - name: Name
        value: '{{ Name }}'
      - name: VersionName
        value: '{{ VersionName }}'
      - name: DocumentType
        value: '{{ DocumentType }}'
      - name: DocumentFormat
        value: '{{ DocumentFormat }}'
      - name: TargetType
        value: '{{ TargetType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Requires
        value:
          - Name: '{{ Name }}'
            Version: '{{ Version }}'
      - name: UpdateMethod
        value: '{{ UpdateMethod }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ssm.documents
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>documents</code> resource, the following permissions are required:

### Create
```json
ssm:CreateDocument,
ssm:GetDocument,
ssm:AddTagsToResource,
ssm:ListTagsForResource,
s3:GetObject,
iam:PassRole
```

### Read
```json
ssm:GetDocument,
ssm:ListTagsForResource
```

### Update
```json
ssm:UpdateDocument,
s3:GetObject,
ssm:AddTagsToResource,
ssm:RemoveTagsFromResource,
ssm:ListTagsForResource,
iam:PassRole,
ssm:UpdateDocumentDefaultVersion,
ssm:DescribeDocument
```

### Delete
```json
ssm:DeleteDocument,
ssm:GetDocument
```

### List
```json
ssm:ListDocuments
```
