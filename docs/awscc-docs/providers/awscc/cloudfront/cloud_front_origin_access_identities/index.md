---
title: cloud_front_origin_access_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_front_origin_access_identities
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
Retrieves a list of <code>cloud_front_origin_access_identities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_front_origin_access_identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cloud_front_origin_access_identities</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.cloud_front_origin_access_identities</code></td></tr>
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

To operate on the <code>cloud_front_origin_access_identities</code> resource, the following permissions are required:

### Create
<pre>
cloudfront:CreateCloudFrontOriginAccessIdentity</pre>

### List
<pre>
cloudfront:ListCloudFrontOriginAccessIdentities</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.cloudfront.cloud_front_origin_access_identities

```