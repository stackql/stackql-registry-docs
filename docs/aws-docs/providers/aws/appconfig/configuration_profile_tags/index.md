---
title: configuration_profile_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile_tags
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

Expands all tag keys and values for <code>configuration_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profile_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.configuration_profile_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration_profile_id" /></td><td><code>string</code></td><td>The configuration profile ID</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>A URI to locate the configuration. You can specify the AWS AppConfig hosted configuration store, Systems Manager (SSM) document, an SSM Parameter Store parameter, or an Amazon S3 object.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of configurations contained in the profile. When calling this API, enter one of the following values for Type: AWS.AppConfig.FeatureFlags, AWS.Freeform</td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td>The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the configuration profile.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name of the AWS Key Management Service key to encrypt new configuration data versions in the AWS AppConfig hosted configuration store. This attribute is only used for hosted configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an AWS KMS key for that particular service.</td></tr>
<tr><td><CopyableCode code="validators" /></td><td><code>array</code></td><td>A list of methods for validating the configuration.</td></tr>
<tr><td><CopyableCode code="retrieval_role_arn" /></td><td><code>string</code></td><td>The ARN of an IAM role with permission to access the configuration at the specified LocationUri.</td></tr>
<tr><td><CopyableCode code="deletion_protection_check" /></td><td><code>string</code></td><td>On resource deletion this controls whether the Deletion Protection check should be applied, bypassed, or (the default) whether the behavior should be controlled by the account-level Deletion Protection setting. See https://docs.aws.amazon.com/appconfig/latest/userguide/deletion-protection.html</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the configuration profile.</td></tr>
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
Expands tags for all <code>configuration_profiles</code> in a region.
```sql
SELECT
region,
configuration_profile_id,
location_uri,
type,
kms_key_identifier,
description,
kms_key_arn,
validators,
retrieval_role_arn,
deletion_protection_check,
application_id,
name,
tag_key,
tag_value
FROM aws.appconfig.configuration_profile_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>configuration_profile_tags</code> resource, see <a href="/providers/aws/appconfig/configuration_profiles/#permissions"><code>configuration_profiles</code></a>

