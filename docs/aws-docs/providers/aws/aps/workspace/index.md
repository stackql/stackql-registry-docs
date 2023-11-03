---
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
  - aps
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>workspace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.aps.workspace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>WorkspaceId</code></td><td><code>string</code></td><td>Required to identify a specific APS Workspace.</td></tr><tr><td><code>Alias</code></td><td><code>string</code></td><td>AMP Workspace alias.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>Workspace arn.</td></tr><tr><td><code>AlertManagerDefinition</code></td><td><code>string</code></td><td>The AMP Workspace alert manager definition data</td></tr><tr><td><code>PrometheusEndpoint</code></td><td><code>string</code></td><td>AMP Workspace prometheus endpoint</td></tr><tr><td><code>LoggingConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.aps.workspace
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>
