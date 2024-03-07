---
title: origin_request_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_request_policies
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>origin_request_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_request_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>origin_request_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.origin_request_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>origin_request_policies</code> resource, the following permissions are required:

### Create
<pre>
cloudfront:CreateOriginRequestPolicy</pre>

### List
<pre>
cloudfront:ListOriginRequestPolicies</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.cloudfront.origin_request_policies

```
