---
title: db_security_group_ingress
hide_title: false
hide_table_of_contents: false
keywords:
  - db_security_group_ingress
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>db_security_group_ingress</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_security_group_ingress</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_security_group_ingress</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_security_group_ingress</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CIDRIP</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DBSecurityGroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EC2SecurityGroupId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EC2SecurityGroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EC2SecurityGroupOwnerId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.rds.db_security_group_ingress<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
