---
title: source_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - source_locations
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
Retrieves a list of <code>source_locations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>source_locations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediatailor.source_locations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>source_location_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>source_locations</code> resource, the following permissions are required:

### Create
```json
mediatailor:CreateSourceLocation,
mediatailor:DescribeSourceLocation,
mediatailor:TagResource,
secretsmanager:DescribeSecret,
secretsmanager:GetSecretValue,
kms:CreateGrant
```

### List
```json
mediatailor:ListSourceLocations
```


## Example
```sql
SELECT
region,
source_location_name
FROM awscc.mediatailor.source_locations
WHERE region = 'us-east-1'
```
