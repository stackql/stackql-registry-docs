---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - amplify
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amplify.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AppId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AutoSubDomainCreationPatterns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AutoSubDomainIAMRole</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CertificateRecord</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DomainStatus</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EnableAutoSubDomain</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>StatusReason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SubDomainSettings</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.amplify.domain<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
