---
title: configuration_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>configuration_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_profile</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appconfig.configuration_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>validators</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>retrieval_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
location_uri,
type,
description,
validators,
retrieval_role_arn,
id,
application_id,
tags,
name
FROM aws.appconfig.configuration_profile
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
