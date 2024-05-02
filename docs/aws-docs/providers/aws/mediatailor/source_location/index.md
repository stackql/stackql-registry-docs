---
title: source_location
hide_title: false
hide_table_of_contents: false
keywords:
  - source_location
  - mediatailor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>source_location</code> resource, use <code>source_locations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_location</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::SourceLocation Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediatailor.source_location</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The ARN of the source location.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>default_segment_delivery_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>http_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>segment_delivery_configurations</code></td><td><code>array</code></td><td>&lt;p&gt;A list of the segment delivery configurations associated with this resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>source_location_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to assign to the source location.</td></tr>
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
access_configuration,
arn,
default_segment_delivery_configuration,
http_configuration,
segment_delivery_configurations,
source_location_name,
tags
FROM aws.mediatailor.source_location
WHERE data__Identifier = '<SourceLocationName>';
```

## Permissions

To operate on the <code>source_location</code> resource, the following permissions are required:

### Read
```json
mediatailor:DescribeSourceLocation
```

### Update
```json
mediatailor:DescribeSourceLocation,
mediatailor:TagResource,
mediatailor:UntagResource,
mediatailor:UpdateSourceLocation,
secretsmanager:DescribeSecret,
secretsmanager:GetSecretValue,
kms:CreateGrant
```

### Delete
```json
mediatailor:DeleteSourceLocation,
mediatailor:DescribeSourceLocation
```

