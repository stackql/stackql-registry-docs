---
title: public_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - public_repositories
  - ecr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>public_repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>public_repositories</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecr.public_repositories</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RepositoryName</code></td><td><code>string</code></td><td>The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a&#x2F;nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html.</td></tr>
<tr><td><code>RepositoryPolicyText</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RepositoryCatalogData</code></td><td><code>object</code></td><td>The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see &lt;link&gt;</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ecr.public_repositories
WHERE region = 'us-east-1'
</pre>
