---
title: documentation_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - documentation_versions
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
Retrieves a list of <code>documentation_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documentation_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>documentation_versions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.documentation_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>documentation_version</code></td><td><code>string</code></td><td>The version identifier of the to-be-updated documentation version.</td></tr>
<tr><td><code>rest_api_id</code></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>documentation_versions</code> resource, the following permissions are required:

### Create
<pre>
apigateway:GET,
apigateway:POST</pre>

### List
<pre>
apigateway:GET</pre>


## Example
```sql
SELECT
region,
documentation_version,
rest_api_id
FROM awscc.apigateway.documentation_versions
WHERE region = 'us-east-1'
```
