---
title: cluster_security_group_ingress
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_security_group_ingress
  - redshift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster_security_group_ingress</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_security_group_ingress</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster_security_group_ingress</td></tr>
<tr><td><b>Id</b></td><td><code>aws.redshift.cluster_security_group_ingress</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>c_id_ri_p</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cluster_security_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>e_c2_security_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>e_c2_security_group_owner_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
c_id_ri_p,
cluster_security_group_name,
e_c2_security_group_name,
e_c2_security_group_owner_id
FROM aws.redshift.cluster_security_group_ingress
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
