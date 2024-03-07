---
title: packaging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - packaging_configurations
  - mediapackage
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>packaging_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>packaging_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediapackage.packaging_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the PackagingConfiguration.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>packaging_configurations</code> resource, the following permissions are required:

### Create
```json
mediapackage-vod:CreatePackagingConfiguration,
mediapackage-vod:DescribePackagingConfiguration,
mediapackage-vod:TagResource,
iam:PassRole
```

### List
```json
mediapackage-vod:ListPackagingConfigurations,
mediapackage-vod:DescribePackagingGroup
```


## Example
```sql
SELECT
region,
id
FROM awscc.mediapackage.packaging_configurations
WHERE region = 'us-east-1'
```
