---
title: partner_app_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_app_tags
  - sagemaker
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

Expands all tag keys and values for <code>partner_apps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_app_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::PartnerApp</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.partner_app_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the created PartnerApp.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the PartnerApp.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of PartnerApp.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>The execution role for the user.</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td>The tier of the PartnerApp.</td></tr>
<tr><td><CopyableCode code="enable_iam_session_based_identity" /></td><td><code>boolean</code></td><td>Enables IAM Session based Identity for PartnerApp.</td></tr>
<tr><td><CopyableCode code="application_config" /></td><td><code>object</code></td><td>A collection of settings that specify the maintenance schedule for the PartnerApp.</td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td>The Auth type of PartnerApp.</td></tr>
<tr><td><CopyableCode code="base_url" /></td><td><code>string</code></td><td>The AppServerUrl based on app and account-info.</td></tr>
<tr><td><CopyableCode code="maintenance_config" /></td><td><code>object</code></td><td>A collection of settings that specify the maintenance schedule for the PartnerApp.</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>The client token for the PartnerApp.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>partner_apps</code> in a region.
```sql
SELECT
region,
arn,
name,
type,
execution_role_arn,
tier,
enable_iam_session_based_identity,
application_config,
auth_type,
base_url,
maintenance_config,
client_token,
tag_key,
tag_value
FROM aws.sagemaker.partner_app_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>partner_app_tags</code> resource, see <a href="/providers/aws/sagemaker/partner_apps/#permissions"><code>partner_apps</code></a>

