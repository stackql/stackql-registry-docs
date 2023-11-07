---
title: publishers
hide_title: false
hide_table_of_contents: false
keywords:
  - publishers
  - cloudformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>publishers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>publishers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.cloudformation.publishers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AcceptTermsAndConditions</code></td><td><code>boolean</code></td><td>Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https:&#x2F;&#x2F;cloudformation-registry-documents.s3.amazonaws.com&#x2F;Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf</td></tr>
<tr><td><code>PublisherId</code></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
<tr><td><code>ConnectionArn</code></td><td><code>string</code></td><td>If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.</td></tr>
<tr><td><code>PublisherStatus</code></td><td><code>string</code></td><td>Whether the publisher is verified.</td></tr>
<tr><td><code>PublisherProfile</code></td><td><code>string</code></td><td>The URL to the publisher's profile with the identity provider.</td></tr>
<tr><td><code>IdentityProvider</code></td><td><code>string</code></td><td>The type of account used as the identity provider when registering this publisher with CloudFormation.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cloudformation.publishers
WHERE region = 'us-east-1'
</pre>
