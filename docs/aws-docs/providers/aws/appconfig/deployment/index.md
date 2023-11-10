---
title: deployment
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment
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
Gets an individual <code>deployment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deployment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appconfig.deployment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>deployment_strategy_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configuration_profile_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configuration_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
deployment_strategy_id,
configuration_profile_id,
environment_id,
kms_key_identifier,
description,
configuration_version,
id,
application_id,
tags
FROM aws.appconfig.deployment
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
