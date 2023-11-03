---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
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
Retrieves a list of <code>grants</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.licensemanager.grants</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>GrantArn</code></td><td><code>undefined</code></td><td>Arn of the grant.</td></tr><tr><td><code>GrantName</code></td><td><code>string</code></td><td>Name for the created Grant.</td></tr><tr><td><code>LicenseArn</code></td><td><code>undefined</code></td><td>License Arn for the grant.</td></tr><tr><td><code>HomeRegion</code></td><td><code>string</code></td><td>Home region for the created grant.</td></tr><tr><td><code>Version</code></td><td><code>string</code></td><td>The version of the grant.</td></tr><tr><td><code>AllowedOperations</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Principals</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.licensemanager.grants
WHERE region = 'us-east-1'
</pre>
