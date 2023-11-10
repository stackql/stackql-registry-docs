---
title: grant
hide_title: false
hide_table_of_contents: false
keywords:
  - grant
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
Gets an individual <code>grant</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grant</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>grant</td></tr>
<tr><td><b>Id</b></td><td><code>aws.licensemanager.grant</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>grant_arn</code></td><td><code>string</code></td><td>Arn of the grant.</td></tr>
<tr><td><code>grant_name</code></td><td><code>string</code></td><td>Name for the created Grant.</td></tr>
<tr><td><code>license_arn</code></td><td><code>string</code></td><td>License Arn for the grant.</td></tr>
<tr><td><code>home_region</code></td><td><code>string</code></td><td>Home region for the created grant.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The version of the grant.</td></tr>
<tr><td><code>allowed_operations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>principals</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
grant_arn,
grant_name,
license_arn,
home_region,
version,
allowed_operations,
principals,
status
FROM aws.licensemanager.grant
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;GrantArn&gt;'
```
