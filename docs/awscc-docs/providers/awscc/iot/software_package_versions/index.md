---
title: software_package_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - software_package_versions
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>software_package_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_package_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>software_package_versions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.software_package_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>package_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>version_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>software_package_versions</code> resource, the following permissions are required:

### Create
<pre>
iot:CreatePackageVersion,
iot:GetPackageVersion,
iot:TagResource,
iot:GetIndexingConfiguration</pre>

### List
<pre>
iot:ListPackageVersions</pre>


## Example
```sql
SELECT
region,
package_name,
version_name
FROM awscc.iot.software_package_versions
WHERE region = 'us-east-1'
```
