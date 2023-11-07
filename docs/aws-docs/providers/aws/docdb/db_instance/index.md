---
title: db_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - db_instance
  - docdb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>db_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.docdb.db_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DBInstanceClass</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Port</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DBClusterIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AvailabilityZone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PreferredMaintenanceWindow</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EnablePerformanceInsights</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>AutoMinorVersionUpgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DBInstanceIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.docdb.db_instance<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
