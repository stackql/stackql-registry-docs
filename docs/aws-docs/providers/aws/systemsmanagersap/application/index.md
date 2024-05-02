---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - systemsmanagersap
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SystemsManagerSAP::Application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.systemsmanagersap.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the Helix application</td></tr>
<tr><td><code>credentials</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>instances</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>sap_instance_number</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sid</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags of a SystemsManagerSAP application.</td></tr>
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
application_id,
application_type,
arn,
credentials,
instances,
sap_instance_number,
sid,
tags
FROM aws.systemsmanagersap.application
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
ssm-sap:GetApplication,
ssm-sap:ListTagsForResource
```

### Update
```json
ssm-sap:TagResource,
ssm-sap:UntagResource,
ssm-sap:ListTagsForResource,
ssm-sap:GetApplication
```

### Delete
```json
ssm-sap:DeregisterApplication,
ssm-sap:GetApplication
```

