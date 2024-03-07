---
title: license
hide_title: false
hide_table_of_contents: false
keywords:
  - license
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
Gets an individual <code>license</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>license</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>license</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.licensemanager.license</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>product_sk_u</code></td><td><code>string</code></td><td>ProductSKU of the license.</td></tr>
<tr><td><code>issuer</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>license_name</code></td><td><code>string</code></td><td>Name for the created license.</td></tr>
<tr><td><code>product_name</code></td><td><code>string</code></td><td>Product name for the created license.</td></tr>
<tr><td><code>home_region</code></td><td><code>string</code></td><td>Home region for the created license.</td></tr>
<tr><td><code>validity</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>entitlements</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>beneficiary</code></td><td><code>string</code></td><td>Beneficiary of the license.</td></tr>
<tr><td><code>consumption_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>license_metadata</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>license_arn</code></td><td><code>string</code></td><td>Amazon Resource Name is a unique name for each resource.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The version of the license.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
product_sk_u,
issuer,
license_name,
product_name,
home_region,
validity,
entitlements,
beneficiary,
consumption_configuration,
license_metadata,
license_arn,
status,
version
FROM awscc.licensemanager.license
WHERE region = 'us-east-1'
AND data__Identifier = '{LicenseArn}';
```

## Permissions

To operate on the <code>license</code> resource, the following permissions are required:

### Read
```json
license-manager:GetLicense
```

### Update
```json
license-manager:CreateLicenseVersion
```

### Delete
```json
license-manager:DeleteLicense
```

