---
title: base_path_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - base_path_mappings
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>base_path_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>base_path_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>base_path_mappings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.base_path_mappings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The domain name of the BasePathMapping resource to be described.</td></tr>
<tr><td><code>base_path</code></td><td><code>string</code></td><td>The base path name that callers of the API must provide as part of the URL after the domain name.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>base_path_mappings</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET
```

### List
```json
apigateway:GET
```


## Example
```sql
SELECT
region,
domain_name,
base_path
FROM awscc.apigateway.base_path_mappings
WHERE region = 'us-east-1'
```
