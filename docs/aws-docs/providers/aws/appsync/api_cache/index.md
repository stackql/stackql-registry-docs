---
title: api_cache
hide_title: false
hide_table_of_contents: false
keywords:
  - api_cache
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
Gets an individual <code>api_cache</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_cache</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.appsync.api_cache</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TransitEncryptionEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>AtRestEncryptionEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApiCachingBehavior</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Ttl</code></td><td><code>number</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appsync.api_cache
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
