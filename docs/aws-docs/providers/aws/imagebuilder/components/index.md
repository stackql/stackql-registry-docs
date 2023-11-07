---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>components</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.components</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the component.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the component.</td></tr>
<tr><td><code>Version</code></td><td><code>string</code></td><td>The version of the component.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the component.</td></tr>
<tr><td><code>ChangeDescription</code></td><td><code>string</code></td><td>The change description of the component.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>The type of the component denotes whether the component is used to build the image or only to test it. </td></tr>
<tr><td><code>Platform</code></td><td><code>string</code></td><td>The platform of the component.</td></tr>
<tr><td><code>Data</code></td><td><code>string</code></td><td>The data of the component.</td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td>The KMS key identifier used to encrypt the component.</td></tr>
<tr><td><code>Encrypted</code></td><td><code>boolean</code></td><td>The encryption status of the component.</td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>The tags associated with the component.</td></tr>
<tr><td><code>Uri</code></td><td><code>string</code></td><td>The uri of the component.</td></tr>
<tr><td><code>SupportedOsVersions</code></td><td><code>array</code></td><td>The operating system (OS) version supported by the component.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.imagebuilder.components
WHERE region = 'us-east-1'
</pre>
