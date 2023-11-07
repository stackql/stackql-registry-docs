---
title: domain_name_api_association
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name_api_association
  - appsync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain_name_api_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name_api_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain_name_api_association</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.domain_name_api_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiAssociationIdentifier</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appsync.domain_name_api_association
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ApiAssociationIdentifier&gt;'
</pre>
