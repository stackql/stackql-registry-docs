---
title: contact_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_lists
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
Retrieves a list of <code>contact_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.contact_lists</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ContactListName</code></td><td><code>string</code></td><td>The name of the contact list.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the contact list.</td></tr><tr><td><code>Topics</code></td><td><code>array</code></td><td>The topics associated with the contact list.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the contact list.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.ses.contact_lists
WHERE region = 'us-east-1'
```
