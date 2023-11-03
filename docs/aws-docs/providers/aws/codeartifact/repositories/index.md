---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - codeartifact
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codeartifact.repositories</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RepositoryName</code></td><td><code>string</code></td><td>The name of the repository.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the repository. This is used for GetAtt</td></tr><tr><td><code>DomainName</code></td><td><code>string</code></td><td>The name of the domain that contains the repository.</td></tr><tr><td><code>DomainOwner</code></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A text description of the repository.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the repository.</td></tr><tr><td><code>ExternalConnections</code></td><td><code>array</code></td><td>A list of external connections associated with the repository.</td></tr><tr><td><code>Upstreams</code></td><td><code>array</code></td><td>A list of upstream repositories associated with the repository.</td></tr><tr><td><code>PermissionsPolicyDocument</code></td><td><code>object</code></td><td>The access control resource policy on the provided repository.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.codeartifact.repositories
WHERE region = 'us-east-1'
</pre>
