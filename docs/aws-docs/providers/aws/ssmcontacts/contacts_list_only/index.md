---
title: contacts_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts_list_only
  - ssmcontacts
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

Lists <code>contacts</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/contacts/"><code>contacts</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contacts_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSMContacts::Contact</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmcontacts.contacts_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>Alias of the contact. String value with 20 to 256 characters. Only alphabetical, numeric characters, dash, or underscore allowed.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>Name of the contact. String value with 3 to 256 characters. Only alphabetical, space, numeric characters, dash, or underscore allowed.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Contact type, which specify type of contact. Currently supported values: “PERSONAL”, “SHARED”, “OTHER“.</td></tr>
<tr><td><CopyableCode code="plan" /></td><td><code>array</code></td><td>The stages that an escalation plan or engagement plan engages contacts and contact methods in.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the contact.</td></tr>
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
Lists all <code>contacts</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ssmcontacts.contacts_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>contacts_list_only</code> resource, see <a href="/providers/aws/ssmcontacts/contacts/#permissions"><code>contacts</code></a>


