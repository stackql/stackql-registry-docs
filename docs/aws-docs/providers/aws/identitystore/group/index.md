---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - identitystore
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.identitystore.group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A string containing the description of the group.</td></tr>
<tr><td><code>DisplayName</code></td><td><code>string</code></td><td>A string containing the name of the group. This value is commonly displayed when the group is referenced.</td></tr>
<tr><td><code>GroupId</code></td><td><code>string</code></td><td>The unique identifier for a group in the identity store.</td></tr>
<tr><td><code>IdentityStoreId</code></td><td><code>string</code></td><td>The globally unique identifier for the identity store.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.identitystore.group
WHERE region = 'us-east-1' AND data__Identifier = '&lt;GroupId&gt;' AND data__Identifier = '&lt;IdentityStoreId&gt;'
</pre>
