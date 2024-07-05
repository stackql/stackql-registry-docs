---
title: licenses_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>licenses</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/licenses/"><code>licenses</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>licenses_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::LicenseManager::License</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.licensemanager.licenses_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="product_sku" /></td><td><code>string</code></td><td>ProductSKU of the license.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>licenses</code> in a region.
```sql
SELECT
region,
license_arn
FROM aws.licensemanager.licenses_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>licenses_list_only</code> resource, see <a href="/providers/aws/licensemanager/licenses/#permissions"><code>licenses</code></a>


