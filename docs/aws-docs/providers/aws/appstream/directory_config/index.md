---
title: directory_config
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_config
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>directory_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.appstream.directory_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>OrganizationalUnitDistinguishedNames</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ServiceAccountCredentials</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DirectoryName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CertificateBasedAuthProperties</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appstream.directory_config
WHERE region = 'us-east-1' AND data__Identifier = '{DirectoryName}'
</pre>
