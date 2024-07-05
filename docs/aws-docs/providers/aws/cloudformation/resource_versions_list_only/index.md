---
title: resource_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_versions_list_only
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

Lists <code>resource_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resource_versions/"><code>resource_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource that has been registered in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.resource_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type, here the ResourceVersion. This is used to uniquely identify a ResourceVersion resource</td></tr>
<tr><td><CopyableCode code="type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type without the versionID.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM execution role to use to register the type. If your resource type calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your resource type with the appropriate credentials.</td></tr>
<tr><td><CopyableCode code="is_default_version" /></td><td><code>boolean</code></td><td>Indicates if this type version is the current default version</td></tr>
<tr><td><CopyableCode code="logging_config" /></td><td><code>object</code></td><td>Specifies logging configuration information for a type.</td></tr>
<tr><td><CopyableCode code="provisioning_type" /></td><td><code>string</code></td><td>The provisioning behavior of the type. AWS CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</td></tr>
<tr><td><CopyableCode code="schema_handler_package" /></td><td><code>string</code></td><td>A url to the S3 bucket containing the schema handler package that contains the schema, event handlers, and associated files for the type you want to register.<br />For information on generating a schema handler package for the type you want to register, see submit in the CloudFormation CLI User Guide.</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.<br />We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="version_id" /></td><td><code>string</code></td><td>The ID of the version of the type represented by this resource instance.</td></tr>
<tr><td><CopyableCode code="visibility" /></td><td><code>string</code></td><td>The scope at which the type is visible and usable in CloudFormation operations.<br />Valid values include:<br />PRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.<br />PUBLIC: The type is publically visible and usable within any Amazon account.</td></tr>
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
Lists all <code>resource_versions</code> in a region.
```sql
SELECT
region,
arn
FROM aws.cloudformation.resource_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_versions_list_only</code> resource, see <a href="/providers/aws/cloudformation/resource_versions/#permissions"><code>resource_versions</code></a>


