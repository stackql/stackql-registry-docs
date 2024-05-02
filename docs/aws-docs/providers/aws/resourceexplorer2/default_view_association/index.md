---
title: default_view_association
hide_title: false
hide_table_of_contents: false
keywords:
  - default_view_association
  - resourceexplorer2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>default_view_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>default_view_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ResourceExplorer2::DefaultViewAssociation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.resourceexplorer2.default_view_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>view_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>associated_aws_principal</code></td><td><code>string</code></td><td>The AWS principal that the default view is associated with, used as the unique identifier for this resource.</td></tr>
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
view_arn,
associated_aws_principal
FROM aws.resourceexplorer2.default_view_association
WHERE data__Identifier = '<AssociatedAwsPrincipal>';
```

## Permissions

To operate on the <code>default_view_association</code> resource, the following permissions are required:

### Update
```json
resource-explorer-2:GetDefaultView,
resource-explorer-2:AssociateDefaultView
```

### Read
```json
resource-explorer-2:GetDefaultView
```

### Delete
```json
resource-explorer-2:GetDefaultView,
resource-explorer-2:DisassociateDefaultView
```

