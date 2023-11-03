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
<tr><td><b>Id</b></td><td><code>aws.appconfig.configuration_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>LocationUri</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Validators</code></td><td><code>array</code></td><td></td></tr><tr><td><code>RetrievalRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApplicationId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.appconfig.configuration_profile
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
