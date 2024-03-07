---
title: location_azure_blobs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_azure_blobs
  - datasync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>location_azure_blobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_azure_blobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location_azure_blobs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.location_azure_blobs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Azure Blob Location that is created.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>location_azure_blobs</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationAzureBlob,
datasync:DescribeLocationAzureBlob,
datasync:TagResource,
datasync:ListTagsForResource
```

### List
```json
datasync:ListLocations
```


## Example
```sql
SELECT
region,
location_arn
FROM awscc.datasync.location_azure_blobs
WHERE region = 'us-east-1'
```
