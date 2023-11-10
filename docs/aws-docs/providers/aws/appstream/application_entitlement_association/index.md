---
title: application_entitlement_association
hide_title: false
hide_table_of_contents: false
keywords:
  - application_entitlement_association
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application_entitlement_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_entitlement_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application_entitlement_association</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.application_entitlement_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>stack_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>entitlement_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
stack_name,
entitlement_name,
application_identifier
FROM aws.appstream.application_entitlement_association
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;StackName&gt;'
AND data__Identifier = '&lt;EntitlementName&gt;'
AND data__Identifier = '&lt;ApplicationIdentifier&gt;'
```
