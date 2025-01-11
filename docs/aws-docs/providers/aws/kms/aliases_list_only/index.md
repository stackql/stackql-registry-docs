---
title: aliases_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases_list_only
  - kms
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

Lists <code>aliases</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/aliases/"><code>aliases</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::KMS::Alias</code> resource specifies a display name for a &#91;KMS key&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys). You can use an alias to identify a KMS key in the KMS console, in the &#91;DescribeKey&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) operation, and in &#91;cryptographic operations&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations), such as &#91;Decrypt&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) and &#91;GenerateDataKey&#93;(https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html).<br />Adding, deleting, or updating an alias can allow or deny permission to the KMS key. For details, see &#91;ABAC for&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the *Developer Guide*.<br />Using an alias to refer to a KMS key can help you simplify key management. For example, an alias in your code can be associated with different KMS keys in different AWS-Regions. For more information, see &#91;Using aliases&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html) in the *Developer Guide*.<br />When specifying an alias, observe the following rules.<br />+ Each alias is associated with one KMS key, but multiple aliases can be associated with the same KMS key.<br />+ The alias and its associated KMS key must be in the same AWS-account and Region.<br />+ The alias name must be unique in the AWS-account and Region. However, you can create aliases with the same name in different AWS-Regions. For example, you can have an <code>alias/projectKey</code> in multiple Regions, each of which is associated with a KMS key in its Region.<br />+ Each alias name must begin with <code>alias/</code> followed by a name, such as <code>alias/exampleKey</code>. The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with <code>alias/aws/</code>. That alias name prefix is reserved for &#91;&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).<br /><br />*Regions* <br />KMS CloudFormation resources are available in all AWS-Regions in which KMS and CFN are supported.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.aliases_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alias_name" /></td><td><code>string</code></td><td>Specifies the alias name. This value must begin with <code>alias/</code> followed by a name, such as <code>alias/ExampleAlias</code>. <br />If you change the value of the <code>AliasName</code> property, the existing alias is deleted and a new alias is created for the specified KMS key. This change can disrupt applications that use the alias. It can also allow or deny access to a KMS key affected by attribute-based access control (ABAC).<br />The alias must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). The alias name cannot begin with <code>alias/aws/</code>. The <code>alias/aws/</code> prefix is reserved for &#91;&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk).</td></tr>
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
Lists all <code>aliases</code> in a region.
```sql
SELECT
region,
alias_name
FROM aws.kms.aliases_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>aliases_list_only</code> resource, see <a href="/providers/aws/kms/aliases/#permissions"><code>aliases</code></a>

