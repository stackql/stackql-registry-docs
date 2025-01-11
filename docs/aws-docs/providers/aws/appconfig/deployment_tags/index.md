---
title: deployment_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_tags
  - appconfig
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

Expands all tag keys and values for <code>deployments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::Deployment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.deployment_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="deployment_strategy_id" /></td><td><code>string</code></td><td>The deployment strategy ID.</td></tr>
<tr><td><CopyableCode code="configuration_profile_id" /></td><td><code>string</code></td><td>The configuration profile ID.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The environment ID.</td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td>The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the deployment.</td></tr>
<tr><td><CopyableCode code="configuration_version" /></td><td><code>string</code></td><td>The configuration version to deploy. If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.</td></tr>
<tr><td><CopyableCode code="deployment_number" /></td><td><code>string</code></td><td>The sequence number of the deployment.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="dynamic_extension_parameters" /></td><td><code>array</code></td><td></td></tr>
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
Expands tags for all <code>deployments</code> in a region.
```sql
SELECT
region,
deployment_strategy_id,
configuration_profile_id,
environment_id,
kms_key_identifier,
description,
configuration_version,
deployment_number,
application_id,
dynamic_extension_parameters,
tag_key,
tag_value
FROM aws.appconfig.deployment_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>deployment_tags</code> resource, see <a href="/providers/aws/appconfig/deployments/#permissions"><code>deployments</code></a>

