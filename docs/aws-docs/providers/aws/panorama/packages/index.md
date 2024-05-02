---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
  - panorama
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>packages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for Package CloudFormation Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.panorama.packages</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>package_id</code></td><td><code>undefined</code></td><td></td></tr>
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
package_id
FROM aws.panorama.packages
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>packages</code> resource, the following permissions are required:

### Create
```json
panorama:CreatePackage,
panorama:ListTagsForResource,
panorama:TagResource,
panorama:DescribePackage,
s3:ListBucket,
s3:PutObject,
s3:GetObject,
s3:GetObjectVersion
```

### List
```json
panorama:ListPackages,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

