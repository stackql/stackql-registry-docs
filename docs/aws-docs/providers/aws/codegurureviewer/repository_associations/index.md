---
title: repository_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_associations
  - codegurureviewer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>repository_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repository_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codegurureviewer.repository_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the repository to be associated.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>The type of repository to be associated.</td></tr>
<tr><td><code>Owner</code></td><td><code>string</code></td><td>The owner of the repository. For a Bitbucket repository, this is the username for the account that owns the repository.</td></tr>
<tr><td><code>BucketName</code></td><td><code>string</code></td><td>The name of the S3 bucket associated with an associated S3 repository. It must start with `codeguru-reviewer-`.</td></tr>
<tr><td><code>ConnectionArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection.</td></tr>
<tr><td><code>AssociationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the repository association.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags associated with a repository association.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.codegurureviewer.repository_associations
WHERE region = 'us-east-1'
</pre>
