---
title: document
hide_title: false
hide_table_of_contents: false
keywords:
  - document
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
Gets or operates on an individual <code>document</code> resource, use <code>documents</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.document</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>content</code></td><td><code>object</code></td><td>The content for the Systems Manager document in JSON, YAML or String format.</td></tr>
<tr><td><code>attachments</code></td><td><code>array</code></td><td>A list of key and value pairs that describe attachments to a version of a document.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the Systems Manager document.</td></tr>
<tr><td><code>version_name</code></td><td><code>string</code></td><td>An optional field specifying the version of the artifact you are creating with the document. This value is unique across all versions of a document, and cannot be changed.</td></tr>
<tr><td><code>document_type</code></td><td><code>string</code></td><td>The type of document to create.</td></tr>
<tr><td><code>document_format</code></td><td><code>string</code></td><td>Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.</td></tr>
<tr><td><code>target_type</code></td><td><code>string</code></td><td>Specify a target type to define the kinds of resources the document can run on.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.</td></tr>
<tr><td><code>requires</code></td><td><code>array</code></td><td>A list of SSM documents required by a document. For example, an ApplicationConfiguration document requires an ApplicationConfigurationSchema document.</td></tr>
<tr><td><code>update_method</code></td><td><code>string</code></td><td>Update method - when set to 'Replace', the update will replace the existing document; when set to 'NewVersion', the update will create a new version.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.ssm.document
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>document</code> resource, the following permissions are required:

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

