---
title: endpoint_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_authorizations
  - redshift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>endpoint_authorizations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>endpoint_authorizations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.endpoint_authorizations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_identifier</code></td><td><code>string</code></td><td>The cluster identifier.</td></tr>
<tr><td><code>account</code></td><td><code>undefined</code></td><td>The target AWS account ID to grant or revoke access for.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>endpoint_authorizations</code> resource, the following permissions are required:

### Create
<pre>
redshift:AuthorizeEndpointAccess,
redshift:DescribeEndpointAuthorization</pre>

### List
<pre>
redshift:DescribeEndpointAuthorization</pre>


## Example
```sql
SELECT
region,
cluster_identifier,
account
FROM awscc.redshift.endpoint_authorizations
WHERE region = 'us-east-1'
```
