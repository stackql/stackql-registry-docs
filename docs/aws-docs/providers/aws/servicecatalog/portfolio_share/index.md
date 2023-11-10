---
title: portfolio_share
hide_title: false
hide_table_of_contents: false
keywords:
  - portfolio_share
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>portfolio_share</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portfolio_share</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>portfolio_share</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.portfolio_share</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>accept_language</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>portfolio_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>share_tag_options</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
accept_language,
portfolio_id,
account_id,
share_tag_options,
id
FROM aws.servicecatalog.portfolio_share
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
