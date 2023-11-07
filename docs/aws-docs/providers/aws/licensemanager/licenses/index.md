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
<tr><td><b>Id</b></td><td><code>aws.licensemanager.licenses</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ProductSKU</code></td><td><code>string</code></td><td>ProductSKU of the license.</td></tr>
<tr><td><code>Issuer</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LicenseName</code></td><td><code>string</code></td><td>Name for the created license.</td></tr>
<tr><td><code>ProductName</code></td><td><code>string</code></td><td>Product name for the created license.</td></tr>
<tr><td><code>HomeRegion</code></td><td><code>string</code></td><td>Home region for the created license.</td></tr>
<tr><td><code>Validity</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Entitlements</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Beneficiary</code></td><td><code>string</code></td><td>Beneficiary of the license.</td></tr>
<tr><td><code>ConsumptionConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LicenseMetadata</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LicenseArn</code></td><td><code>undefined</code></td><td>Amazon Resource Name is a unique name for each resource.</td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Version</code></td><td><code>string</code></td><td>The version of the license.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.licensemanager.licenses<br/>WHERE region = 'us-east-1'
</pre>
