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
Retrieves a list of <code>documents</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.documents</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the Systems Manager document.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name
FROM aws.ssm.documents
WHERE region = 'us-east-1'
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

### List
```json
ssm:ListDocuments
```

