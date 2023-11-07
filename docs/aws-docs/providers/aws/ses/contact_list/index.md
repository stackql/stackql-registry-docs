---
title: contact_list
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_list
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>contact_list</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ses.contact_list</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ContactListName</code></td><td><code>string</code></td><td>The name of the contact list.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the contact list.</td></tr>
<tr><td><code>Topics</code></td><td><code>array</code></td><td>The topics associated with the contact list.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the contact list.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ses.contact_list
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ContactListName&gt;'
</pre>
