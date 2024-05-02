---
title: component
hide_title: false
hide_table_of_contents: false
keywords:
  - component
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>component</code> resource, use <code>components</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Component</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.component</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the component.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the component.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The version of the component.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the component.</td></tr>
<tr><td><code>change_description</code></td><td><code>string</code></td><td>The change description of the component.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the component denotes whether the component is used to build the image or only to test it. </td></tr>
<tr><td><code>platform</code></td><td><code>string</code></td><td>The platform of the component.</td></tr>
<tr><td><code>data</code></td><td><code>string</code></td><td>The data of the component.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The KMS key identifier used to encrypt the component.</td></tr>
<tr><td><code>encrypted</code></td><td><code>boolean</code></td><td>The encryption status of the component.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The tags associated with the component.</td></tr>
<tr><td><code>uri</code></td><td><code>string</code></td><td>The uri of the component.</td></tr>
<tr><td><code>supported_os_versions</code></td><td><code>array</code></td><td>The operating system (OS) version supported by the component.</td></tr>
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
arn,
name,
version,
description,
change_description,
type,
platform,
data,
kms_key_id,
encrypted,
tags,
uri,
supported_os_versions
FROM aws.imagebuilder.component
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>component</code> resource, the following permissions are required:

### Read
```json
imagebuilder:GetComponent
```

### Delete
```json
imagebuilder:GetComponent,
imagebuilder:UnTagResource,
imagebuilder:DeleteComponent
```

