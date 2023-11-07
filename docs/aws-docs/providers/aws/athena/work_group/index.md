---
title: work_group
hide_title: false
hide_table_of_contents: false
keywords:
  - work_group
  - athena
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>work_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>work_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>work_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.athena.work_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The workGroup name.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The workgroup description.</td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td>One or more tags, separated by commas, that you want to attach to the workgroup as you create it</td></tr>
<tr><td><code>WorkGroupConfiguration</code></td><td><code>undefined</code></td><td>The workgroup configuration</td></tr>
<tr><td><code>WorkGroupConfigurationUpdates</code></td><td><code>undefined</code></td><td>The workgroup configuration update object</td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td>The date and time the workgroup was created.</td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td>The state of the workgroup: ENABLED or DISABLED.</td></tr>
<tr><td><code>RecursiveDeleteOption</code></td><td><code>boolean</code></td><td>The option to delete the workgroup and its contents even if the workgroup contains any named queries.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.athena.work_group
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;'
</pre>
