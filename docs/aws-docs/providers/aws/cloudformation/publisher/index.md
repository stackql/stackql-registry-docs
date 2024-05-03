---
title: publisher
hide_title: false
hide_table_of_contents: false
keywords:
  - publisher
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>publisher</code> resource, use <code>publishers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>publisher</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Register as a publisher in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.publisher" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="accept_terms_and_conditions" /></td><td><code>boolean</code></td><td>Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https:&#x2F;&#x2F;cloudformation-registry-documents.s3.amazonaws.com&#x2F;Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf</td></tr>
<tr><td><CopyableCode code="publisher_id" /></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
<tr><td><CopyableCode code="connection_arn" /></td><td><code>string</code></td><td>If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.</td></tr>
<tr><td><CopyableCode code="publisher_status" /></td><td><code>string</code></td><td>Whether the publisher is verified.</td></tr>
<tr><td><CopyableCode code="publisher_profile" /></td><td><code>string</code></td><td>The URL to the publisher's profile with the identity provider.</td></tr>
<tr><td><CopyableCode code="identity_provider" /></td><td><code>string</code></td><td>The type of account used as the identity provider when registering this publisher with CloudFormation.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
accept_terms_and_conditions,
publisher_id,
connection_arn,
publisher_status,
publisher_profile,
identity_provider
FROM aws.cloudformation.publisher
WHERE data__Identifier = '<PublisherId>';
```

## Permissions

To operate on the <code>publisher</code> resource, the following permissions are required:

### Read
```json
cloudformation:DescribePublisher
```

