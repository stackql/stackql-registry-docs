---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
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
Retrieves a list of <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workspaces</td></tr>
<tr><td><b>Id</b></td><td><code>aws.aps.workspaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>WorkspaceId</code></td><td><code>string</code></td><td>Required to identify a specific APS Workspace.</td></tr>
<tr><td><code>Alias</code></td><td><code>string</code></td><td>AMP Workspace alias.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Workspace arn.</td></tr>
<tr><td><code>AlertManagerDefinition</code></td><td><code>string</code></td><td>The AMP Workspace alert manager definition data</td></tr>
<tr><td><code>PrometheusEndpoint</code></td><td><code>string</code></td><td>AMP Workspace prometheus endpoint</td></tr>
<tr><td><code>LoggingConfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.aps.workspaces<br/>WHERE region = 'us-east-1'
</pre>
