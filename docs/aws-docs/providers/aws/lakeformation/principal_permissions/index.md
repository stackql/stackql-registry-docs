---
title: principal_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - principal_permissions
  - lakeformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>principal_permissions</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>principal_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.lakeformation.principal_permissions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Catalog</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Principal</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Resource</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Permissions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>PermissionsWithGrantOption</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>PrincipalIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResourceIdentifier</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lakeformation.principal_permissions
WHERE region = 'us-east-1' AND data__Identifier = '&lt;PrincipalIdentifier&gt;' AND data__Identifier = '&lt;ResourceIdentifier&gt;'
</pre>
