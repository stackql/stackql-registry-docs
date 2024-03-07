---
title: licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses
  - licensemanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>licenses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>licenses</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.licensemanager.licenses</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>license_arn</code></td><td><code>undefined</code></td><td>Amazon Resource Name is a unique name for each resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>licenses</code> resource, the following permissions are required:

### Create
```json
license-manager:CreateLicense
```

### List
```json
license-manager:ListLicenses
```


## Example
```sql
SELECT
region,
license_arn
FROM awscc.licensemanager.licenses
WHERE region = 'us-east-1'
```
