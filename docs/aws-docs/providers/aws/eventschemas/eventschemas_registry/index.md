---
title: eventschemas_registry
hide_title: false
hide_table_of_contents: false
keywords:
  - eventschemas_registry
  - eventschemas
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>eventschemas_registry</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eventschemas_registry</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Registry</td></tr>
<tr><td><b>Id</b></td><td><code>aws.eventschemas.eventschemas_registry</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>registry_name</code></td><td><code>string</code></td><td>The name of the schema registry.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the registry to be created.</td></tr>
<tr><td><code>registry_arn</code></td><td><code>string</code></td><td>The ARN of the registry.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags associated with the resource.</td></tr>
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
registry_name,
description,
registry_arn,
tags
FROM aws.eventschemas.eventschemas_registry
WHERE data__Identifier = '<RegistryArn>';
```

## Permissions

To operate on the <code>eventschemas_registry</code> resource, the following permissions are required:

### Read
```json
schemas:DescribeRegistry
```

### Update
```json
schemas:DescribeRegistry,
schemas:UpdateRegistry,
schemas:TagResource,
schemas:UntagResource,
schemas:ListTagsForResource
```

### Delete
```json
schemas:DescribeRegistry,
schemas:DeleteRegistry
```

