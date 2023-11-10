---
title: cloud_formation_product
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_formation_product
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
Gets an individual <code>cloud_formation_product</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_formation_product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cloud_formation_product</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.cloud_formation_product</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>owner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>product_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>support_email</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>product_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provisioning_artifact_names</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>replace_provisioning_artifacts</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>support_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>distributor</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provisioning_artifact_ids</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>accept_language</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>support_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_connection</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>provisioning_artifact_parameters</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
owner,
description,
product_name,
support_email,
product_type,
provisioning_artifact_names,
name,
replace_provisioning_artifacts,
support_description,
distributor,
provisioning_artifact_ids,
accept_language,
support_url,
id,
source_connection,
tags,
provisioning_artifact_parameters
FROM aws.servicecatalog.cloud_formation_product
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
