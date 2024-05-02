---
title: data_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - data_provider
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>data_provider</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::DataProvider</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dms.data_provider</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>data_provider_name</code></td><td><code>string</code></td><td>The property describes a name to identify the data provider.</td></tr>
<tr><td><code>data_provider_identifier</code></td><td><code>string</code></td><td>The property describes an identifier for the data provider. It is used for describing&#x2F;deleting&#x2F;modifying can be name&#x2F;arn</td></tr>
<tr><td><code>data_provider_arn</code></td><td><code>string</code></td><td>The data provider ARN.</td></tr>
<tr><td><code>data_provider_creation_time</code></td><td><code>string</code></td><td>The data provider creation time.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The optional description of the data provider.</td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td>The property describes a data engine for the data provider.</td></tr>
<tr><td><code>exact_settings</code></td><td><code>boolean</code></td><td>The property describes the exact settings which can be modified</td></tr>
<tr><td><code>settings</code></td><td><code>object</code></td><td>The property identifies the exact type of settings for the data provider.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
data_provider_name,
data_provider_identifier,
data_provider_arn,
data_provider_creation_time,
description,
engine,
exact_settings,
settings,
tags
FROM aws.dms.data_provider
WHERE data__Identifier = '<DataProviderArn>';
```

## Permissions

To operate on the <code>data_provider</code> resource, the following permissions are required:

### Read
```json
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:ListTagsForResource
```

### Update
```json
dms:UpdateDataProvider,
dms:ModifyDataProvider,
dms:AddTagsToResource,
dms:RemoveTagsToResource,
dms:ListTagsForResource
```

### Delete
```json
dms:DeleteDataProvider
```

