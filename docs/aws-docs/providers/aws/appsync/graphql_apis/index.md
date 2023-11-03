---
title: graphql_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - graphql_apis
  - appsync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>graphql_apis</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graphql_apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.graphql_apis</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>OpenIDConnectConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AdditionalAuthenticationProviders</code></td><td><code>array</code></td><td></td></tr><tr><td><code>GraphQLUrl</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LambdaAuthorizerConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>XrayEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UserPoolConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>AuthenticationType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LogConfig</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appsync.graphql_apis
WHERE region = 'us-east-1'
</pre>
