---
title: directory_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_registrations
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
Retrieves a list of <code>directory_registrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>directory_registrations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pcaconnectorad.directory_registrations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>directory_registration_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>directory_registrations</code> resource, the following permissions are required:

### Create
<pre>
pca-connector-ad:GetDirectoryRegistration,
pca-connector-ad:CreateDirectoryRegistration,
ds:AuthorizeApplication,
ds:DescribeDirectories</pre>

### List
<pre>
pca-connector-ad:ListDirectoryRegistrations</pre>


## Example
```sql
SELECT
region,
directory_registration_arn
FROM awscc.pcaconnectorad.directory_registrations
WHERE region = 'us-east-1'
```
