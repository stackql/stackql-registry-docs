---
title: dev_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_endpoint
  - glue
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dev_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dev_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.glue.dev_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ExtraJarsS3Path</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PublicKey</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NumberOfNodes</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Arguments</code></td><td><code>object</code></td><td></td></tr><tr><td><code>SubnetId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PublicKeys</code></td><td><code>array</code></td><td></td></tr><tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>WorkerType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EndpointName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>GlueVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ExtraPythonLibsS3Path</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SecurityConfiguration</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NumberOfWorkers</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.glue.dev_endpoint
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
