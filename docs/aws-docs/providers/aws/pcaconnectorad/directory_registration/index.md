---
title: directory_registration
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_registration
  - pcaconnectorad
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>directory_registration</code> resource, use <code>directory_registrations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_registration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::DirectoryRegistration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pcaconnectorad.directory_registration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>directory_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>directory_registration_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
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
directory_id,
directory_registration_arn,
tags
FROM aws.pcaconnectorad.directory_registration
WHERE data__Identifier = '<DirectoryRegistrationArn>';
```

## Permissions

To operate on the <code>directory_registration</code> resource, the following permissions are required:

### Read
```json
pca-connector-ad:ListTagsForResource,
pca-connector-ad:GetDirectoryRegistration
```

### Delete
```json
pca-connector-ad:GetDirectoryRegistration,
pca-connector-ad:DeleteDirectoryRegistration,
ds:DescribeDirectories,
ds:UnauthorizeApplication,
ds:UpdateAuthorizedApplication
```

### Update
```json
pca-connector-ad:ListTagsForResource,
pca-connector-ad:TagResource,
pca-connector-ad:UntagResource
```

