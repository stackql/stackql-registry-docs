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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>license</code> resource, use <code>licenses</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>license</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::LicenseManager::License</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.licensemanager.license" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="product_sku" /></td><td><code>string</code></td><td>ProductSKU of the license.</td></tr>
<tr><td><CopyableCode code="issuer" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="license_name" /></td><td><code>string</code></td><td>Name for the created license.</td></tr>
<tr><td><CopyableCode code="product_name" /></td><td><code>string</code></td><td>Product name for the created license.</td></tr>
<tr><td><CopyableCode code="home_region" /></td><td><code>string</code></td><td>Home region for the created license.</td></tr>
<tr><td><CopyableCode code="validity" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="entitlements" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="beneficiary" /></td><td><code>string</code></td><td>Beneficiary of the license.</td></tr>
<tr><td><CopyableCode code="consumption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="license_metadata" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="license_arn" /></td><td><code>string</code></td><td>Amazon Resource Name is a unique name for each resource.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the license.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
product_sku,
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
FROM aws.licensemanager.license
WHERE data__Identifier = '<LicenseArn>';
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

