---
title: connector
hide_title: false
hide_table_of_contents: false
keywords:
  - connector
  - pcaconnectorad
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>connector</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connector</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pcaconnectorad.connector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_authority_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connector_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>directory_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>vpc_information</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>connector</code> resource, the following permissions are required:

### Read
<pre>
pca-connector-ad:ListTagsForResource,
pca-connector-ad:GetConnector</pre>

### Delete
<pre>
pca-connector-ad:GetConnector,
pca-connector-ad:DeleteConnector,
ec2:DeleteVpcEndpoints,
ec2:DescribeVpcEndpoints</pre>

### Update
<pre>
pca-connector-ad:ListTagsForResource,
pca-connector-ad:TagResource,
pca-connector-ad:UntagResource</pre>


## Example
```sql
SELECT
region,
certificate_authority_arn,
connector_arn,
directory_id,
tags,
vpc_information
FROM awscc.pcaconnectorad.connector
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ConnectorArn&gt;'
```
