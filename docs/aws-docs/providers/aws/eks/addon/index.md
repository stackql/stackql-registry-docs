---
title: addon
hide_title: false
hide_table_of_contents: false
keywords:
  - addon
  - eks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>addon</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addon</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.eks.addon</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ClusterName</code></td><td><code>string</code></td><td>Name of Cluster</td></tr><tr><td><code>AddonName</code></td><td><code>string</code></td><td>Name of Addon</td></tr><tr><td><code>AddonVersion</code></td><td><code>string</code></td><td>Version of Addon</td></tr><tr><td><code>PreserveOnDelete</code></td><td><code>boolean</code></td><td>PreserveOnDelete parameter value</td></tr><tr><td><code>ResolveConflicts</code></td><td><code>string</code></td><td>Resolve parameter value conflicts</td></tr><tr><td><code>ServiceAccountRoleArn</code></td><td><code>string</code></td><td>IAM role to bind to the add-on's service account</td></tr><tr><td><code>ConfigurationValues</code></td><td><code>string</code></td><td>The configuration values to use with the add-on</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the add-on</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.eks.addon
WHERE region = 'us-east-1' AND data__Identifier = '{ClusterName}' AND data__Identifier = '{AddonName}'
</pre>
