---
title: publishers_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - publishers_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>publishers</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/publishers/"><code>publishers</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>publishers_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Register as a publisher in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.publishers_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="accept_terms_and_conditions" /></td><td><code>boolean</code></td><td>Whether you accept the terms and conditions for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to publish public extensions to the CloudFormation registry. The terms and conditions can be found at https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>publishers</code> in a region.
```sql
SELECT
region,
publisher_id
FROM aws.cloudformation.publishers_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>publishers_list_only</code> resource, see <a href="/providers/aws/cloudformation/publishers/#permissions"><code>publishers</code></a>


