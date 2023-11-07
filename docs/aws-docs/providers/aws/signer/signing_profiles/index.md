---
title: signing_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - signing_profiles
  - signer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>signing_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signing_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>signing_profiles</td></tr>
<tr><td><b>Id</b></td><td><code>aws.signer.signing_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ProfileName</code></td><td><code>string</code></td><td>A name for the signing profile. AWS CloudFormation generates a unique physical ID and uses that ID for the signing profile name. </td></tr>
<tr><td><code>ProfileVersion</code></td><td><code>undefined</code></td><td>A version for the signing profile. AWS Signer generates a unique version for each profile of the same profile name.</td></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the specified signing profile.</td></tr>
<tr><td><code>ProfileVersionArn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the specified signing profile version.</td></tr>
<tr><td><code>SignatureValidityPeriod</code></td><td><code>undefined</code></td><td>Signature validity period of the profile.</td></tr>
<tr><td><code>PlatformId</code></td><td><code>undefined</code></td><td>The ID of the target signing platform.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of tags associated with the signing profile.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.signer.signing_profiles
WHERE region = 'us-east-1'
</pre>
