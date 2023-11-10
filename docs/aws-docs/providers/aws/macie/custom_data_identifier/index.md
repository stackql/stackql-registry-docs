---
title: custom_data_identifier
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_data_identifier
  - macie
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>custom_data_identifier</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_data_identifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>custom_data_identifier</td></tr>
<tr><td><b>Id</b></td><td><code>aws.macie.custom_data_identifier</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of custom data identifier.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of custom data identifier.</td></tr>
<tr><td><code>regex</code></td><td><code>string</code></td><td>Regular expression for custom data identifier.</td></tr>
<tr><td><code>maximum_match_distance</code></td><td><code>integer</code></td><td>Maximum match distance.</td></tr>
<tr><td><code>keywords</code></td><td><code>array</code></td><td>Keywords to be matched against.</td></tr>
<tr><td><code>ignore_words</code></td><td><code>array</code></td><td>Words to be ignored.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Custom data identifier ID.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Custom data identifier ARN.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
regex,
maximum_match_distance,
keywords,
ignore_words,
id,
arn
FROM aws.macie.custom_data_identifier
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
