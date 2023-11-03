---
title: package_version
hide_title: false
hide_table_of_contents: false
keywords:
  - package_version
  - panorama
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>package_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.panorama.package_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>OwnerAccount</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PackageId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PackageArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PackageVersion</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PatchVersion</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>MarkLatest</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>IsLatestPatch</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>PackageName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StatusDescription</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RegisteredTime</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>UpdatedLatestPatchVersion</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.panorama.package_version
WHERE region = 'us-east-1' AND data__Identifier = '{PackageId}' AND data__Identifier = '{PackageVersion}' AND data__Identifier = '{PatchVersion}'
</pre>
